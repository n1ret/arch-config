#!/bin/sh

base_dir="$(dirname "$(realpath "$0")")/../.."

"$base_dir"/scripts/install_paru

paru -S --needed \
  aurorae bluedevil breeze breeze-cursors breeze-gtk kactivitymanagerd kde-cli-tools \
  kde-gtk-config kdecoration kdeplasma-addons kglobalacceld kinfocenter kmenuedit \
  knighttime kpipewire krdp kscreen kscreenlocker ksshaskpass ksystemstats kwallet-pam \
  kwayland kwin kwrited layer-shell-qt libkscreen libksysguard libplasma milou \
  ocean-sound-theme plasma-activities plasma-activities-stats plasma-browser-integration \
  plasma-desktop plasma-disks plasma-firewall plasma-integration plasma-keyboard plasma-login-manager \
  plasma-nm plasma-pa plasma-systemmonitor plasma-thunderbolt plasma-vault plasma-welcome plasma-workspace \
  plasma-workspace-wallpapers plasma5support polkit-kde-agent powerdevil print-manager qqc2-breeze-style \
  sddm-kcm spectacle systemsettings xdg-desktop-portal-kde \
  \
  kde-material-you-colors

