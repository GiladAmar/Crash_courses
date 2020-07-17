#!/usr/bin/env bash

# run 'xrandr' to get list of displays and available resolutions

# Set displays
xrandr--output eDP-1-1 --mode 1920x1080 --primary --output HDMI-0 --mode 1920x1080 --right-of eDP-1-1

# run main python script
source ./bin/activate
python main.py