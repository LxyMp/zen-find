# Zen Find

为 **Zen 1.23.3b（Gecko 158.0）** 重设计原生查找栏的纯 CSS Mod；**Zen 1.22b（Gecko 155.0.1）** 为历史基线。1.23.3b 已完成交互、九位置、窗口、主题和禁用恢复的临时 profile 验收；随后默认顶部改为 40px、计数宽度改为 180px、加入 180/140ms 开合动画。位置和动画已在本机日常配置确认；中文长计数尚未重新截图确认。1.22b 本轮未复测，详见 `docs/VERIFICATION.md`。

默认显示在网页区域顶部下方 40px、水平居中；支持顶部/中部/底部与左侧/中部/右侧共九种组合（左侧/右侧/底部使用 12px 边距）。界面采用扁平化纯色背景和外部边缘阴影；背景留空时跟随 Zen 主题，也可在 Mod 设置中输入 CSS 颜色代码。背景始终按不透明颜色渲染，颜色中的 Alpha 值不会让网页透出。请使用不透明颜色；`transparent` 会被强制渲染为黑色，非法颜色会让背景失效。

查找栏带 180ms 入场、140ms 退场动画；系统开启“减少动态效果”时关闭。默认保留全部原生控件。开启隐藏选项后隐藏上一项、下一项、高亮全部、大小写、变音符号和完整单词选项；保留关闭、输入框与计数。隐藏不会重置查找选项，需调整时关闭隐藏设置。

## 本地开发安装

本项目以 Zen 1.23.3b 为当前验证目标；Zen 没有通用的“从本地目录安装”入口。本仓库提供离线开发安装工具，需要 Python 3。

1. 在 Zen 打开 `about:support`，找到“配置文件夹”，记录其完整路径。
2. 完全退出 Zen。建议先用 `about:profiles` 创建独立测试配置。
3. 在本项目目录执行，将示例路径替换为实际配置文件夹：

```sh
python3 tools/install_local.py "/完整路径/Zen配置文件夹"
```

4. 重新启动该配置的 Zen，在设置中的 Zen Mods 找到 Zen Find 并调整选项。若首次启动未显示默认设置，禁用后重新启用一次。

脚本合并 `zen-themes.json`，复制 CSS、设置和说明到 `chrome/zen-themes/<id>/`，重建 `chrome/zen-themes.css`，保留其他 Mod。覆盖前备份到配置目录的 `zen-find-backups/`。检测到锁文件或损坏的注册表时拒绝安装。

修改 CSS 后退出 Zen，再运行同一命令更新。禁用或卸载可在 Zen Mods 设置中完成；不要删除整个 `zen-themes.json`，其中包含其他 Mod。

## 打包约定

`chrome.css` 是自包含入口，不使用 `@import`。`theme.json` 中的相对路径仅供本地安装脚本解析，不能直接作为商店下载元数据。发布时须为 `style`、`preferences`、`readme` 填写真实 HTTPS URL，并按商店要求补齐元数据；当前尚未发布。

## 正式发布准备

源码仓库：<https://github.com/LxyMp/zen-find>。当前包版本为 `0.0.1`。

Zen Theme Store 的新 Mod 发布流程是：在[主题商店的创建主题 issue 模板](https://github.com/zen-browser/theme-store/issues/new?assignees=&labels=new-theme&projects=&template=create-theme.yml&title=%5Bcreate-theme%5D%3A+)中提交名称、描述、主页、PNG 预览图、CSS、README 和 `preferences.json`。维护者的机器人会根据 issue 创建主题目录和后续 PR；不需要直接修改主题商店仓库。

1.23.3b 基准验收已完成；最终位置和动画参数已在本机日常配置确认，计数已加宽到 180px（1.22b 历史记录见 `docs/VERIFICATION.md`）。提交前还需确认接受主题商店采用的 CC BY-NC-SA 4.0 授权；最终参数的完整结构化复测尚未完成。已准备当前版本的 PNG 预览图 `docs/images/store-preview.png`，尚未提交商店 issue。`tools/install_local.py` 仅用于本地开发，不作为商店主题文件提交。

## 验证状态

已核对 Zen 1.22b 安装包内原生结构、主题变量和 Mod 加载器，并静态核对 1.23.3b 的 findbar 结构与 Mod 加载器。安装工具已完成临时配置验证。1.23.3b 已在临时 profile 验收：输入、Enter/Shift+Enter、Esc、无匹配、四个原生选项、九位置、窄面板、侧栏、紧凑、分屏、深浅主题、自定义背景和禁用恢复。随后默认顶部改为 40px、计数宽度改为 180px、加入 180/140ms 开合动画；位置和动画已在本机日常配置确认，中文长计数尚未重新截图确认。仍缺 1.22b 回归、真实 Cmd/Ctrl+F 键盘路径、深色系统自动主题，以及最终参数的完整结构化复测；详见 `docs/VERIFICATION.md`。早期毛玻璃实验已停止，历史记录保留在 `docs/GLASS-INVESTIGATION.md`。
