# sht_raspberry_thingspeak
#### Sends temperature and humidity data to Thingspeak from a SHT sensor connected to Raspberry

*Requires sht-sensor library to be installed: https://github.com/mk-fg/sht-sensor*

Basic usage:

> python sht_thingspeak.py

Sends data in every 10 mins:

> crontab -e

> */10 * * * * /usr/bin/python /home/pi/sht_thingspeak.py

This code shows SHT21 connected to BCM pin 24 (pin 18 on Rpi3)


*tamasharasztosi, 2018*
