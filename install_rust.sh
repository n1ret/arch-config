#!/bin/sh

cancel_i () {
    echo "Installation canceled"
    exit 1
}

sudo pacman -S rustup
[ "$?" -eq 0 ] || cancel_i

rustup default stable

echo "Rust lang installed"
