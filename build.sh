#!/usr/bin/sh

script_dir="$(dirname "$(realpath "$0")")"

mkdir -p "$script_dir/bin" && \
  python -m venv __venv && \
  __venv/bin/pip install pyinstaller && \
  __venv/bin/pyinstaller --onefile --distpath "$script_dir/bin" arch-cfg.py && \
  sudo rm -rf __venv build __pycache__ arch-cfg.spec
