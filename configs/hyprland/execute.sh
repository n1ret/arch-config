#!/bin/sh

$(dirname $(realpath "$0"))/../../install_paru.sh

paru -S hyprland hyprpaper hyprlock hypridle \
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
        firefox

sudo systemctl enable sddm.service
systemctl enable --user pipewire-pulse.service pipewire.service

