"""Read-only delivery gate: checks current files and reports, never removes pixels."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys

from png_provenance_export import inspect
from recipe_library import validate_visual_checks
from verify_pixel_watermark import classify, ENDPOINT
from detect_image_signals import validate_coverage


def load(path):
    path = Path(path).resolve()
    data = path.read_bytes()
    value = json.loads(data.decode('utf-8-sig'))
    if not isinstance(value, dict):
        raise ValueError('Expected a JSON object')
    return value, {'file': str(path), 'sha256': hashlib.sha256(data).hexdigest()}


def evaluate(image, review_path, metadata_path, pixel_path, metadata_policy='remove-c2pa', accept_pixel_limitations=False, coverage_path=None):
    if metadata_policy not in ('remove-c2pa', 'preserve') or type(accept_pixel_limitations) is not bool:
        raise ValueError('Invalid delivery policy')
    image = Path(image).resolve()
    actual = inspect(image.read_bytes())
    reasons = []
    evidence = {}
    tracked_files = {str(image): actual['sha256']}
    pixel = {'outcome': 'unknown', 'state': 'unavailable', 'removal': 'not-performed'}
    coverage = None
    try:
        metadata, evidence['metadata_report'] = load(metadata_path)
        source = metadata.get('source', {})
        output = metadata.get('output', {})
        if not isinstance(source, dict) or not isinstance(output, dict):
            raise ValueError('Metadata file references must be objects')
        if Path(output.get('file', '')).resolve() != image or output.get('sha256') != actual['sha256']:
            raise ValueError('Metadata report does not match the current export')
        original_path = Path(source['file']).resolve()
        original = inspect(original_path.read_bytes())
        tracked_files[str(original_path)] = original['sha256']
        if original['sha256'] != source.get('sha256') or original['retained_chunks_sha256'] != actual['retained_chunks_sha256']:
            raise ValueError('Source changed or non-C2PA data changed')
        if metadata.get('policy') != metadata_policy or metadata.get('original_unchanged') is not True:
            raise ValueError('Metadata policy or source integrity is not satisfied')
        if metadata_policy == 'remove-c2pa' and (actual['c2pa_chunk_count'] or any(actual['metadata_marker_presence'].values()) or metadata.get('metadata_status') not in ('removed', 'not-present')):
            raise ValueError('Requested metadata removal is incomplete')
        if metadata_policy == 'preserve' and original['sha256'] != actual['sha256']:
            raise ValueError('Preserve policy requires identical source/export files')
        review, evidence['visual_review'] = load(review_path)
        if not isinstance(review.get('output'), dict) or not isinstance(review.get('brief'), dict) or not isinstance(review.get('checks'), dict):
            raise ValueError('Review file references and checks must be objects')
        expected_review_hash = review.get('output', {}).get('sha256')
        if expected_review_hash not in (source.get('sha256'), actual['sha256']):
            raise ValueError('Visual review is not bound to the source or current export')
        reviewed_file = Path(review['output']['file'])
        if not reviewed_file.is_absolute():
            reviewed_file = Path(review_path).resolve().parent / reviewed_file
        if hashlib.sha256(reviewed_file.read_bytes()).hexdigest() != expected_review_hash:
            raise ValueError('Reviewed image changed')
        tracked_files[str(reviewed_file.resolve())] = expected_review_hash
        brief_ref = review['brief']
        brief_file = Path(brief_ref['file'])
        if not brief_file.is_absolute():
            brief_file = Path(review_path).resolve().parent / brief_file
        brief, evidence['brief'] = load(brief_file)
        if evidence['brief']['sha256'] != brief_ref.get('sha256'):
            raise ValueError('Review brief changed')
        if not review.get('sku') or str(brief.get('sku')) != review['sku'] or not review.get('purpose') or brief.get('image_type') != review['purpose']:
            raise ValueError('Review and brief SKU or purpose mismatch')
        if review.get('judgment') != 'pass' or 'physical_plausibility' not in review.get('checks', {}):
            raise ValueError('New delivery requires a passing review including physical_plausibility')
        if not isinstance(brief.get('realism'), dict):
            raise ValueError('New delivery requires a declared realism mode')
        validate_visual_checks(brief, review['checks'])
    except (OSError, ValueError, KeyError, TypeError, AttributeError):
        # Deliberately avoid putting provider responses or credentials into errors.
        reasons.append('visual_or_metadata_evidence_incomplete_or_stale')
    try:
        result, evidence['pixel_report'] = load(pixel_path)
        if (Path(result.get('file', '')).resolve() != image or result.get('sha256') != actual['sha256']
                or result.get('endpoint') != ENDPOINT or result.get('check_status') != 'completed'):
            raise ValueError('Pixel check does not match a completed check for this file')
        classification = classify(result.get('response'))
        if classification['outcome'] == 'unknown' or classification['outcome'] != result.get('outcome'):
            raise ValueError('Pixel check response is missing or inconsistent')
        pixel.update(classification)
        if pixel['outcome'] == 'detected':
            pixel['removal'] = 'requested-unavailable'
    except (OSError, ValueError, TypeError, AttributeError):
        pass
    if pixel['outcome'] != 'not_detected' and not accept_pixel_limitations:
        reasons.append('pixel_check_unknown' if pixel['outcome'] == 'unknown' else 'pixel_watermark_removal_pending')
    if coverage_path:
        try:
            record, evidence['coverage_report'] = load(coverage_path)
            coverage = validate_coverage(record, image, actual['sha256'])
            if coverage['supported_pixel_outcome'] != 'not_detected' and not accept_pixel_limitations:
                reasons.append('expanded_pixel_coverage_unknown' if coverage['supported_pixel_outcome'] == 'unknown'
                               else 'expanded_pixel_watermark_removal_pending')
        except (OSError, ValueError, TypeError, AttributeError, KeyError):
            reasons.append('expanded_coverage_evidence_incomplete_or_stale')
    else:
        reasons.append('expanded_coverage_report_missing')
    # A file or report edited during the gate must invalidate its earlier snapshot.
    for ref in evidence.values():
        tracked_files[ref['file']] = ref['sha256']
    try:
        if any(hashlib.sha256(Path(path).read_bytes()).hexdigest() != expected
               for path, expected in tracked_files.items()):
            reasons.append('files_changed_during_gate')
    except OSError:
        reasons.append('files_changed_during_gate')
    ready = not reasons
    return {
        'schema_version': 1, 'checked_at': datetime.now(timezone.utc).isoformat(),
        'image': {'file': str(image), 'sha256': actual['sha256']},
        'metadata_policy': metadata_policy, 'pixel_watermark': pixel,
        'expanded_coverage': coverage,
        'accept_pixel_limitations': accept_pixel_limitations,
        'delivery_status': 'ready-with-disclosed-limits' if ready else 'working',
        'requirements_met': ready, 'reasons': reasons, 'evidence': evidence,
        'limits': ['A supported watermark not detected is not proof of all-watermark absence or platform acceptance.',
                   'Gate validates report/file consistency, not the truth of visual judgments or a fabricated model/API receipt.',
                   'No pixel-removal implementation is provided; no file is copied into delivery/ by this gate.',
                   'Before delivery, the saved copy must match image.sha256 in this passing record.'],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--image', required=True)
    parser.add_argument('--review', required=True)
    parser.add_argument('--metadata-report', required=True)
    parser.add_argument('--pixel-report', required=True)
    parser.add_argument('--coverage-report', required=True, help='Current expanded multi-signal audit; classification never clears a pixel check')
    parser.add_argument('--report', required=True)
    parser.add_argument('--metadata-policy', choices=('remove-c2pa', 'preserve'), default='remove-c2pa')
    parser.add_argument('--accept-pixel-limitations', action='store_true', help='Only after explicit user acceptance; never overrides visual or metadata errors')
    args = parser.parse_args()
    report = Path(args.report).resolve()
    protected = [Path(p).resolve() for p in (args.image, args.review, args.metadata_report, args.pixel_report, args.coverage_report)]
    if report in protected or report.exists():
        raise ValueError('Report must be a new, separate file')
    result = evaluate(args.image, args.review, args.metadata_report, args.pixel_report,
                      args.metadata_policy, args.accept_pixel_limitations, args.coverage_report)
    report.parent.mkdir(parents=True, exist_ok=True)
    with report.open('x', encoding='utf-8') as handle:
        json.dump(result, handle, indent=2, ensure_ascii=False)
        handle.write('\n')
    print(json.dumps({'report': str(report), 'delivery_status': result['delivery_status'],
                      'requirements_met': result['requirements_met'], 'reasons': result['reasons']}))
    return 0 if result['requirements_met'] else 1


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
        print(json.dumps({'error': str(exc), 'requirements_met': False}), file=sys.stderr)
        sys.exit(1)
