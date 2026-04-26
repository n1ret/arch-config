#!/bin/sh

base_dir="$(dirname "$(realpath "$0")")/../.."

"$base_dir"/scripts/install_paru

sudo paru -S --needed \
  noto-fonts noto-fonts-cjk noto-fonts-emoji \
  zsh-syntax-highlighting zsh-autosuggestions zsh-theme-powerlevel10k

