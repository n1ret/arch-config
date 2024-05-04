#!/bin/sh

base_dir="$(dirname $(realpath "$0"))/../.."

$base_dir/scripts/install_paru

paru --needed -S \
    hyprland hyprpaper hyprlock hypridle \
    jq \
    rofi-lbonn-wayland wtype \
    brightnessctl \
    thunar \
    polkit-kde-agent \
    xdg-desktop-portal-hyprland \
    sddm qt5-quickcontrols2 qt5-graphicaleffects qt5-svg \
    pipewire pipewire-pulse \
    wl-clipboard cliphist \
    waybar \
    mako \
    neovim \
    firefox

sudo systemctl enable sddm.service
systemctl enable --user pipewire-pulse.service pipewire.service

