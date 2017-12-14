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
    echo $rounds
    uiautomator dump $rounds.xml
    screencap -p $rounds.png

done
