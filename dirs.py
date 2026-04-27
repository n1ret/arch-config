import os
import sys

if getattr(sys, 'frozen', False):
    DIR = os.path.dirname(sys.executable).removesuffix("/bin")
else:
    DIR = os.path.dirname(__file__)
BIN_DIR = os.path.join(DIR, "bin")
CONFIGS = os.path.join(DIR, "configs")
HOME = os.getenv("HOME")
_sudo_user = os.getenv("SUDO_USER")
if _sudo_user is not None:
    HOME = os.path.expanduser(f"~{_sudo_user}")

if HOME is None:
    print("Can't detect home directory. A HOME or SUDO_USER var must be set")

    exit(1)

DIRS_ALIASES = (
    ("usr", "/usr"),
    ("etc", "/etc"),
    ("root", "/root"),
    ("home", HOME)
)
