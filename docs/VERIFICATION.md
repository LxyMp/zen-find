# Zen 1.22b 核对记录

## 依据

直接读取 `/Applications/Zen.app/Contents/Resources/` 应用包：

- application.ini：Version=1.22b，Gecko=155.0.1，BuildID=20260904060728。
- SourceStamp：c2a638b7f735c7e7d4ee22e0182c8f6a16da93e5。
- browser/omni.ja 的 tabbrowser.js：按标签页创建 findbar，没有固定 ID。
- omni.ja 的 elements/findbar.js：导航类名 findbar-find-previous、findbar-find-next；关闭类名 findbar-closebutton。
- 选项类名 findbar-highlight、findbar-case-sensitive、findbar-match-diacritics、findbar-entire-word。
- 匹配计数 found-matches，查找状态 findbar-find-status。
- zen-theme.css 提供 --zen-colors-secondary、--zen-colors-input-bg、--zen-colors-border、--zen-input-border-color、--zen-border-radius；背景变量使用 light-dark 跟随主题。
- ZenMods.mjs 下载字符串 URL 字段 style/readme/preferences；拼接各 Mod CSS；string 偏好为空时移除对应 CSS 变量。

## 已执行

- JSON 语法与 Git 差异空白检查。
- 安装工具临时配置测试：保留其他 Mod、重复安装、备份、拒绝锁定和损坏配置。
- CSS 源码检查：无相对导入、无 FindToolbar ID、使用真实按钮类名、默认两轴独立、内容换行、隐藏态不显示。

## 待实机验收

### 定位回归（已验证）

使用 Marionette 启动独立临时配置的 Zen 1.22b（无头模式），打开原生查找栏，比较新旧 grid-area 的真实布局：网页区域 y=8、高度=752，旧 findbar 区域让查找栏 y=772，超出网页底边 760；改为 browserstack 后 y=20、高度=66。确认未打开开发者工具时已位于网页区域内。此项为原生布局验证，不代表下面所有桌面视觉场景已通过。

以下项目尚未宣称通过，不能用源码检查替代：

- 九个位置组合及从未设置横向偏好时的垂直居中。
- 浅色、深色、自动主题和实际毛玻璃合成效果；颜色与 0/0.72/1 不透明度。
- 320/520/1280 像素窗口、侧栏展开/收起、紧凑模式和分屏。
- Cmd/Ctrl+F、Esc、Enter、Shift+Enter、无匹配与计数。
- 全部按钮及隐藏开关、禁用 Mod 后恢复原生布局。

模糊效果取决于浏览器合成层，CSS 声明不保证能模糊网页背后的像素。非法颜色和非数字不透明度需在设置中改回有效值。
