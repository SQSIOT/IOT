#!/usr/bin/env python
__author__ = 'skunda'
# This program logs a Raspberry Pi's CPU temperature to a Thingspeak Channel
# To use, get a Thingspeak.com account, set up a channel, and capture the Channel Key at https://thingspeak.com/docs/tutorials/ 
# Then paste your channel ID in the code for the value of "key" below.
# Then run as sudo python pitemp.py (access to the CPU temp requires sudo access)
# You can see my channel at https://thingspeak.com/channels/41518

import httplib, urllib
import time
#sleep = 1 # how many seconds to sleep between posts to the channel
key = 'I7U7DH9MZJ536JLW'#'Put your Thingspeak Channel Key here'  # Thingspeak channel to update

#Report Raspberry Pi internal temperature to Thingspeak Channel
def thermometer():
    while True:
        #Calculate CPU temperature of Raspberry Pi in Degrees C
        RPM = int('1890')#open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3 # Get Raspberry Pi CPU temp
        SPEED = int('0')
        ACCELERATION= int('0')
        THROTTLE= int('68')
        params = urllib.urlencode({'field1': RPM, 'field2': SPEED, 'field3': ACCELERATION, 'field4': THROTTLE,  'key':key} )
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            #print RPM#temp
            print response.status, response.reason
            data = response.read()
            conn.close()
        except:
            print "connection failed"
        break
#sleep for desired amount of time
if __name__ == "__main__":
        while True:
                thermometer()
##                time.sleep(sleep)

