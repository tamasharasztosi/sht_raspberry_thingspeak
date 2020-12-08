# sht_raspberry_thingspeak
#### Sends temperature and humidity data to Thingspeak from a SHT sensor connected to Raspberry

*Requires sht-sensor library to be installed: https://github.com/mk-fg/sht-sensor*

Basic usage:

> python sht_thingspeak.py

Sends data in every 10 mins:

> crontab -e

> */10 * * * * /usr/bin/python /home/pi/sht_thingspeak.py

The connections are SCK pin: GPIO 21, DATA pin: GPIO 18


*tamasharasztosi, 2018*
