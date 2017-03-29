#!/usr/bin/env python
__author__ = 'skunda'
# This program logs a Raspberry Pi's CPU temperature to a Thingspeak Channel
# To use, get a Thingspeak.com account, set up a channel, and capture the Channel Key at https://thingspeak.com/docs/tutorials/ 
# Then paste your channel ID in the code for the value of "key" below.
# Then run as sudo python pitemp.py (access to the CPU temp requires sudo access)
# You can see my channel at https://thingspeak.com/channels/41518
#import os
#os.system("sudo pon rnet")
import ssl
import httplib, urllib
import time
import random
#sleep = 1 # how many seconds to sleep between posts to the channel
key = 'I7U7DH9MZJ536JLW'#'Put your Thingspeak Channel Key here'  # Thingspeak channel to update

#Report Raspberry Pi internal temperature to Thingspeak Channel
def thermometer():
##    while True:
        #Calculate CPU temperature of Raspberry Pi in Degrees C
##        RPM = int('3500')#open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3 # Get Raspberry Pi CPU temp
##        SPEED = int('10')
##        ACCELERATION= int('50')
##        THROTTLE= int('76')
    LONGI= random.randint(73,75)
    LATI= random.randint(18,19)
    ALTI= random.randint(635,640)

    RPM= random.randint(1000,5000)
    SPEED= random.randint(0,1)
    ACCEL= random.randint(0,100)
    THROT= random.randint(0,100)
    params = urllib.urlencode({'field1': RPM, 'field2': SPEED, 'field3': ACCEL, 'field4': THROT, 'field5':key, 'field6':LONGI, 'field7':LATI})
        #print params
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        #print headers
##    conn = httplib.HTTPConnection("api.thingspeak.com:80")
##    conn = httplib.HTTPConnection("192.168.162.72:22")
##    conn = httplib.HTTPConnection("35.154.211.9:8083")
    conn = httplib.HTTPSConnection("clda.sqs.com:22")
##    conn = httplib.HTTPConnection("103.6.167.65:22")
##        try:
    conn.request("POST", "/update", params, headers)
    response = conn.getresponse()
        #print RPM#temp
    print response.status, response.reason
    data = response.read()
##    conn.close()
##        except:
##            print "connection failed"
##        break
#sleep for desired amount of time
if __name__ == "__main__":
    while True:
          thermometer()
##                time.sleep(sleep)

