import os
import re
from argparse import ArgumentParser
from os.path import isdir, isfile, join, split

from dirs import CONFIGS, DIRS_ALIASES, HOME

PLACEHOLDER_RE = re.compile(r"\{\{([\w-]+)\}\}")
ESCAPED_PLACEHOLDER_RE = re.compile(r"\\\{\{([\w-]+)\}\}")


def expand_env_templates(text: str):
    escaped_backslashes = set()

    for i in range(len(text)):
        if (
            i >= 1
            and text[i] == "\\"
            and text[i - 1] == "\\"
            and i - 1 not in escaped_backslashes
        ):
            escaped_backslashes.update((i - 1, i))

    def replace_placeholder(match: re.Match):
        prev = match.start() - 1
        if prev >= 0 and text[prev] == "\\" and prev not in escaped_backslashes:
            return match.group(0)

        return os.getenv(match.group(1), "")

    def replace_escaped_placeholder(match: re.Match):
        return match.group(0).replace("\\{{", "{{")

    text = PLACEHOLDER_RE.sub(replace_placeholder, text)
    text = ESCAPED_PLACEHOLDER_RE.sub(replace_escaped_placeholder, text)

    return text.replace("\\\\", "\\")


def expand_data(data: bytes):
    try:
        source_text = data.decode("utf-8")
    except UnicodeDecodeError:
        return data

    return expand_env_templates(source_text).encode("utf-8")


def main():
    if os.getuid() != 0 or os.getenv("SUDO_UID") is None:
        print("Run script via sudo")
        quit(-1)

    argparser = ArgumentParser(description="Setup configs utility")
    argparser.add_argument(
        "--config",
        "-c",
        choices=[
            path
            for path in os.listdir(CONFIGS)
            if isdir(join(CONFIGS, path)) and path != "global"
        ],
        help="Config variant",
    )

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
                print(
                    f"Config `{config}` is not installed because "
                    f"execute.sh exit with code {status_code}"
                )
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

                    with open(file_path, "rb") as src_file:
                        src_content = src_file.read()

                    with open(dst_path, "wb") as dst_file:
                        dst_file.write(expand_data(src_content))

                    if dst.startswith(HOME):
                        os.chown(dst_path, uid, gid)

    print("Done!")


if __name__ == "__main__":
    main()
