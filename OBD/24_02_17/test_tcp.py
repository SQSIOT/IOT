import time
import os
import string
import serial

from at import conna

port= conna.port
gps_c= conna()
gps_c.conn()
##port = serial.Serial("/dev/ttyS0", baudrate= 9600, timeout=1)
port.flushOutput()
port.flushInput()
port.write('AT'+'\r\n')
time.sleep(2)
c = port.read(48)
print c
#################
port.flushOutput()
port.write('AT'+'\r\n')
time.sleep(2)
c = port.read(48)
#################
port.flushOutput()
port.write('AT+CSTT="www"'+'\r\n')
time.sleep(2)
c = port.read(48)
print c
#################
port.flushOutput()
port.write('AT+CIICR'+'\r\n')
time.sleep(2)
c = port.read(48)
################
port.flushOutput()
port.write('AT+CIFSR'+'\r\n')
time.sleep(2)
c = port.read(48)
print c
################

flap= 0 
while True:
    infi= gps_c.get_cor()
    print infi
    port.flushInput()
    port.flushOutput()
    port.write('AT+CIPSTART="TCP","api.thingspeak.com",80'+'\r\n')
    time.sleep(1)
    c = port.read(78)
    print c
    ###################
    port.flushInput()
    port.flushOutput()
    port.write('AT+CIPSEND= 120'+'\r\n')
    #time.sleep(2)
    c = port.read(58)
    print c
    if flap== 0:
        api_key= 'I7U7DH9MZJ536JLW'
        field1= '1000'
        field2= '20'
        field3= '0'
        field4= '68'
        flap=1
        port.write('GET https://api.thingspeak.com/update?api_key=%s&field1=%s&field2=%s&field3=%s&field4=%s'%(api_key,field1,field2,field3,field4)+'\r\n')
    else:
        api_key= 'GAFPJLKKFEAC3M1B'
        field1= '0'
        field2= '0'
        field3= '0'
        #field4= None
        port.write('GET https://api.thingspeak.com/update?api_key=%s&field1=%s&field2=%s&field3=%s'%(api_key,field1,field2,field3)+'\r\n')
        flap=0
    #################

    #port.write('GET https://api.thingspeak.com/update?api_key=GAFPJLKKFEAC3M1B&field1=0.0000&field2=0.0000&field3=0.0000'+'\r\n')
####    port.write('Host: api.thingspeak.com:80'+'\r\n')#www.tutorialspoint.com '+'^m^j')
##    port.write('\r\n')
##    time.sleep(2)
##    port.flushInput()
##    port.flushOutput()
    #port.write('AT+CIPTERM'+'\r\n')
    c = port.read(58)
    print c    
    ###################
##    port.flushInput()
##    port.flushOutput()
##    port.write('AT+CIPSTART="TCP","api.thingspeak.com",80'+'\r\n')
##    time.sleep(2)
    
    ####################
##    port.flushInput()
##    port.flushOutput()
##    port.write('AT+CIPSEND= 120'+'\r\n')
##    #time.sleep(2)
##    c = port.read(58)
##    print c
    #################
##    port.write('GET https://api.thingspeak.com/update?api_key=GAFPJLKKFEAC3M1B&field1=0.0000&field2=0.0000&field3=0.0000'+'\r\n')
##    port.write('\r\n')
##    time.sleep(2)
##    port.flushInput()
##    port.flushOutput()
##    port.write('AT+CIPCLOSE'+'\r\n')
##    port.write('Host: api.thingspeak.com:80'+'\r\n')#www.tutorialspoint.com '+'^m^j')
##    time.sleep(2)

#################
##port.flushInput()
##port.flushOutput()
#port.write('POST https://api.thingspeak.com/update.json HTTP/1.1'+'\r\n')#/cgi-bin/process.cgi HTTP/1.1 '+'^m^j')
######port.write('Connection:Keep-Alive'+'^m^j')
######port.write('api_key= I7U7DH9MZJ536JLW'+'\r\n')
######port.write('X-THINGSPEAKAPIKEY: I7U7DH9MZJ536JLW'+'^m^j')
##port.write('User-Agent: Mozilla/4.0'+'\r\n')#curl/7.45.0 '+'\r\n')
######port.write('Accept:*/* '+'^m^j')
###port.write('Accept:text/plain '+'\n')
######port.write('Content-typZZe:application/x-www-form-urlencoded '+'^m^j')
##port.write('Content-Type: text/xml; charset=utf-8'+'\r\n')#application/x-www-form-urlencoded '+'\n')
##port.write('Content-Length: 88'+'\r\n')
##port.write('Accept-Language: en-us'+'\r\n')
##port.write('Accept-Encoding: grip,deflate'+'\r\n')
###port.write('{"api_key":"I7U7DH9MZJ536JLW"&"field1":"0"&"field2":"0"&"field3":"0"&"field4":"66"}')#+'\r\n')
##port.write('<?xml version="1.0" encoding="utf-8"?>'+'\r\n')
##port.write('string xmlns="http://clearforest.com/">string</string>'+'\r\n')
##c=port.read(259)
##print c
################
#port.flushInput()
#port.flushOutput()
#port.write('POST /update?api_key=I7U7DH9MZJ536JLW&field4=20 HTTP/1.1 '+'\r\n')
#port.write('POST https://api.thingspeak.com/apps/thinghttp/send_request&api_key=HKUO8HMNBVHMGXFD&message=hello world'+'\r\n')
#port.write('GET https://api.thingspeak.com/update?api_key=I7U7DH9MZJ536JLW&field1=0'+'^m^j')
##port.write('POST https://api.thingspeak.com/update.json')
##port.write('&api_key=I7U7DH9MZJ536JLW')
#######port.write('field1=73&field2=0&field3=0&field4=13'+'\r\n')
##port.flushInput()
##port.flushOutput()
#port.write('Host: api.thingspeak.com '+'\r\n')
##port.flushInput()
##port.flushOutput()
#port.write('Connection: close')
##port.write('X-THINGSPEAKAPIKEY: I7U7DH9MZJ536JLW')
###port.write('User-Agent: curl/7.45.0 ')#+'\r\n')
##port.flushInput()
##port.flushOutput()
#port.write('Accept:*/* '+'\r\n')
##port.flushInput()
##port.flushOutput()
#port.write('User-Agent: Mozilla/4.0 (compatible; esp8266 Lua; Windows NT 5.1)'+'\r\n')#curl/7.45.0 '+'\r\n')
##port.flushInput()
##port.flushOutput()
#port.write('\r\n')
#c=port.read(259)
#print c
##port.write('Accept:text/plain ')#+'\r\n')
###port.write('Content-typZZe:application/x-www-form-urlencoded ')#+'\r\n')
##port.write('Content-Type: application/x-www-form-urlencoded ')#+'')
##port.write('Content-Length:9 ')#+'\r\n')
###port.write('{"api_key":"I7U7DH9MZJ536JLW"&"field1":"0"&"field2":"0"&"field3":"0"&"field4":"66"}')#+'\r\n')
##port.write('field1= 0')
##c=port.read(259)
##print c













