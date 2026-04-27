import os
import re
import shutil
import subprocess
import tempfile
from argparse import ArgumentParser
from os.path import isdir, isfile, join, split

from dirs import CONFIGS, DIRS_ALIASES

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


def is_system_path(path: str):
    return not path.startswith("/home") and path.startswith("/")


def run_sudo(cmd: list[str]):
    return subprocess.run(["sudo", *cmd]).returncode


def main():
    if os.getuid() == 0:
        print("Do not run this script as root")
        quit(-1)

    sudo_available = not shutil.which("sudo") is not None

    if sudo_available:
        print("Sudo is not available")
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

    sudo_validated = False

    def check_sudo(path: str):
        nonlocal sudo_available, sudo_validated

        if not sudo_available:
            print(
                f"Skipping `{path}` because sudo is not available for system path copy"
            )

            return False
        if not sudo_validated:
            if run_sudo(["-v"]) != 0:
                print("Skipping system path copy because sudo authentication failed")
                sudo_available = False
                return False
            sudo_validated = True

        return True

    for config in ("global", args.config):
        if not config:
            continue

        execute_path = join(CONFIGS, config, "execute.sh")
        if isfile(execute_path) and os.access(execute_path, os.X_OK):
            result = subprocess.run([execute_path])
            status_code = result.returncode
            if status_code != 0:
                print(
                    f"Config `{config}` is not installed because "
                    f"execute.sh exit with code {status_code}"
                )
                continue

        for src, dst in DIRS_ALIASES:
            src = join(CONFIGS, config, src)
            for dir, _, files in os.walk(src):
                if split(dir)[-1].startswith(".git"):
                    continue

                dst_dir = join(dst, dir.removeprefix(src).lstrip(os.sep))

                if is_system_path(dst_dir):
                    if not check_sudo(dst_dir):
                        continue

                    if run_sudo(["mkdir", "-p", dst_dir]) != 0:
                        print(f"Skipping `{dst_dir}` because directory creation failed")
                        continue
                else:
                    os.makedirs(dst_dir, exist_ok=True)

                for file in files:
                    if file in (".git", ".gitignore", ".gitattributes"):
                        # Ignore submodule metadata
                        continue

                    file_path = join(dir, file)

                    dst_path = join(dst_dir, file)
                    src_mode = os.stat(file_path).st_mode & 0o777

                    with open(file_path, "rb") as src_file:
                        src_content = src_file.read()
                    dst_content = expand_data(src_content)

                    if is_system_path(dst_path):
                        if not check_sudo(dst_path):
                            continue

                        with tempfile.NamedTemporaryFile() as tmp:
                            tmp.write(dst_content)

                            if (
                                run_sudo(
                                    [
                                        "install",
                                        "-m",
                                        f"{src_mode:o}",
                                        tmp.name,
                                        dst_path,
                                    ]
                                )
                                != 0
                            ):
                                print(
                                    f"Skipping `{dst_path}` because "
                                    "privileged copy failed"
                                )
                    else:
                        if isfile(dst_path):
                            os.remove(dst_path)

                        with open(dst_path, "wb") as dst_file:
                            dst_file.write(dst_content)
                        os.chmod(dst_path, src_mode)

    print("Done!")


if __name__ == "__main__":
    main()
