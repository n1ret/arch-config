import os
import sys

if getattr(sys, 'frozen', False):
    DIR = os.path.dirname(sys.executable).removesuffix("/bin")
else:
    DIR = os.path.dirname(__file__)
BIN_DIR = os.path.join(DIR, "bin")
CONFIGS = os.path.join(DIR, "configs")
HOME = os.path.expanduser(f"~{os.getenv('SUDO_USER')}")
DIRS_ALIASES = (
    ("usr", "/usr"),
    ("etc", "/etc"),
    ("root", "/root"),
    ("home", HOME)
)
