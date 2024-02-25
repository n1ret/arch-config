#!/bin/bash

sudo reflector --latest 5 --protocol https --sort rate --save /etc/pacman.d/mirrorlist
