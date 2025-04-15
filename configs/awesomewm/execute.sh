#!/bin/sh

base_dir="$(dirname $(realpath "$0"))/../.."

$base_dir/scripts/install_paru

paru --needed -S \
    awesome numlockx \
    lightdm lightdm-gtk-greeter \
    kitty

