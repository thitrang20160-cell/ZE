# ZE

### Make your product the hero.

**A product visual director for Codex: spatial typography, material tension, purposeful motion, and reusable visual recipes.**

[![Codex Skill](https://img.shields.io/badge/Codex-Skill-111827)](skills/safesell-product-visuals/SKILL.md)
[![Version](https://img.shields.io/badge/version-1.9-0f766e)](skills/safesell-product-visuals/SKILL.md)
[![License: MIT](https://img.shields.io/badge/original_code-MIT-blue)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/thitrang20160-cell/ZE?style=social)](https://github.com/thitrang20160-cell/ZE)

**English · [简体中文](README.zh-CN.md)**

<p align="center">
  <img src="skills/safesell-product-visuals/assets/approved-spatial-type-v3.png" width="520" alt="A cable-led composition with spatial typography, foreground depth, and a localized interaction effect">
</p>

<p align="center"><em>AI-generated style study. This example is style-approved; SKU geometry and numeric claims still need product-specific review.</em></p>

ZE helps Codex turn a product reference into a deliberate commercial image: choose the visual idea, lock the product's identity, give typography a place in the scene, build an appropriate material or action event, then review the actual result.

The workflow travels with the skill. You get the references, recipe cards, visual anchors, failure notes, and helper scripts together — **all 211 original skill files**, with the reusable assets included.

## See the visual language

| Material and depth | Contact and movement | Tactile campaign styling |
| :---: | :---: | :---: |
| ![A rolled mat uses continuous curvature and product-aligned copy](skills/safesell-product-visuals/assets/recipes/sports-grounded-movement/v1/anchor-0.png) | ![A bag campaign combines hand contact, handles, and a spatial headline](skills/safesell-product-visuals/assets/recipes/fashion-soft-editorial/v1/anchor-0.png) | ![A personal-care campaign combines packaging, fabric, and spatial type](skills/safesell-product-visuals/assets/recipes/beauty-sensory-cream/v1/anchor-0.png) |

These are included AI-generated design studies. Recorded review scope belongs to each example; branding, copy, claims, and third-party image rights do not transfer to a new product.

## What ZE brings to an image

| Capability | What the skill directs |
| --- | --- |
| **Spatial typography** | Give headlines and supporting copy foreground, middle, and background relationships. Derive orientation from the product and its action; review exact wording separately. |
| **Material tension** | Express a credible material event through bending, draping, compression, contact, curvature, or depth. Preserve texture scale and avoid invented internal structures. |
| **Purposeful action** | Define who acts, where contact happens, and what visible result follows. Review hands, support, gravity, and the product's working relationship. |
| **Product identity locks** | Anchor shape, part count, connectors, seams, color, accessories, logo, and supported claims to current evidence. Compare actual output against it. |
| **Listing image direction** | Give each image a job. The default seven-image plan is one main image, two features, one material image, two use scenes, and one dimensions image. Adapt to the brief and platform rules. |
| **Recipe reuse** | Retrieve by morphology, action, image purpose, design language, and production route. Reuse useful relationships while replacing SKU facts and copy. |
| **Explicit review** | Keep pass, revise, and unknown visible. A beautiful composition does not erase a wrong part, unsupported number, or unreadable word. |

## Start in Codex

Copy this into Codex:

~~~text
Install https://github.com/thitrang20160-cell/ZE/tree/main/skills/safesell-product-visuals
as a global skill for the current user. Read the repository README first.
Install the entire folder, including assets, references, and scripts.
Back up an existing same-name version, preserve unrelated skills and settings,
and keep automatic task-based invocation enabled.
Verify file hashes against distribution-manifest.json and run recipe_library.py validate.
Report any optional detector dependencies separately.
~~~

Then attach your product reference and ask:

~~~text
Use ZE to make a campaign image for this product.
Keep the observed shape, color, logo, and accessories.
Use a clear near/middle/far composition and typography that follows the product.
Make one product-specific action or material relationship the visual focus.
Check the actual output for identity, copy, contact, and style.
~~~

Try a focused request:

~~~text
Create a seven-image listing set for this product, with a distinct job for each image.
~~~

~~~text
Make a material-tension image using a credible bend, drape, or contact relationship.
Preserve the original texture scale and keep the product recognizable.
~~~

The installed skill identifier is **safesell-product-visuals**, also available explicitly as **$safesell-product-visuals**. Its metadata allows task-based automatic selection; the host decides when a relevant skill is loaded.

Prefer a manual download? [Download the complete repository ZIP](https://github.com/thitrang20160-cell/ZE/archive/refs/heads/main.zip), then install the entire skills/safesell-product-visuals folder. [Installation and optional checks](docs/INSTALL.md).

## What is inside

- **11 original style references** and a user-approved spatial-typography anchor.
- **15 versioned recipe cards**, with matching assets, scope, evidence, and failure notes.
- **12 visual-family records** spanning home, kitchen, cleaning, electronics, pets, garden, sports, tools, beauty, fashion, food, and toys.
- Guidance for main images, features, material studies, use scenes, dimensions, and campaigns.
- Helpers for recipe retrieval, evidence integrity, PNG provenance handling, supported-signal checks, and delivery-state validation.

~~~text
skills/safesell-product-visuals/
├── SKILL.md          # Direction and task routing
├── agents/           # Display metadata and invocation policy
├── references/       # Workflows and versioned recipe cards
├── assets/           # Style samples and recipe evidence
└── scripts/          # Retrieval and verification helpers
~~~

From the installed skill directory:

~~~bash
python -X utf8 scripts/recipe_library.py validate
python -X utf8 scripts/recipe_library.py find --morphology flexible-linear --purpose material --route ai-reference-guided --action bend --style technical-studio
~~~

The validator checks recipe, asset, and evidence integrity. It does not independently judge an image or prove that a historical review was correct.

## Production routes and dependencies

ZE uses the built-in image generation actually available in the target Codex environment. It is a skill and reference library, not a separate generation service.

Reference-guided generation produces candidates that need identity review. Pixel-exact preservation calls for a fixed real product layer or verified render-and-composite workflow. Internal parts, dimensions, and unseen angles need source material. Main-image requirements are checked for the current platform and category.

Core recipe helpers use Python's standard library. Optional watermark checks need supported models, dependencies, or cloud credentials. Missing coverage stays unknown; metadata handling is distinct from pixel-watermark detection. [Dependency details](docs/INSTALL.md).

No universal first-pass guarantee, measured conversion lift, or universal watermark-removal claim is made.

## Help the library grow

Contribute a reusable recipe, a documented failure and repair, or a clearer workflow. Include the product basis, generated result, review scope, and evidence needed to reproduce it. [Contribution guide](CONTRIBUTING.md).

If ZE helps your work, **give it a Star** so other makers can find it. Share a result or a concrete issue to help shape the next recipes.

## License

Original instructions, recipe structures, and original code use [MIT](LICENSE). Included third-party code retains its notices; reference images, brands, and trademarks retain their respective rights. See [NOTICE.md](NOTICE.md).
