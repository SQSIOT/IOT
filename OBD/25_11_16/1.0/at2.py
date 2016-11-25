import serial
import os
import time


available = []
for i in range(256):
    try:
        s = serial.Serial("/dev/ttyS"+str(i))
        available.append(str(s.port))
        s.close()   # explicit close 'cause of delayed GC in java
    except serial.SerialException:
        pass
print available
try:
    port = serial.Serial("/dev/ttyS0", baudrate= 9600, timeout=1)
    cmd = "AT+JE"
    if port:
        port.flushOutput()
        port.flushInput()
        #for c in cmd:
            #print c
        port.write('AT+JE'+'\r\n')
        print "send: " ,cmd
        port.write('\r\n')
        c = port.read(100)
        print 'c=',c[1:20]
        time.sleep(1)
    repeat_count = 0
    if port is not None:
        buffer = ""
        while 1:
            c = (port.read(10))
            #print "c in get_result =" ,c
            #if len(c) == 0:
                #if(repeat_count == 0):
                    #break
                #print "Got nothing\n"
                #repeat_count = repeat_count + 1
                #continue
            #if c == '\r':
                #print 'carry'
              #  continue
                    
            #if c == ">":
                #print '>'
               # break;
            #if buffer != "" or c != ">": #if something is in buffer, add everything
             #   buffer = buffer + c
              #  print "get_result buffer= " , buffer
                #port.flushInput()
             #debug_display(self._notify_window, 3, "Get result:" + buffer)
            #if(buffer == ""):
                #print None
            #print buffer
except serial.SerialException:
    print "fail"
    pass
