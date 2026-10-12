# Contributing to ZE

Useful contributions include a reusable product-specific recipe, a documented visual failure and repair, a clearer workflow, or a reproducible bug fix.

For a recipe contribution, include:

1. The product source basis and the exact scope you checked.
2. The generated example, brief, and image purpose; disclose the actual tool used.
3. Review results and remaining unknowns, with file hashes and reproducible evidence.
4. Transferable relationships, facts that must not transfer, and observed failure notes.
5. Rights information for any images or code you contribute.

Keep style seeds, local reviews, and cross-product validation distinct. Preserve SKU identity and exact-copy checks. Do not add credentials, private customer data, fabricated receipts, or unsupported performance claims.

Run python -X utf8 scripts/recipe_library.py validate from the skill directory after a library update. Use the existing catalog tools and refresh the distribution manifest when distributed content changes. The validator checks records and hashes; it does not replace looking at actual images.

欢迎贡献配方、失败修复和工作流改进。请注明真实工具、素材权利、已验证范围与剩余未知项，让其他人能够复现；一张好看的结果不自动成为整个类目通用结论。
