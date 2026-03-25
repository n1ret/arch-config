#!/usr/bin/sh

prev_dir="$(pwd)"
script_dir="$(dirname "$(realpath "$0")")"

rm -rf "$script_dir/bin" &&
  mkdir -p "$script_dir/bin" &&
  cd "$script_dir/bin" && {
  python -m venv __venv &&
    __venv/bin/pip install pyinstaller &&
    __venv/bin/pyinstaller --onefile --distpath "$script_dir/bin" "$script_dir/arch_cfg.py" &&
    mv arch_cfg arch-cfg

  sudo rm -rf __venv build arch_cfg.spec
}

cd "$prev_dir" || exit
