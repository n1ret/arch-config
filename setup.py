import os
import shutil
from os.path import isdir, isfile, join, split

from dirs import CONFIGS, DIRS_ALIASES, HOME

if os.getuid() != 0 or os.getenv("SUDO_UID") is None:
    print('Run script under sudo')
    quit(-1)

uid = int(os.getenv("SUDO_UID"))
gid = int(os.getenv("SUDO_GID"))
for src, dst in DIRS_ALIASES:
    src = join(CONFIGS, src)
    for dir, dirs, files in os.walk(src):
        if split(dir)[-1].startswith(".git"):
            continue

        dst_dir = join(dst, dir.removeprefix(src).lstrip(os.sep))

        if not isdir(dst_dir):
            os.mkdir(dst_dir)
            if dst.startswith(HOME):
                os.chown(dst_dir, uid, gid)

        for file in files:
            if file == ".git":
                continue
            file_path = join(dir, file)

            dst_path = join(dst_dir, file)

            if isfile(dst_path):
                os.remove(dst_path)

            shutil.copy(
                file_path, dst_path
            )

            if dst.startswith(HOME):
                os.chown(dst_path, uid, gid)

print("Done!")
