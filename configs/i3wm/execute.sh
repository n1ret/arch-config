#!/bin/sh

paru -S i3-wm \
        sddm qt5-quickcontrols2 qt5-graphicaleffects qt5-svg

sudo systemctl enable sddm.service

