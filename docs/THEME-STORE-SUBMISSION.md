# Zen Theme Store 提交清单

这是提交给 Zen Theme Store 创建主题 issue 前的检查表，不是商店 API 请求，也不会自动提交 issue。

## 当前元数据

- Name: `Zen Find`
- Description: `Flat, customizable redesign of Zen's native find bar with position and visibility controls.`
- Homepage: <https://github.com/LxyMp/zen-find>
- Version: `0.0.1`
- Author: `LxyMp`
- Theme ID: `7d7d01bd-1788-4e0a-a0c9-4aa463a9d9fb`
- Style: `chrome.css`
- Preferences: `preferences.json`
- Readme: `README.md`

## 提交前必须完成

- [ ] 使用当前 Zen 1.23.3b 完成打开、输入、Enter、Shift+Enter、Esc、无匹配和所有原生选项测试（1.22b 记录见 `VERIFICATION.md`）。
- [ ] 检查浅色、深色、窄窗口、紧凑模式和九种位置组合。
- [ ] 确认纯色背景不透出网页，边缘阴影清晰，原生控件可读。
- [ ] 准备一张展示最终版本的 PNG 预览图。不要使用早期毛玻璃实验截图。
- [ ] 确认 `theme.json` 的 author/description 与上表一致。
- [ ] 若直接使用仓库 `theme.json` 作为商店元数据，将 `style`、`preferences`、`readme` 替换为真实 HTTPS URL。
- [ ] 检查 CSS、JSON 和 README 中没有本地绝对路径、临时诊断标记或开发环境信息。
- [ ] 确认接受主题商店的 CC BY-NC-SA 4.0 授权条款。

## 提交入口

在 <https://github.com/zen-browser/theme-store/issues/new?assignees=&labels=new-theme&projects=&template=create-theme.yml&title=%5Bcreate-theme%5D%3A+> 打开创建主题表单，填入上面的元数据，并粘贴 `chrome.css`、`README.md` 和 `preferences.json` 的内容。主题商店机器人会负责创建主题目录和后续 PR。

当前不提交 issue：最终预览图和实机验收尚未完成。
