#!/usr/bin/env python3
"""Generate the copy-paste Zen Theme Store submission package."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "docs" / "STORE-SUBMISSION-PACKAGE.md"

REPO = "https://github.com/LxyMp/zen-find"
ISSUE_URL = (
    "https://github.com/zen-browser/theme-store/issues/new"
    "?assignees=&labels=new-theme&projects=&template=create-theme.yml"
    "&title=%5Bcreate-theme%5D%3A+"
)
IMAGE_URL = "https://raw.githubusercontent.com/LxyMp/zen-find/main/docs/images/store-preview.png"


def main() -> None:
    meta = json.loads((ROOT / "theme.json").read_text(encoding="utf-8"))
    css = (ROOT / "chrome.css").read_text(encoding="utf-8").rstrip() + "\n"
    readme = (ROOT / "docs" / "store-readme.md").read_text(encoding="utf-8").rstrip() + "\n"
    prefs = (ROOT / "preferences.json").read_text(encoding="utf-8").rstrip() + "\n"

    parts = [
        "# Zen Theme Store 提交材料包",
        "",
        "本文件由 `tools/build_store_package.py` 生成，是给 "
        "`zen-browser/theme-store` 的 `Submit a theme` issue 准备的"
        "**可直接复制**材料，不会自动提交 issue。修改源文件后重新运行脚本即可更新。",
        "",
        f"对应版本：`{meta['version']}`；来源：<{REPO}>；生成日期：{date.today().isoformat()}。",
        "",
        f"提交入口：<{ISSUE_URL}>",
        "",
        "## 1. 表单字段",
        "",
        "Issue 标题：",
        "",
        "```text",
        f"[create-theme]: {meta['name']}",
        "```",
        "",
        "| 字段 | 应填内容 |",
        "| --- | --- |",
        f"| Name | `{meta['name']}` |",
        f"| Description | `{meta['description']}` |",
        f"| Homepage | <{meta['homepage']}> |",
        f"| Image | <{IMAGE_URL}> |",
        "| Type | **不要勾选 JSON Color Theme**（这是 CSS Mod，不是 JSON 颜色主题） |",
        f"| Author | `{meta['author']}` |",
        f"| Version | `{meta['version']}` |",
        "",
        "说明：",
        "",
        f"- `Name` {len(meta['name'])} 个字符，`Description` "
        f"{len(meta['description'])} 个字符，均未超过模板的 25/100 字符上限。",
        f"- Theme ID 不需要填；商店机器人会为商店目录生成/分配 ID。"
        f"本地 `{meta['id']}` 只用于开发安装器。",
        "- Image 必须是 PNG。当前使用 `docs/images/store-preview.png` 的 raw GitHub 地址；"
        "商店机器人会把它复制到主题目录。",
        "- 如果表单因为 `Type` 是必填项而不允许留空：不要勾选成颜色主题，"
        "在 issue 里补充说明“CSS theme, not a JSON color theme”，或先联系维护者确认模板。",
        "",
        "## 2. Theme Styles（粘贴到 Theme Styles 输入框）",
        "",
        "```css",
        css,
        "```",
        "",
        "## 3. Readme（粘贴到 Readme 输入框）",
        "",
        "下面是为商店展示准备的 README，不是仓库根目录里面向开发者的 `README.md`。",
        "",
        "````markdown",
        readme,
        "````",
        "",
        "## 4. Preferences（粘贴到 Preferences 输入框）",
        "",
        "```json",
        prefs,
        "```",
        "",
        "说明：商店里已有主题使用同样的数组结构；模板里的对象示例只是占位示意，"
        "以本文件为准。",
        "",
        "## 5. 提交前检查",
        "",
        "- [x] `theme.json` 的 name/description/author/homepage 与上表一致。",
        "- [x] CSS 无 `@-moz-document` 包裹、无本地绝对路径、无诊断脚本内容。",
        "- [x] `preferences.json` 是合法 JSON；CSS 大括号配对；纯 ASCII。",
        "- [x] 当前版本 PNG 预览图已准备（1200x630，取自已验证的 1.23.3b 临时 profile，显示实际 `1 of 5 matches` 计数）。",
        "- [x] 当前 Zen 1.23.3b 的完整交互验收：实际输入、Enter/Shift+Enter、Esc、"
        "无匹配、计数更新、所有原生选项。",
        "- [x] 最终默认顶部 40px、入场/退场 180/140ms 已由用户在日常配置确认；计数已加宽到 180px，中文长计数尚未重新截图确认。",
        "- [x] 深色/浅色主题、真实窗口宽度、侧栏、紧凑模式、分屏、"
        "禁用 Mod 恢复；320px 场景由 macOS 最小窗口钳制，实际测到更窄的 238px/258px。",
        "- [ ] 最终参数（top 40/count 180/animation 180-140ms）的完整九位置与窄宽结构化复测；中文长计数截图确认。",
        "- [ ] 确认接受商店的 CC BY-NC-SA 4.0 授权（只有作者本人能确认）。",
        "",
        "> 1.23.3b 临时 profile 已完成交互、九位置、窄面板、侧栏、紧凑、分屏、"
        "深浅主题、自定义背景、禁用恢复验收；1.22b 本轮未回归（本机无该版本）。"
        "Cmd/Ctrl+F 实际键盘路径和深色系统自动主题未单独模拟。"
        "最终位置和动画已日常确认；计数已加宽，中文长计数尚未重新截图；"
        "最终参数的结构化复测仍待完成；"
        "完整结构化测量基于参数变更前基线。"
        "预览图是聚焦图，不是完整桌面截图。",
        "",
        "## 6. 提交之后",
        "",
        "- 商店机器人会创建主题目录和 PR；不要直接改 `zen-browser/theme-store` 仓库。",
        "- 上架后用户从 Zen Mods 一键安装；更新时按商店 README 提交新的 PR，"
        "并提升 `theme.json` 的 version。",
        "- 首次上架后可把本地 `theme.json` 的 id 对齐商店分配的 id，便于后续发布；"
        "本地开发安装器仍可用当前 id。",
        "- 如果维护者要求调整描述/标签/预览图，直接在 issue 或后续 PR 中改，"
        "不要重复开新 issue。",
        "",
        "## 7. 相关文件",
        "",
        f"- 源码：<{REPO}>",
        f"- CSS：<{REPO}/blob/main/chrome.css>",
        f"- 设置：<{REPO}/blob/main/preferences.json>",
        f"- 商店 README：<{REPO}/blob/main/docs/store-readme.md>",
        f"- 预览图：<{REPO}/blob/main/docs/images/store-preview.png>",
        f"- 验证记录：<{REPO}/blob/main/docs/VERIFICATION.md>",
        f"- 提交清单：<{REPO}/blob/main/docs/THEME-STORE-SUBMISSION.md>",
        "",
    ]
    PACKAGE.write_text("\n".join(parts), encoding="utf-8")
    print(f"wrote {PACKAGE} ({PACKAGE.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
