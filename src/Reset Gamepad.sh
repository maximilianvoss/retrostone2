#!/bin/bash
#

ps aux | grep tz_gpio | grep sudo | awk '{ printf("sudo kill -9 %s\n", $2); }' | /bin/bash
sudo python /home/pi/RetrOrangePi/GPIO/drivers/tz_gpio_controller.py &