# Zen 核对记录（1.23.3b 当前，1.22b 历史基线）

当前视觉方向（2026-09-08）：采用不透明纯色背景、扁平边框和外部边缘阴影。毛玻璃已移出验收范围；此前跨文档模糊实验保留在 `GLASS-INVESTIGATION.md`。

> 2026-10-20 状态：本机 Zen 已更新为 **1.23.3b（Gecko 158.0，BuildID 20261016101044）**。本文的 1.22b 记录保留为历史基线。当前 CSS 的基准版本（默认顶部 12px、计数 140px）已在 1.23.3b 临时 profile 完成交互、布局与主题验收；随后默认顶部改为 40px、计数宽度改为 180px，并加入 180/140ms 开合动画。最终位置和动画已在本机日常配置确认；中文长计数尚未重新截图确认。本文的九位置/尺寸测量对应参数变更前基线，最终参数见下方。1.22b 本轮未复测（本机没有 1.22b 可执行环境）。

## 依据

当前应用包：

- `/Applications/Zen.app/Contents/Resources/application.ini`：Version=1.23.3b，Gecko=158.0，BuildID=20261016101044。
- `browser/omni.ja` 的 `chrome/browser/content/browser/zen-components/ZenMods.mjs`：string 偏好写为 `--<property>` 变量，空值移除；`#writeStylesheet` 读取本地 `chrome/zen-themes/<id>/chrome.css`；`#downloadUrlToFile` 只接受 HTTPS。
- `omni.ja` 的 `chrome/toolkit/content/global/elements/findbar.js`：`findbar > hbox.findbar-container`；输入与前后导航在 `hbox[anonid="findbar-textbox-wrapper"]`；四个 checkbox 和状态/计数是 container 的直接子元素；关闭按钮是 findbar 的直接子元素。
- `chrome/toolkit/skin/classic/global/findbar.css`：原生 `[hidden]` 用 `display:flex !important; visibility:collapse` 做开合过渡；`.findbar-container` 高 32px；计数和状态有原生 margin。
- `chrome/browser/skin/classic/browser/tabbrowser/content-area.css`：`.browserContainer` 是 grid，包含 `browserstack` 与 `findbar` 区域。
- `Tabbrowser.sys.mjs`：查找栏按标签页创建；实测 1.23.3b 中父节点为 `box.browserContainer`。
- `zen-theme.css` 提供 `--zen-colors-tertiary`、`--zen-colors-border`、`--zen-colors-input-bg`、`--zen-input-border-color`、`--zen-border-radius` 等变量；`--toolbarbutton-hover-background` 不存在，原生用 `--toolbarbutton-background-color-hover`。

1.22b 历史记录：application.ini 曾为 Version=1.22b、Gecko=155.0.1、BuildID=20260904060728、SourceStamp c2a638b7f735c7e7d4ee22e0182c8f6a16da93e5；当时的 findbar 结构、类名和变量与上述 1.23.3b 记录基本一致。

## 已执行

- 勾选项悬停区域修复：四列等宽；Zen 1.22b 原生布局测量均为 125.5px，消除最后一列独占剩余空间。窄面板使用两列。
- 材质参考：Transparent Zen 1.17.16 的 chrome.css 仅用于参考透明底色、高光边框、内阴影；未复制其全局页面透明或整页滤镜规则。
- 计数布局：通过原生匹配计数更新路径检查 560px/300px 面板；2026-10-20 起，容器宽度 ≤420px 时计数移到输入行下方，避免挤占输入区。计数宽度默认 `min(180px, 42cqw)`，输入框右 padding 按计数宽 + 18px 预留；已在 1.23.3b 实测基础布局通过，180px 下中文长计数尚未重新截图确认。
- 开合动画：默认顶部位置从内容区顶部进入（隐藏态上移 40px、scale 0.9、opacity 0），关闭时反向退出；入场 180ms、退场 140ms，`visibility` 延迟 140ms；只改变 `transform` 与 `opacity`，`prefers-reduced-motion` 关闭动画。
- 视觉优化：1.22b 无头截图检查 560px 和 300px 面板；1.23.3b 在 GUI 临时 profile 重新截图检查。
- 密集文字背景测试未观察到 backdrop-filter 模糊网页；当前 CSS 通过相对色语法强制 alpha=1，保证背景为不透明纯色。
- JSON 语法与 Git 差异空白检查。
- 安装工具临时配置测试：保留其他 Mod、重复安装、备份、拒绝锁定和损坏配置。
- CSS 源码检查：无相对导入、无 FindToolbar ID、使用真实按钮类名、默认两轴独立、内容换行、隐藏态不显示。

## 1.23.3b 验收（2026-10-20，参数变更前基线）

环境：临时 profile `/tmp/zf-verify`，经 `tools/install_local.py` 安装当时 `chrome.css`，Zen 1.23.3b GUI，Marionette 驱动。测试实例临时设置 `MOZ_DISABLE_CONTENT_SANDBOX=1`，仅用于验证；用户日常 profile 未修改。以下交互/主题结论仍适用于当前 CSS；布局测量值对应 top:12px、count:140px 的基线。

### 交互

测试页：`alpha alpha alpha` / `Alpha ALPHA` / `café cafe` / `cat concatenate cats`。

- `alpha`：默认 `1 of 5 matches`；Enter → `2 of 5 matches`；Shift+Enter → `1 of 5 matches`。
- Esc：findbar 关闭（`hidden=true`）。
- Match Case：关 `1 of 5`，开 `1 of 3`，再关 `1 of 5`。
- Whole Words（查询 `cat`）：关 `1 of 3`，开 `1 of 1`，再关 `1 of 3`。
- Match Diacritics（查询 `cafe`）：关 `1 of 2`，开 `1 of 1`，再关 `2 of 2`。
- Highlight All：开时 checkbox `checked` 且原生 `_highlightAll=true`，关时恢复。
- 无匹配 `zzzznotfound`：计数隐藏，状态为 `Phrase not found`。
- 四个 checkbox 均可见；前后按钮可用；关闭按钮存在。

### 布局与位置

- findbar 父节点为 `box.browserContainer`；`grid-area: browserstack` 计算值生效。
- 1280x900、侧栏展开：browserContainer `[230,42,1042,850]`，findbar `[471,54,560,86]`。
- 九种位置全部通过：left/center/right 的 x 为 242/695/1148，top/center/bottom 的 y 为 20/499/978（12px 边距与 50% 居中公式成立；测量窗口的 browserContainer 为 `[230,8,1490,1068]`）。
- 窄面板：520x800 时 browserContainer 宽 282，findbar 258x150，输入框 140px、`padding-right:9px`，选项 2x2；请求 320 被 macOS 最小窗口钳制为 500，findbar 仍为 238x150，输入框 120px，无重叠。238px 比 320px 更窄，覆盖 320px 场景。
- 隐藏开关：宽面板高 54px、窄面板高 75px；前后按钮和四个选项均 `display:none`；关闭、输入、计数保留。
- 焦点：原生 2px outline、offset -2px；hover 变量解析为 Zen color-mix 值。
- 侧栏收起：browserContainer `[60,42,1212,850]`，findbar `[386,54,560,86]`；展开恢复。
- 紧凑模式（520 宽）：browserContainer `[8,42,504,750]`，findbar `[20,54,480,97]`，输入框 362px；关闭后恢复。
- 分屏：两个非空标签页各占 518px 宽；选中面板的 findbar 为 `[242,54,494,97]`，完整位于半屏内；`unsplitCurrentView()` 后恢复。
- 禁用 Mod：原生 findbar 回到 `static`、`grid-area:findbar`、`[230,850,1042,43]`，背景为原生半透明；重新启用后恢复 absolute `[471,54,560,86]`。

### 主题与背景

- 浅色：findbar 背景 `color(srgb 0.981726 0.990275 1)`，文字 `rgb(21,20,26)`。
- 深色：背景 `color(srgb 0.0621961 0.0637255 0.0654118)`，文字 `rgb(251,251,254)`；网页内容保持自身颜色（CSS Mod 只改 chrome）。
- 自动：`zen.view.window.scheme=2` 在系统浅色下解析为 light；深色系统的自动切换未单独模拟。
- 自定义背景：`#ff0000` 显示为不透明红；`rgb(255 0 0 / 0.4)` 也被强制为不透明红。
- 已知限制：`transparent` 被相对色语法渲染为黑色；非法颜色使声明失效，背景变为透明。README 和商店说明已提示使用不透明合法颜色。

### 最终参数（2026-10-20 之后）

- 默认顶部：`inset: 40px auto auto 50%`；左侧/右侧/底部仍为 12px，中部垂直居中。
- 计数：`--zen-find-count-width: min(180px, 42cqw)`；输入框右 padding 为计数宽 + 18px；≤420px 仍移到输入行下方。
- 动画：入场 180ms、退场 140ms，scale 0.9；隐藏态仍 `display:flex`，用 `visibility` 延迟 140ms 隐藏；`prefers-reduced-motion` 关闭动画。只改变 `transform` 与 `opacity`。
- 确认范围：最终默认位置和动画已在本机日常配置确认；计数宽度已加宽，中文长计数尚未重新截图确认。未重新做完整九位置/窄宽结构化测量。动画按默认顶部位置设计；切换中部/底部时退场只上移 40px，不保证回到内容区顶部。

### 未覆盖

- 1.22b 本轮未复测（当前机器只有 1.23.3b）；1.22b 的历史定位记录保留在下方。
- Cmd/Ctrl+F 快捷键未用真实键盘事件单独模拟；已验证原生 findbar 打开、输入、Enter/Shift+Enter/Esc 路径，CSS 不改变快捷键处理。
- 深色系统的“自动”模式未单独模拟；已验证显式深色与显式浅色。
- 最终参数未重新做完整九位置/窄宽结构化测量；中文长计数在 180px 下的显示未重新截图确认。
- 商店 CC BY-NC-SA 4.0 授权需仓库作者本人确认。

## 1.22b 定位回归（历史）

使用 Marionette 启动独立临时配置的 Zen 1.22b（无头模式），打开原生查找栏，比较新旧 grid-area 的真实布局：网页区域 y=8、高度=752，旧 findbar 区域让查找栏 y=772，超出网页底边 760；改为 browserstack 后 y=20、高度=66。确认未打开开发者工具时已位于网页区域内。

## 1.22b 历史截图与限制

- 560px 与 300px 面板截图检查了输入/导航首行、四列/两列选项和关闭按钮位置。
- 1.22b 的计数布局、焦点样式和隐藏开关由后续 1.23.3b 验收覆盖；1.22b 本身未运行本轮完整用例。
- 非法颜色需在设置中改回有效值；`transparent` 会被相对色语法渲染为黑色，请使用不透明颜色。
