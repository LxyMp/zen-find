"""Offline development installer for Zen 1.22b; never loads browser scripts."""
import argparse
import json
import shutil
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def install(profile):
    profile = profile.resolve()
    if not (profile / "prefs.js").is_file():
        raise ValueError("请选择包含 prefs.js 的 Zen 配置目录")
    if any((profile / name).exists() or (profile / name).is_symlink()
           for name in ("parent.lock", ".parentlock", "lock")):
        raise ValueError("配置目录存在锁文件；请退出使用此目录的 Zen 后重试")
    registry = profile / "zen-themes.json"
    mods = json.loads(registry.read_text()) if registry.exists() else {}
    if not isinstance(mods, dict):
        raise ValueError("zen-themes.json 必须是对象；未修改配置")
    mod = json.loads((ROOT / "theme.json").read_text())
    for key in ("style", "readme", "preferences"):
        mod[key] = (ROOT / mod[key]).as_uri()
    mod["enabled"] = True
    updated = {**mods, mod["id"]: mod}
    destination = profile / "chrome" / "zen-themes" / mod["id"]
    # Read every dependency before touching the profile, including other mods.
    styles = []
    for key, entry in updated.items():
        if entry.get("enabled", True):
            source = (ROOT / "chrome.css" if key == mod["id"] else
                      profile / "chrome" / "zen-themes" / entry["id"] / "chrome.css")
            styles.append(source.read_text())
    stylesheet = profile / "chrome" / "zen-themes.css"
    backup = profile / "zen-find-backups" / datetime.now().strftime("%Y%m%d-%H%M%S-%f")
    backup.mkdir(parents=True)
    for source in (registry, stylesheet, destination):
        if source.is_dir():
            shutil.copytree(source, backup / source.name)
        elif source.exists():
            shutil.copy2(source, backup / source.name)
    destination.mkdir(parents=True, exist_ok=True)
    for source, target in (("chrome.css", "chrome.css"),
                           ("preferences.json", "preferences.json"),
                           ("README.md", "readme.md")):
        shutil.copy2(ROOT / source, destination / target)
    registry.write_text(json.dumps(updated, ensure_ascii=False, indent=2) + "\n")
    stylesheet.write_text("/* Local development install for Zen 1.22b. */\n" + "\n".join(styles))
    print(f"已安装到 {destination}\n备份：{backup}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("profile", type=Path)
    args = parser.parse_args()
    try:
        install(args.profile)
    except (OSError, ValueError, KeyError) as error:
        parser.exit(1, f"安装失败：{error}\n")
