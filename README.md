# Zen Find

为 **Zen 1.22b（Gecko 155.0.1）** 重设计原生查找栏的纯 CSS Mod。

默认显示在当前网页区域上方居中，支持九种位置组合。界面采用扁平化纯色背景和外部边缘阴影；背景留空时跟随 Zen 主题，也可在 Mod 设置中输入 CSS 颜色代码。背景始终按不透明颜色渲染，颜色中的 Alpha 值不会让网页透出。

默认保留全部原生控件。开启隐藏选项后隐藏上一项、下一项、高亮全部、大小写、变音符号和完整单词选项；保留关闭、输入框与计数。隐藏不会重置查找选项，需调整时关闭隐藏设置。

## 本地开发安装

Zen 1.22b 没有本项目之前声称的“从本地目录安装”入口。本仓库提供离线开发安装工具，需要 Python 3。

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

## 验证状态

已核对本机 Zen 1.22b 包内原生结构、主题变量和 Mod 加载器。安装工具已在临时配置夹验证。完整桌面交互和主题切换仍需实机验收，详见 `docs/VERIFICATION.md`。早期毛玻璃实验已停止，历史记录保留在 `docs/GLASS-INVESTIGATION.md`。
