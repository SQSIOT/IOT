import serial
import os
import time
import string



class conna:
    port = serial.Serial("/dev/ttyS0", baudrate= 9600, timeout=1)
    port.flushOutput()
    port.flushInput()
    infi= []
    def conn(self):
        self.port.flushOutput()
        self.port.flushInput()
        self.port.write('AT'+'\r\n')        
        time.sleep(0.2)
        c = self.port.read(19)
        #print c[5:7]

        self.port.flushOutput()
        self.port.flushInput()
        self.port.write('AT+CGPSPWR=1'+'\r\n')# to turn on gps
        time.sleep(0.2)
        c = self.port.read(19)
        #print c[15:17]
        
        self.port.flushOutput()
        self.port.flushInput()
        self.port.write('AT+CGPSRST=1'+'\r\n')# gps mode reset parameter(0=cold,1=hot,2=warm)
        time.sleep(0.2)
        c = self.port.read(19)
        #print c[15:17]
        
        self.port.flushOutput()
        self.port.flushInput()
        self.port.write('AT+CGPSSTATUS?'+'\r\n')# to check the connection location
        time.sleep(0.2)
        c1 = self.port.read(48)
        
        #print c1[30:46]#'AT+CGPSSTATUS?=>',c1[30:46]
##
##        self.port.flushOutput()
##        self.port.flushInput()
##        self.port.write('AT+CGPSINF=0'+'\r\n')#(to get the data in mode 0)
##        c2 = self.port.read(100)
##        a= c2.split(',',9)
##        print a
##        
    def get_cor(self):
        self.port.flushOutput()
        self.port.flushInput()
        self.port.write('AT+CGPSSTATUS?'+'\r\n')# to check the connection location
        time.sleep(0.2)
        c1 = self.port.read(48)
        #print c1
        self.port.flushOutput()
        self.port.flushInput()
        self.port.write('AT+CGPSINF=0'+'\r\n')
        c2 = self.port.read(100)
        a= ['0','0','0','0','0','0','0','0','0']
        self.infi= ['0','0','0','0','0']
        try:
            a= c2.split(',',9)
            #[4]
            #a[4]= 
            if len(a[4])== 18:
                date= a[4]
            dat= '%s.%s.%s'%(date[6:8],date[4:6],date[0:4])
            #print 'Date=>',dat
            mint= 30+ int(date[10:12])
            hrr= 5+ int(date[8:10])
            sint= mint
            if mint > 60:
                sint= mint- 60
            if mint > 60:
                hrr=hrr+1
            clock= '%s:%s'%(str(hrr),str(sint))#,date[12:14])
            longi= '%s'%(a[1])
            lati= '%s'%(a[2])
            alti= '%s'%(a[3])
            self.infi= [dat,clock,longi,lati,alti]
            return self.infi
        
        except:
            return self.infi






        
