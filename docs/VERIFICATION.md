# Zen 核对记录（1.22b 基线，1.23.3b 待复测）

当前视觉方向（2026-09-08）：采用不透明纯色背景、扁平边框和外部边缘阴影。毛玻璃已移出验收范围；此前跨文档模糊实验保留在 `GLASS-INVESTIGATION.md`。

> 2026-10-20 状态：本机 Zen 已更新为 **1.23.3b（Gecko 158.0，BuildID 20261016101044）**。以下 1.22b 记录保留为历史基线；1.23.3b 的实机复测尚未完成。

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

- 勾选项悬停区域修复：四列等宽；Zen 1.22b 原生布局测量均为 125.5px，消除最后一列独占剩余空间。窄面板仍使用两列。
- 用户明确玻璃参考为 Transparent Zen 的主侧边栏，而非 Glance。其侧边栏规则涉及工具栏背景透明、titlebar 伪元素和遮罩；不能直接等同于覆盖网页的 backdrop-filter。后续以主侧边栏柔和透色为视觉目标，尚未复现背景模糊。

- 材质参考：Transparent Zen 1.17.16（sameerasw，商店 ID 642854b5-88b4-4c40-b256-e035532109df）的 chrome.css 使用明暗主题透明底色、高光边框、内阴影，Glance 侧栏使用 backdrop-filter。参考这些手法调整本项目，未复制其全局页面透明或整页滤镜规则。
- 本轮以 headless=False 启动独立 Zen 1.22b，检查密集文字页面：中性主题底色及边缘层次生效，但截图中的网页文字仍未模糊。不能宣称已实现与 Transparent Zen 相同的背景采样效果。当前实现已改为强制不透明纯色，不透明度设置不再存在。

- 计数布局：通过原生 onMatchesCountResult 注入 2/10 状态并由 Fluent 生成文本，在 560px/300px 面板截图中检查计数位于输入框尾部、输入框预留空间、选项紧凑排列。极长本地化计数允许省略显示；无结果和循环提示仍保留原生状态区域。2026-10-20 起，窄面板（容器宽度 ≤420px）将计数移到输入行下方，避免挤占输入区；此项待 1.23.3b 实机复测。

- 视觉优化：Zen 1.22b 无头原生截图检查 560px 和 300px 面板，输入/导航独立首行，选项分别按四列和两列排列，关闭按钮固定右侧。
- 密集文字背景测试中未观察到 backdrop-filter 模糊网页；当前 CSS 通过相对色语法强制 alpha=1，保证背景为不透明纯色。不能宣称真实毛玻璃已实现，桌面 GPU 合成仍待验证。

- JSON 语法与 Git 差异空白检查。
- 安装工具临时配置测试：保留其他 Mod、重复安装、备份、拒绝锁定和损坏配置。
- CSS 源码检查：无相对导入、无 FindToolbar ID、使用真实按钮类名、默认两轴独立、内容换行、隐藏态不显示。

## 待实机验收

### 定位回归（1.22b 已验证）

使用 Marionette 启动独立临时配置的 Zen 1.22b（无头模式），打开原生查找栏，比较新旧 grid-area 的真实布局：网页区域 y=8、高度=752，旧 findbar 区域让查找栏 y=772，超出网页底边 760；改为 browserstack 后 y=20、高度=66。确认未打开开发者工具时已位于网页区域内。此项为原生布局验证，不代表下面所有桌面视觉场景已通过。

以下项目在 1.23.3b 上尚未宣称通过，不能用源码检查替代：

- 九个位置组合及从未设置横向偏好时的垂直居中。
- 浅色、深色和自动主题；默认背景、自定义背景及带 Alpha 的颜色输入均应显示为不透明纯色。
- 320/520/1280 像素窗口、侧栏展开/收起、紧凑模式和分屏。
- Cmd/Ctrl+F、Esc、Enter、Shift+Enter、无匹配与计数。
- 全部按钮及隐藏开关、禁用 Mod 后恢复原生布局。

非法颜色需在设置中改回有效值；`transparent` 会被相对色语法渲染为黑色，请使用不透明颜色。

## 1.23.3b 待复测重点

- 确认 findbar 实际父节点与 `grid-area: browserstack` 是否仍生效：1.23.3b 源码中 `#createFindBar` 将 findbar 插到 `browser.parentNode` 之后，而 browser 位于 `.browserStack` 内；原生布局 CSS 仍写 `.browserContainer > findbar`。
- 复测窄面板（≤420px）计数独占一行后的输入宽度、选项两列和隐藏开关。
- 复测原生焦点环、悬停色、非法/`transparent` 背景和开合动画。
- 九种位置、深浅/自动主题、320/520/1280、侧栏、紧凑、分屏、快捷键、禁用恢复。
