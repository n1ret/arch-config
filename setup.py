import os
import shutil
from argparse import ArgumentParser
from os.path import isdir, isfile, join, split

from dirs import CONFIGS, DIRS_ALIASES, HOME

if os.getuid() != 0 or os.getenv("SUDO_UID") is None:
    print('Run script via sudo')
    quit(-1)

argparser = ArgumentParser(description="Setup configs utility")
argparser.add_argument("--config", "-c",
                       choices=[path
                                for path in os.listdir(CONFIGS)
                                if isdir(join(CONFIGS, path))
                                   and path != "global"],
                       help="Config variant")

args = argparser.parse_args()

uid = int(os.getenv("SUDO_UID"))
gid = int(os.getenv("SUDO_GID"))

for config in ("global", args.config):
    if not config:
        continue

    execute_path = join(CONFIGS, config, "execute.sh")
    if isfile(execute_path) and os.access(execute_path, os.X_OK):
        result = os.system(f"sudo -u $SUDO_USER {execute_path}")
        status_code = result >> 8
        if status_code != 0:
            print(f"Config `{config}` is not installed becouse execute.sh exit with code {status_code}")
            continue

    for src, dst in DIRS_ALIASES:
        src = join(CONFIGS, config, src)
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
