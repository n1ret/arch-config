#!/bin/zsh

start=$PWD
cd /tmp

sudo pacman -S --needed base-devel
git clone https://aur.archlinux.org/paru.git
cd paru
makepkg -si

cd $start
