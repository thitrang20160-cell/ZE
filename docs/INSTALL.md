# Installation and optional checks / 安装与可选检测

Repository: https://github.com/thitrang20160-cell/ZE — public; no GitHub sign-in is needed to download.

## Install the complete skill

Ask Codex's skill-installer to install the repository path skills/safesell-product-visuals, or download the repository ZIP and copy that entire directory into the global skill directory supported by the target Codex environment.

Back up an existing same-name version. Keep one active copy, and preserve unrelated skills and settings. Include SKILL.md, references, assets, and scripts. The metadata allows task-based automatic invocation; the host controls discovery and selection.

安装时使用当前电脑的实际路径。全局发现目录以目标 Codex 环境支持的位置为准；已有同名版本先备份，避免多份同时生效。目标环境提示需要重新加载时，按其要求操作。

## Verify

distribution-manifest.json lists the distributed file hashes and the 211 original source files. Packaging normalized AI生图SKILL.md to SKILL.md and explicitly allowed implicit invocation. Original UI metadata is retained in original-metadata/openai.yaml; other original content is unchanged.

From the installed skill directory:

~~~powershell
python -X utf8 scripts/recipe_library.py validate
python -X utf8 scripts/delivery_gate.py --help
python -X utf8 scripts/detect_image_signals.py --help
~~~

The recipe validator checks catalog and linked evidence hashes. CLI help checks that entrypoints can load; it is not a live generation or cloud-detector test.

## Image generation and historical paths

The skill uses the built-in image_gen actually available in the target Codex. It does not supply a separate image-generation account or service credential.

Resolve script, reference, and asset paths relative to the installed skill root. C:/Users/TY/..., D:/CODEX/..., old output folders, and historical SKU identifiers in archived examples are source records, not installation requirements or current-task inputs. Reusable style and recipe evidence is included locally and checked by the recipe validator.

## Optional detector dependencies

Ordinary recipe retrieval and PNG provenance helpers use Python's standard library. TrustMark checks additionally need numpy, Pillow, onnxruntime, the original three official ONNX models, and a positive/negative control manifest. These external resources were not included in the original skill.

The model SHA-256 values and supported profiles remain in scripts/trustmark_local.py and references/detector-coverage.md under the installed skill directory. Validate actual models and controls before reporting a completed check.

Cloud checks run only when selected and authorized, with working credentials and provider access. Supply keys through the documented environment variables; never commit them. Missing checks remain unknown. Metadata handling, pixel-watermark checks, and AI classification are separate results; none proves universal absence or removal.

可选检测的模型、密钥、权限不足时单独报告，不把未执行写成通过；不把普通文件校验误报为完成了生图或云端审核。

## Rights

Original code and instructions use MIT. Third-party code and reference assets retain the rights described in [NOTICE.md](../NOTICE.md).
