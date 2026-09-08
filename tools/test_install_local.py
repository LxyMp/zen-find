import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location("installer", Path(__file__).with_name("install_local.py"))
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallerTests(unittest.TestCase):
    def test_preserves_other_mod_and_reinstall(self):
        with tempfile.TemporaryDirectory() as directory:
            profile = Path(directory)
            (profile / "prefs.js").touch()
            other = profile / "chrome/zen-themes/other"
            other.mkdir(parents=True)
            (other / "chrome.css").write_text("/* existing mod */")
            entry = {"id": "other", "enabled": True}
            (profile / "zen-themes.json").write_text(json.dumps({"other": entry}))
            installer.install(profile)
            installer.install(profile)
            mods = json.loads((profile / "zen-themes.json").read_text())
            self.assertEqual(mods["other"], entry)
            self.assertEqual(len(mods), 2)
            css = (profile / "chrome/zen-themes.css").read_text()
            self.assertIn("/* existing mod */", css)
            self.assertNotIn("@import", css)
            self.assertEqual(css.count("/* existing mod */"), 1)
            self.assertEqual(len(list((profile / "zen-find-backups").iterdir())), 2)

    def test_locked_or_broken_profile_is_untouched(self):
        with tempfile.TemporaryDirectory() as directory:
            profile = Path(directory)
            (profile / "prefs.js").touch()
            (profile / "parent.lock").touch()
            with self.assertRaises(ValueError):
                installer.install(profile)
            self.assertFalse((profile / "zen-themes.json").exists())
            (profile / "parent.lock").unlink()
            (profile / "zen-themes.json").write_text("invalid json")
            with self.assertRaises(ValueError):
                installer.install(profile)
            self.assertEqual((profile / "zen-themes.json").read_text(), "invalid json")


if __name__ == "__main__":
    unittest.main()
