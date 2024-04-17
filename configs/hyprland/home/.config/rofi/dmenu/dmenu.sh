#!/usr/bin/env bash

## Author : Aditya Shakya (adi1090x)
## Github : @adi1090x
#
## Rofi   : Power Menu
#
## Available Styles
#
## style-1   style-2   style-3   style-4   style-5
## style-6   style-7   style-8   style-9   style-10

# Current Theme
dir="$HOME/.config/rofi/dmenu/"
theme='style-2'

# Rofi CMD
rofi_cmd() {
	rofi -dmenu \
         -p "" \
         -i \
		 -theme ${dir}/${theme}.rasi
}

# Pass variables to rofi dmenu
run_rofi() {
	cat - | rofi_cmd
}

run_rofi
