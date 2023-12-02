import os
from argparse import ArgumentParser, ArgumentTypeError, Namespace
from os import path

from dirs import BIN_DIR, CONFIGS, DIRS_ALIASES


class PathType:
    def __call__(self, string):
        if not path.exists(string):
            raise ArgumentTypeError(f"\"{string}\" is not exists")
        return string


def install():
    command = f"export PATH=$PATH:{BIN_DIR}"
    with open("/etc/profile.d/n1ret-cfg.sh", 'w') as f:
        f.write(command)
    os.system(command)


def delete():
    os.remove("/etc/profile.d/n1ret-cfg.sh")


def copy_file(abspath: str, uid: int, gid: int):
    if not path.isfile(abspath):
        answer = input(f"File {abspath} is not exists. Do you want to ignore? [Y/n] ")
        if answer.lower() not in ('y', ''):
            quit()
        else:
            return

    for dst, src in DIRS_ALIASES:
        if not abspath.startswith(src):
            continue

        dstpath = path.join(CONFIGS, dst, abspath.removeprefix(src).lstrip('/'))

        # Create dir
        cur_dir = CONFIGS + '/'
        for dir in path.dirname(dstpath.removeprefix(cur_dir)).split(path.sep):
            cur_dir += dir + '/'
            if not path.isdir(cur_dir):
                if path.isfile(cur_dir.rstrip('/')):
                    answer = input(f"Do you want to delete {cur_dir}? [Y/n] ")
                    if answer.lower() in ('y', ''):
                        os.remove(cur_dir)
                os.mkdir(cur_dir)
                os.chown(cur_dir, uid, gid)

        # Create file
        with open(dstpath, 'wb') as f:
            with open(abspath, 'rb') as src_file:
                f.write(src_file.read())
        os.chown(dstpath, uid, gid)

        break
    else:
        print(f"Available only {', '.join(map(lambda t: t[1], DIRS_ALIASES))} dirs")


def update_config(args: Namespace, uid: int, gid: int):
    abspath: str = path.abspath(args.src)
    if path.isfile(abspath):
        copy_file(abspath, uid, gid)
    else:
        if not args.recursive:
            print("Dir specified without --recursive argument")
            return

        for dir, _, nstd_files in os.walk(abspath):
            for nstd_file in nstd_files:
                copy_file(path.join(dir, nstd_file), uid, gid)


def main():
    if os.getuid() != 0 or os.getenv("SUDO_UID") is None:
        print('Run the script under sudo')
        return

    parser = ArgumentParser(description="Update config files for setup.py")
    parser.add_argument("--recursive", "-r", action="store_true")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--src", "-s", type=PathType(),
        help="Source file path"
    )
    group.add_argument(
        "--install", "-i", action="store_true",
        help="Specify to install arch-cfg.sh script with push dir to PATH"
    )
    group.add_argument(
        "--delete", "-d", action="store_true",
        help="Specify to remove arch-cfg.sh script with push dir to PATH"
    )
    args = parser.parse_args()
    uid = int(os.getenv("SUDO_UID"))
    gid = int(os.getenv("SUDO_GID"))

    if args.install:
        install()
        print("! Relogin needed")

    elif args.delete:
        delete()
        print("! Relogin needed")

    if args.src:
        update_config(args, uid, gid)
    
    print("Done")


if __name__ == "__main__":
    main()
