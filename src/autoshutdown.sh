#!/bin/bash
#

function beep() {
    for i in 1 2 3 4 5
    do
        tput bel
        echo -e "\a"
        sleep 1
    done
}


while true; do
    if [ $(cat /sys/class/power_supply/axp20x-battery/capacity) -le 3 ]; then
        beep;
        sudo shutdown -h 3
    fi
    sleep 60
done