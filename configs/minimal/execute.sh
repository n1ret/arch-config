#!/bin/sh

base_dir="$(dirname "$(realpath "$0")")/../.."

"$base_dir"/scripts/install_paru

paru -S --needed \
  zsh zsh-syntax-highlighting zsh-autosuggestions zsh-theme-powerlevel10k

chsh -s /bin/zsh
sudo chsh -s /bin/zsh
