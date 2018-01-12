# Sends temperature and humidity data to Thingspeak from a SHT sensor connected to Raspberry
# Requires sht-sensor library to be installed

# Sends data in every 10 mins:
# crontab -e
# */10 * * * * /usr/bin/python /home/pi/sht_thingspeak.py

# The connections are SCK pin: GPIO 21, DATA pin: GPIO 17
# tamasharasztosi, 2018

import sys
import time
import RPi.GPIO as GPIO
from time import sleep
from sht_sensor import Sht
import urllib2

myAPI = "FILL_WITH_YOUR_API"    
sht = Sht(21, 18)              # SCK pin: GPIO 21, DATA pin: GPIO 17

print 'Temperature', sht.read_t()
print 'Relative Humidity', sht.read_rh()

baseURL = 'https://api.thingspeak.com/update?api_key=FILL_WITH_YOUR_API'
urllib2.urlopen(baseURL + "&field1=%s&field2=%s" % (sht.read_t(), sht.read_rh())).read()
