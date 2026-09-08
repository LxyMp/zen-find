import importlib.util
import json
import tempfile
import unittest
import subprocess
import sys
from pathlib import Path

spec = importlib.util.spec_from_file_location("installer", Path(__file__).with_name("install_local.py"))
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallerTests(unittest.TestCase):
    def test_actual_lock_blocks_install(self):
        with tempfile.TemporaryDirectory() as directory:
            profile = Path(directory)
            (profile / "prefs.js").touch()
            code = "import fcntl,sys; f=open(sys.argv[1],'a+b'); fcntl.lockf(f,fcntl.LOCK_EX); print('ready',flush=True); sys.stdin.read()"
            process = subprocess.Popen(
                [sys.executable, "-c", code, str(profile / ".parentlock")],
                stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
            try:
                self.assertEqual(process.stdout.readline().strip(), "ready")
                with self.assertRaises(ValueError):
                    installer.install(profile)
                self.assertFalse((profile / "zen-themes.json").exists())
            finally:
                process.communicate(timeout=5)
            # The file remains after exit, but its kernel lock has been released.
            self.assertTrue((profile / ".parentlock").exists())
            installer.install(profile)
            self.assertTrue((profile / "zen-themes.json").exists())

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
