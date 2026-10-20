# Zen Theme Store 提交材料包

本文件由 `tools/build_store_package.py` 生成，是给 `zen-browser/theme-store` 的 `Submit a theme` issue 准备的**可直接复制**材料，不会自动提交 issue。修改源文件后重新运行脚本即可更新。

对应版本：`0.0.1`；来源：<https://github.com/LxyMp/zen-find>；生成日期：2026-10-20。

提交入口：<https://github.com/zen-browser/theme-store/issues/new?assignees=&labels=new-theme&projects=&template=create-theme.yml&title=%5Bcreate-theme%5D%3A+>

## 1. 表单字段

Issue 标题：

```text
[create-theme]: Zen Find
```

| 字段 | 应填内容 |
| --- | --- |
| Name | `Zen Find` |
| Description | `Flat, customizable redesign of Zen's native find bar with position and visibility controls.` |
| Homepage | <https://github.com/LxyMp/zen-find> |
| Image | <https://raw.githubusercontent.com/LxyMp/zen-find/main/docs/images/store-preview.png> |
| Type | **不要勾选 JSON Color Theme**（这是 CSS Mod，不是 JSON 颜色主题） |
| Author | `LxyMp` |
| Version | `0.0.1` |

说明：

- `Name` 8 个字符，`Description` 91 个字符，均未超过模板的 25/100 字符上限。
- Theme ID 不需要填；商店机器人会为商店目录生成/分配 ID。本地 `7d7d01bd-1788-4e0a-a0c9-4aa463a9d9fb` 只用于开发安装器。
- Image 必须是 PNG。当前使用 `docs/images/store-preview.png` 的 raw GitHub 地址；商店机器人会把它复制到主题目录。
- 如果表单因为 `Type` 是必填项而不允许留空：不要勾选成颜色主题，在 issue 里补充说明“CSS theme, not a JSON color theme”，或先联系维护者确认模板。

## 2. Theme Styles（粘贴到 Theme Styles 输入框）

```css
/* Zen 1.22b baseline; fully re-verified on Zen 1.23.3b (Gecko 158.0). */
findbar {
  --zen-find-x: -50%;
  --zen-find-y: 0%;
  --zen-find-count-width: min(180px, 42cqw);
  --zen-find-count-right: 114px;
  position: absolute !important;
  /* Native grid-area: findbar is a collapsed bottom row when out of flow. */
  grid-area: browserstack !important;
  inset: 40px auto auto 50% !important;
  transform: translate(var(--zen-find-x), var(--zen-find-y)) scale(1) !important;
  z-index: 10 !important;
  box-sizing: border-box;
  width: min(560px, calc(100% - 24px));
  min-width: 0 !important;
  max-width: calc(100% - 24px);
  max-height: calc(100% - 24px);
  overflow: visible;
  margin: 0 !important;
  padding: 10px !important;
  font-size: 12px;
  gap: 6px;
  align-items: flex-start;
  border: 1px solid var(--zen-colors-border, light-dark(rgb(0 0 0 / 18%), rgb(255 255 255 / 16%))) !important;
  border-radius: var(--zen-border-radius, 7px) !important;
  color: var(--toolbar-field-text-color, CanvasText) !important;
  background: rgb(from var(--mod-zen-find-background-color, var(--zen-colors-tertiary, Canvas)) r g b / 1) !important;
  backdrop-filter: none !important;
  box-shadow: 0 1px 3px rgb(0 0 0 / 18%),
    0 8px 24px light-dark(rgb(0 0 0 / 14%), rgb(0 0 0 / 32%));
  opacity: 1 !important;
  visibility: visible !important;
  will-change: transform, opacity;
  transition:
    transform 180ms cubic-bezier(0.2, 0.8, 0.2, 1),
    opacity 180ms cubic-bezier(0.2, 0.8, 0.2, 1),
    visibility 0s linear 0s !important;
}

findbar[hidden] {
  display: flex !important;
  visibility: hidden !important;
  opacity: 0 !important;
  pointer-events: none !important;
  transform:
    translate(var(--zen-find-x), calc(var(--zen-find-y) - 40px))
    scale(0.9) !important;
  transition:
    transform 140ms cubic-bezier(0.4, 0, 1, 1),
    opacity 140ms cubic-bezier(0.4, 0, 1, 1),
    visibility 0s linear 140ms !important;
}

/* Keep the native content painted while the outer box fades out. */
findbar[hidden] > .findbar-container,
findbar[hidden] > .findbar-closebutton {
  opacity: 1 !important;
}

@media (prefers-reduced-motion: reduce) {
  findbar,
  findbar[hidden] {
    transition-duration: 0s !important;
    transition-delay: 0s !important;
  }
}

findbar .findbar-container {
  display: grid;
  flex: 1 1 0%;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  align-items: center;
  gap: 6px 12px;
  min-width: 0;
  height: auto !important;
  margin: 0 !important;
  padding: 0 !important;
  overflow: visible !important;
}

findbar [anonid="findbar-textbox-wrapper"] {
  grid-column: 1 / -1;
  display: flex;
  margin-right: 32px;
  gap: 4px;
  flex: 1 1 240px;
  min-width: 0;
  max-width: 100%;
}

findbar .findbar-textbox {
  box-sizing: border-box;
  height: 32px;
  padding: 0 9px !important;
  font-size: 13px;
  flex: 1 1 0%;
  width: 0;
  min-width: 0 !important;
  border-radius: var(--zen-border-radius, 7px);
}

/* Reserve input space only while the native count is visible. */
findbar:has(.found-matches:not([hidden])) .findbar-textbox {
  padding-right: calc(var(--zen-find-count-width) + 18px) !important;
}

findbar .found-matches:not([hidden]) {
  position: absolute;
  top: 10px;
  right: var(--zen-find-count-right);
  width: var(--zen-find-count-width);
  height: 32px;
  line-height: 32px;
  font-size: 11px;
  font-variant-numeric: tabular-nums;
  text-align: right;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  opacity: 0.7;
  pointer-events: none;
}

findbar .findbar-find-status:empty,
findbar .find-status-icon:not([status]) {
  display: none;
}

/* Keep native notfound/flash colors and keyboard focus treatment. */
findbar .findbar-textbox:not([status="notfound"], [flash="true"], :focus) {
  background-color: var(--zen-colors-input-bg, Field) !important;
  color: var(--toolbar-field-text-color, FieldText) !important;
  border-color: var(--zen-input-border-color, ThreeDShadow);
}

findbar :is(.findbar-find-previous, .findbar-find-next, .findbar-closebutton) {
  box-sizing: border-box;
  width: 28px;
  height: 32px;
  min-width: 28px;
  margin: 0 !important;
  padding: 6px !important;
  flex: 0 0 auto;
  border-radius: var(--zen-border-radius, 7px);
}

findbar .findbar-closebutton {
  position: absolute;
  right: 10px;
  top: 10px;
}

findbar checkbox {
  box-sizing: border-box;
  justify-self: stretch;
  min-height: 26px;
  margin: 0 !important;
  padding: 4px 5px !important;
  font-size: 11px;
  border-radius: 4px;
}

findbar checkbox:hover {
  background: var(--toolbarbutton-background-color-hover,
    var(--zen-colors-hover-bg, rgb(127 127 127 / 12%)));
}

findbar :is(.findbar-label, .find-status-icon) {
  grid-column: 1 / -1;
  margin: 0 !important;
}

findbar {
  container-type: inline-size;
}

@container (max-width: 420px) {
  findbar .findbar-container {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  /* Keep the count off the input row on narrow panels. */
  findbar:has(.found-matches:not([hidden])) .found-matches {
    position: static;
    grid-column: 1 / -1;
    grid-row: 2;
    width: auto;
    height: auto;
    line-height: 1.4;
    text-align: left;
  }

  findbar:has(.found-matches:not([hidden])) .findbar-textbox {
    padding-right: 9px !important;
  }

  findbar:has(.found-matches:not([hidden])) checkbox:nth-of-type(1) {
    grid-column: 1;
    grid-row: 3;
  }

  findbar:has(.found-matches:not([hidden])) checkbox:nth-of-type(2) {
    grid-column: 2;
    grid-row: 3;
  }

  findbar:has(.found-matches:not([hidden])) checkbox:nth-of-type(3) {
    grid-column: 1;
    grid-row: 4;
  }

  findbar:has(.found-matches:not([hidden])) checkbox:nth-of-type(4) {
    grid-column: 2;
    grid-row: 4;
  }
}

findbar :is(.findbar-find-status, .found-matches, checkbox) {
  min-width: 0;
  max-width: 100%;
  white-space: normal;
  overflow-wrap: anywhere;
}

@media -moz-pref("uc.findbar.horizontal-position", "left") {
  findbar {
    left: 12px !important;
    --zen-find-x: 0%;
  }
}

@media -moz-pref("uc.findbar.horizontal-position", "right") {
  findbar {
    left: auto !important;
    right: 12px !important;
    --zen-find-x: 0%;
  }
}

@media -moz-pref("uc.findbar.vertical-position", "center") {
  findbar {
    top: 50% !important;
    --zen-find-y: -50%;
  }
}

@media -moz-pref("uc.findbar.vertical-position", "bottom") {
  findbar {
    top: auto !important;
    bottom: 12px !important;
  }
}

/* Explicit opt-in: keep close, input and result status available. */
@media -moz-pref("uc.findbar.hide-buttons") {
  findbar {
    --zen-find-count-right: 50px;
  }
  findbar :is(.findbar-find-previous, .findbar-find-next,
    .findbar-highlight, .findbar-case-sensitive,
    .findbar-match-diacritics, .findbar-entire-word) {
    display: none !important;
  }
}

```

## 3. Readme（粘贴到 Readme 输入框）

下面是为商店展示准备的 README，不是仓库根目录里面向开发者的 `README.md`。

````markdown
# Zen Find

A flat, theme-aware redesign of Zen Browser's native find bar.

![Zen Find](https://raw.githubusercontent.com/LxyMp/zen-find/main/docs/images/store-preview.png)

## Features

- Nine positions: left, center or right, combined with top, center or bottom. The default top position sits 40px below the content top.
- Opaque, theme-aware background with an optional custom CSS color.
- Entry and exit animation (180ms in, 140ms out) using only transform and opacity; disabled when reduced motion is requested.
- Optional compact mode that hides previous/next and the four find options, keeping close, input and match count.
- Native Firefox controls, keyboard behavior and accessibility are preserved.
- Responsive layout: on narrow panels the match count moves below the input and the options use two columns. The count reserves up to 180px on wider panels.

## Usage

Install **Zen Find** from Zen Mods, then press `Cmd+F` on macOS or `Ctrl+F` on Windows/Linux.

Open **Settings → Zen Mods → Zen Find** to change the position or enable compact mode.

## Settings

- **Horizontal position**: left, center, right.
- **Vertical position**: top, center, bottom. Top is 40px below the content top; left, right and bottom use 12px margins.
- **Background color**: leave empty to follow the Zen theme, or enter an opaque CSS color. `transparent` is rendered as black; invalid values make the background invalid.
- **Hide navigation and find options**: keeps close, input and match count.

## Compatibility

- Current target: Zen 1.23.3b (Gecko 158.0).
- Historical baseline: Zen 1.22b (Gecko 155.0.1).
- Verified on Zen 1.23.3b: input, Enter/Shift+Enter, Esc, no-match state, all native options, nine positions, narrow panels, sidebar, compact mode, split view, light/dark themes, custom background and disabling the mod.
- The final top 40px and 180/140ms animation were confirmed in the author's daily profile. The 180px count width is implemented; the Chinese long-count display has not been re-screenshotted. The structured layout measurements were taken before the final values were applied.
- The 1.22b build was not re-tested in this round.

## Notes

- This is a CSS-only mod. It does not change find behavior, shortcuts, match rules or the values of native find options.
- The background is intentionally opaque; page content does not show through.
- The exit animation is designed for the default top position. Other vertical positions move up by 40px on exit rather than returning to the absolute content top.
- Source and issue tracker: <https://github.com/LxyMp/zen-find>

## License

Theme store submissions are licensed under CC BY-NC-SA 4.0.

````

## 4. Preferences（粘贴到 Preferences 输入框）

```json
[
  {
    "property": "uc.findbar.horizontal-position",
    "label": "查找栏横向位置",
    "type": "dropdown",
    "defaultValue": "center",
    "options": [
      { "label": "左", "value": "left" },
      { "label": "中", "value": "center" },
      { "label": "右", "value": "right" }
    ]
  },
  {
    "property": "uc.findbar.vertical-position",
    "label": "查找栏垂直位置",
    "type": "dropdown",
    "defaultValue": "top",
    "options": [
      { "label": "上", "value": "top" },
      { "label": "中", "value": "center" },
      { "label": "下", "value": "bottom" }
    ]
  },
  {
    "property": "mod.zen-find.background-color",
    "label": "背景颜色（留空跟随 Zen；请用不透明颜色，勿用 transparent）",
    "type": "string",
    "defaultValue": ""
  },
  {
    "property": "uc.findbar.hide-buttons",
    "label": "隐藏导航及查找选项按钮（保留关闭、输入框与计数）",
    "type": "checkbox",
    "defaultValue": false
  }
]

```

说明：商店里已有主题使用同样的数组结构；模板里的对象示例只是占位示意，以本文件为准。

## 5. 提交前检查

- [x] `theme.json` 的 name/description/author/homepage 与上表一致。
- [x] CSS 无 `@-moz-document` 包裹、无本地绝对路径、无诊断脚本内容。
- [x] `preferences.json` 是合法 JSON；CSS 大括号配对；纯 ASCII。
- [x] 当前版本 PNG 预览图已准备（1200x630，取自已验证的 1.23.3b 临时 profile，显示实际 `1 of 5 matches` 计数）。
- [x] 当前 Zen 1.23.3b 的完整交互验收：实际输入、Enter/Shift+Enter、Esc、无匹配、计数更新、所有原生选项。
- [x] 最终默认顶部 40px、入场/退场 180/140ms 已由用户在日常配置确认；计数已加宽到 180px，中文长计数尚未重新截图确认。
- [x] 深色/浅色主题、真实窗口宽度、侧栏、紧凑模式、分屏、禁用 Mod 恢复；320px 场景由 macOS 最小窗口钳制，实际测到更窄的 238px/258px。
- [ ] 最终参数（top 40/count 180/animation 180-140ms）的完整九位置与窄宽结构化复测；中文长计数截图确认。
- [ ] 确认接受商店的 CC BY-NC-SA 4.0 授权（只有作者本人能确认）。

> 1.23.3b 临时 profile 已完成交互、九位置、窄面板、侧栏、紧凑、分屏、深浅主题、自定义背景、禁用恢复验收；1.22b 本轮未回归（本机无该版本）。Cmd/Ctrl+F 实际键盘路径和深色系统自动主题未单独模拟。最终位置和动画已日常确认；计数已加宽，中文长计数尚未重新截图；最终参数的结构化复测仍待完成；完整结构化测量基于参数变更前基线。预览图是聚焦图，不是完整桌面截图。

## 6. 提交之后

- 商店机器人会创建主题目录和 PR；不要直接改 `zen-browser/theme-store` 仓库。
- 上架后用户从 Zen Mods 一键安装；更新时按商店 README 提交新的 PR，并提升 `theme.json` 的 version。
- 首次上架后可把本地 `theme.json` 的 id 对齐商店分配的 id，便于后续发布；本地开发安装器仍可用当前 id。
- 如果维护者要求调整描述/标签/预览图，直接在 issue 或后续 PR 中改，不要重复开新 issue。

## 7. 相关文件

- 源码：<https://github.com/LxyMp/zen-find>
- CSS：<https://github.com/LxyMp/zen-find/blob/main/chrome.css>
- 设置：<https://github.com/LxyMp/zen-find/blob/main/preferences.json>
- 商店 README：<https://github.com/LxyMp/zen-find/blob/main/docs/store-readme.md>
- 预览图：<https://github.com/LxyMp/zen-find/blob/main/docs/images/store-preview.png>
- 验证记录：<https://github.com/LxyMp/zen-find/blob/main/docs/VERIFICATION.md>
- 提交清单：<https://github.com/LxyMp/zen-find/blob/main/docs/THEME-STORE-SUBMISSION.md>
