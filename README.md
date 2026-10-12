# ZE — 跨境电商超强表现力生图 Skill

你的「塞星商品视觉导演 / safesell-product-visuals」v1.9 完整分发版。

包含原技能的全部 211 个文件，约 95 MiB：11 张原始风格样本、认可的空间文字锚点、15 张配方卡、12 个视觉家族记录、制作与审核规范、Listing 7 张分工、材质张力、动作场景、空间文字，以及配方检索、来源声明处理、检测和交付验证脚本。配方状态与已知失败项原样保留，不把历史样本视为新商品事实。

## 安装到其他 Codex

仓库：https://github.com/thitrang20160-cell/ZE（公开开源，无需 GitHub 登录即可下载）。

将 `skills/safesell-product-visuals` 整个目录安装到当前用户的全局技能目录。可以让目标 Codex 使用其内置 skill-installer，仓库路径选 `skills/safesell-product-visuals`；或者拉取仓库后复制整个目录。先检查目标环境的技能发现目录及同名技能，已有同名版本先备份，只保留一个生效版本，其他技能与设置不变。不要只复制 SKILL.md。

复制给另一台 Codex：

```text
请拉取 https://github.com/thitrang20160-cell/ZE，先读 README.md，将 skills/safesell-product-visuals 整套安装到当前用户的全局技能目录，供多个项目使用。使用当前环境的实际路径，备份同名旧版，保留其他技能与配置，避免重复生效。保持按任务自动识别调用。安装后核对 distribution-manifest.json 的文件哈希，运行配方库 validate 并检查脚本可用性，告诉我是否需要重启 Codex。可选检测功能需要的模型或账号密钥单独说明，缺失不能报告已通过。出现问题主动调查、修复并复测，不把未完成报告为成功。
```

## 跨机路径与依赖

- 生图仍使用目标 Codex 实际提供的内置 image_gen。Skill 是制作规范、经验库与辅助脚本，本身不提供生图服务凭证。
- 脚本路径相对技能根目录。文档及历史审核里的 `C:/Users/TY/...`、`D:/CODEX/...`、旧 SKU 和旧任务输出目录是原始案例记录，不是另一台电脑必须创建的目录。可复用样本和配方证据已随本包复制，并由配方验证器检查哈希；不把外部历史路径当当前任务输入。
- 普通配方检索与 PNG 声明处理脚本使用 Python 标准库，无需额外账号。
- 可选 TrustMark 检测另需 numpy、Pillow、onnxruntime，以及原规范中的三个官方 ONNX 模型和正负对照清单；这些外部运行资源原本就不包含在 Skill 内。本包保留全部检测实现和所需模型 SHA-256，见 `references/detector-coverage.md`。
- 云端检测只在用户选择且有对应账号、密钥、权限时使用。密钥通过环境变量提供，不写进技能。未执行、不可用或缺资料按原规范记录 unknown；不宣称通用水印去除或绕过平台检测。

## 核验

在安装后的技能目录运行：

```powershell
python -X utf8 scripts/recipe_library.py validate
python -X utf8 scripts/delivery_gate.py --help
python -X utf8 scripts/detect_image_signals.py --help
```

分发时只将原 `AI生图SKILL.md` 改为标准入口 `SKILL.md`，文件内容完全保留；`agents/openai.yaml` 增加显式允许自动调用的配置，原版保存在 `original-metadata/openai.yaml`。其他原文件字节不变。完整清单和原始哈希见 `distribution-manifest.json`。声明自动调用可用，不保证每个无关任务都会加载此技能。

原样本中的第三方品牌与图片仅作既有参考资产；未为其授予新商用许可。Adobe BCH/DataLayer 辅助实现的原 MIT 许可证保留在 `scripts/_trustmark_ecc/LICENSE`。本分发不改写技能原有的审核限制，不自动接入或发布业务系统。


## 开源许可

原创技能说明、配方结构和原创辅助代码采用 MIT 许可证，见仓库根目录 `LICENSE`。
第三方代码、参考图片、品牌及商标的权利与适用范围见 `NOTICE.md`；公开下载不为参考素材授予额外商用权利。
