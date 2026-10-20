# Zen Theme Store 提交清单

这是提交给 Zen Theme Store 创建主题 issue 前的检查表，不是商店 API 请求，也不会自动提交 issue。可直接粘贴的完整材料见 [`STORE-SUBMISSION-PACKAGE.md`](STORE-SUBMISSION-PACKAGE.md)。

## 当前元数据

- Name: `Zen Find`
- Description: `Flat, customizable redesign of Zen's native find bar with position and visibility controls.`
- Homepage: <https://github.com/LxyMp/zen-find>
- Version: `0.0.1`
- Author: `LxyMp`
- Theme ID: `7d7d01bd-1788-4e0a-a0c9-4aa463a9d9fb`
- Style: `chrome.css`
- Preferences: `preferences.json`
- Readme（本地开发）: `README.md`
- Readme（商店展示）: `docs/store-readme.md`

## 提交前必须完成

- [x] 在当前 Zen 1.23.3b 上完成打开、输入、Enter、Shift+Enter、Esc、无匹配、计数更新和所有原生选项测试（2026-10-20，临时 profile；1.22b 历史记录见 `VERIFICATION.md`）。
- [x] 检查浅色、深色、窄窗口、侧栏、紧凑模式、分屏、禁用恢复和九种位置组合。
- [x] 确认纯色背景不透出网页，边缘阴影清晰，原生控件可读；自定义背景、`transparent` 和非法颜色也做了检查。
- [x] 已准备当前版本的 PNG 预览图：`docs/images/store-preview.png`（1200x630，实际 `1 of 5 matches` 计数）。
- [x] 确认 `theme.json` 的 author/description 与上表一致。
- [ ] 若直接使用仓库 `theme.json` 作为商店元数据，将 `style`、`preferences`、`readme` 替换为真实 HTTPS URL；走 issue 表单时使用材料包中的 raw URL，主题商店机器人负责目录。
- [x] 检查 CSS、JSON 和商店 README 中没有本地绝对路径、临时诊断标记或开发环境信息。
- [ ] 确认接受主题商店的 CC BY-NC-SA 4.0 授权条款。

## 已完成，但仍有边界

- 1.22b 本轮没有可执行环境，未做回归；1.23.3b 是当前验收目标。
- Cmd/Ctrl+F 快捷键没有用真实键盘事件单独模拟；已通过原生 findbar 打开、输入、Enter/Shift+Enter、Esc 路径验证，CSS 不改变快捷键处理。
- 深色系统的“自动”主题没有单独模拟；显式深色和显式浅色已通过。
- macOS 最小窗口宽度为 500，请求 320 会被钳制；实际已测到 238px/258px 的 findbar 宽度，覆盖 320px 场景。

## 提交入口

在 <https://github.com/zen-browser/theme-store/issues/new?assignees=&labels=new-theme&projects=&template=create-theme.yml&title=%5Bcreate-theme%5D%3A+> 打开创建主题表单，填入上面的元数据，并粘贴 `chrome.css`、`docs/store-readme.md` 和 `preferences.json` 的内容。主题商店机器人会负责创建主题目录和后续 PR。

当前不提交 issue：1.23.3b 完整验收已完成，等待作者确认 CC BY-NC-SA 4.0 后提交。预览图和材料包均已按当前版本更新。
