import serial
import os
import time
import string
#########AT
##port = serial.Serial("/dev/ttyS0", baudrate= 9600, timeout=1)
##port.flushOutput()
##port.flushInput()
##port.write('AT'+'\r\n')        
##c = port.read(19)
##print 'AT=>',c[5:7]
##time.sleep(1)
##
#########AT+CGPSPWR=1
##port = serial.Serial("/dev/ttyS0", baudrate= 9600, timeout=1)
##port.flushOutput()
##port.flushInput()
##port.write('AT+CGPSPWR=1'+'\r\n')        
##c = port.read(19)
##print 'AT+CGPSPWR=1=>',c[15:17]
##time.sleep(1)
##
#########AT+CGPSRST=0
##port = serial.Serial("/dev/ttyS0", baudrate= 9600, timeout=1)
##port.flushOutput()
##port.flushInput()
##port.write('AT+CGPSRST=0'+'\r\n')        
##c = port.read(19)
##print 'AT+CGPSRST=0=>',c[15:17]
##time.sleep(1)

#######AT+CGPSSTATUS?

port = serial.Serial("/dev/ttyS0", baudrate= 9600, timeout=1)
port.flushOutput()
port.flushInput()
port.write('AT+CGPSSTATUS?'+'\r\n')        
c = port.read(48)

print 'AT+CGPSSTATUS?=>',c[30:46]
time.sleep(1)

#######AT+CGPINF=0
port = serial.Serial("/dev/ttyS0", baudrate= 9600, timeout=1)
port.flushOutput()
port.flushInput()
port.write('AT+CGPSINF=0'+'\r\n')
c = port.read(100)
#print c
a= c.split(',',8)
print 'Longitude=> ',a[1]
print 'Latitude=> ',a[2]
print 'Altitude=> ',a[3]
#print 'Speed=>',a[7]
date= a[4]
#print date
#print 'AT+CGPSINF=0=>',c[30:94]
print 'Date=>%s.%s.%s'%(date[6:8],date[4:6],date[0:4])
mint= 30+int(date[10:12])
hrr=5+int(date[8:10])
sint= mint
if mint > 60:
    sint= mint- 60
if mint > 60:
    hrr+1
print 'Clock=>%s:%s:%s'%(str(hrr),str(sint),date[12:14])
time.sleep(1)

