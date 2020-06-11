#!/bin/bash
#

ps aux | grep tz_gpio | grep sudo | awk '{ printf("sudo kill %s\n", $2); }' | sh
sudo python /home/pi/RetrOrangePi/GPIO/drivers/tz_gpio_controller.py &