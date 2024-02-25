#!/bin/sh

start=$PWD
cd /tmp

sudo pacman -S --needed base-devel

if ! command -v rustup > /dev/null; then 
    ./install_rust.sh
fi

[ $(rustup show active-toolchain | wc -l) -ne 0 ] || rustup default stable

rm -rf paru
git clone https://aur.archlinux.org/paru.git
cd paru

makepkg -si

cd $start
