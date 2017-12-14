#!/bin/bash

########################################################################
# This file is supposed to run on the mobile/wearable devices
# It grabs xml files and coresponding PNGs
########################################################################
rounds=$((1))

while [ true ]
do
    sleep 5
    rounds=$(($rounds+1))
    #uiautomator dump /sdcard/$file.txt
    echo $rounds
    uiautomator dump /sdcard/screencaps/$rounds.xml
    screencap -p $rounds.png

done
