

count = 0
s1 = 0
s2 = 0
from ddials import ddial_rpm
from ddials import ddial_mph
from ddials import dtext
from ddials import dtext1
from ddials import dtext2
#from ddials import dtext3
#from ddials import ddial
class SensorTag:

    def __init__( self, bluetooth_adr ):
        print "gatttool trying"
        self.con = pexpect.spawn('gatttool -b ' + bluetooth_adr + ' -I')
        self.con.expect('\[LE]>', timeout=600)
        print "Preparing to connect. You might need to press the side button..."
        self.con.sendline('connect')
        # test for success of connect
        self.con.expect('Connection successful.*\[LE]>')
        
        # Earlier versions of gatttool returned a different message.  Use this pattern -
        #self.con.expect('\[CON\].*>')
        self.cb = {}
        return

        #self.con.expect('\[CON\].*>')
        #self.cb = {}
        return

    def char_write_cmd( self, handle, value ):
        # The 0%x for value is VERY naughty!  Fix this!
        cmd = 'char-write-req 0x%02x 0%x' % (handle, value)
        print cmd
        self.con.sendline( cmd )
        return

    def char_read_hnd( self, handle ):
        self.con.sendline('char-read-hnd 0x%02x' % handle)
        self.con.expect('descriptor: .*? \r')
        after = self.con.after
        rval = after.split()[1:]
        return [long(float.fromhex(n)) for n in rval]

    # Notification handle = 0x0025 value: 9b ff 54 07
    def notification_loop( self ):
        
                        try:
                                pnum = self.con.expect('Notification handle = .*? \r', timeout=4)
                        except pexpect.TIMEOUT:
                                print "TIMEOUT exception!"
                                #break
                        if pnum==0:
                                after = self.con.after
                                #print after
                                hxstr = after.split()[3:]
                                #print hxstr
                                handle = long(float.fromhex(hxstr[0]))
                                #print handle
                                #return [long(float.fromhex(n)) for n in hxstr[2:]]
                                try:
                                        self.cb[handle]([long(float.fromhex(n)) for n in hxstr[2:]])
                                except:
                                        print "Error in callback for %x" % handle
                                        print sys.argv[1]
                                        pass
                        else:
                                print "TIMEOUT!!"

    def register_cb( self, handle, fn ):
                self.cb[handle]=fn;
                return

class SensorCallbacks:
    data = {}
    s= 0
    #def __init__(self,addr):
       # self.data['addr'] = addr
        #self.data['addr'] = addr
    count = 0

    def accel(self,v):
        cx= v[0]+(255*v[1])
        cy= v[2]+(255*v[3])
        cz= v[4]+(255*v[5])
        #ox = ((v[0]*360)/255)-180
        #ax = (v[1]*1000)/255
        #oy = ((v[2]*180)/255)-90
        #ay = (v[3]*1000)/255
        #oz = ((v[4]*360)/255)-180
        #az = 0.000
        #if(v[5]) > 0 :
         #   az = 1000*255/v[5]
         #   print ax
        #print ay
        #print az
        #print ox
        #print oy
        #print oz
        print 'Accel x:',cx
        #cx= str(cx)
        v1= str(v[0])
        dtext1(v1,390,380,88,28)
        print 'Accel y:',cy
        #cy= str(cy)
        v2= str(v[2])
        dtext1(v2,390,420,88,28)
        #dtext1(cy,,,,)
        print 'Accel z:',cz
        #cz= str(cz)
        v3= str(v[4])
        dtext1(v3,390,460,88,28)
        #dtext1(cz,,,,)
       

    def orien(self,v):
        cxx= v[0]#+(255*v[1])
        cyy= v[2]#+(255*v[3])
        czz= v[4]#+(255*v[5])
##        ox = ((v[0]*360)/255)-180
##        ax = (v[1]*1000)/255
##        oy = ((v[2]*180)/255)-90
##        ay = (v[3]*1000)/255
##        oz = ((v[4]*360)/255)-180
##        az = 0.000
##        if(v[5]) > 0 :
##            az = 1000*255/v[5]
##            print ax
##        print ay
##        print az
##        print ox
##        print oy
##        print oz
        print 'ori x:',cxx
        cxx= str(cxx)
        dtext1(cxx,390,540,88,28)
        print 'ori y:',cyy
        cyy= str(cyy)
        dtext1(cyy,390,580,88,28)
        #dtext1(cy,,,,)
        print 'ori z:',czz
        czz= str(czz)
        dtext1(czz,390,620,88,28)
        
        
    def csc(self,v):
        global count
        global s1
        global s2
        rev = v[1]+(255*v[2])+(255*255*v[3])+(255*255*255*v[4])
        
        if v[5] == s1 and v[6] == s2 :
            count += 1
            s1 = v[5]
            s2 = v[6]
            if count > 2:
                v[5] = 0
                v[6] = 0
        else:
            s1 = v[5]
            s2 = v[6]
            count = 0
        #print "rev ",rev
        dist = rev*3.24*3.14 * 0.01
        #print "dist ",dist
        d= "Battery = "
        h= "Distance = "
        humi= "Humidity = "
        temp= "Temperature = "
        light= "Light = "
        acce= "Accelerometer:"
        x="X ="
        y="Y ="
        z="Z ="
        ori= "Orientation:"
        xx="X ="
        yy="Y ="
        zz="Z ="
        dtext2(d,50,380)
        dtext2(h,50,420)
        dtext2(humi,50,460)
        dtext2(temp,50,500)
        dtext2(acce,350,340)
        dtext2(x,350,380)
        dtext2(y,350,420)
        dtext2(z,350,460)
        dtext2(ori,350,500)
        dtext2(xx,350,540)
        dtext2(yy,350,580)
        dtext2(zz,350,620)
        
        dist = str(dist)
        dtext1(dist,224,420,88,32)
        #print "dist = ",dist
        rpm = (((v[5]*255)+v[6])/(1024)) 
        ddial_rpm(rpm)
        #print "rpm ",rpm
        speed = rpm * 3*0.01 * 3.14  #* 60
        ddial_mph(speed)
        #time.sleep(1)
        #if s1== 
        #print "Speed ",speed
 
import pexpect
import sys
import time
bluetooth_adr='00:0B:57:0C:24:23'
while True:
        try:
                print "[re]starting.."
                #hell= "hell"
                #dtext(hell)
                tag = SensorTag(bluetooth_adr)
                cbs = SensorCallbacks()#bluetooth_adr)
                

                tag.register_cb(0x0019,cbs.csc)
                tag.char_write_cmd(0x1a,0x0100)

                tag.register_cb(0x0036,cbs.accel)
                tag.char_write_cmd(0x37,0x0100)

                tag.register_cb(0x0039,cbs.orien)
                tag.char_write_cmd(0x3a,0x0100)
                while True:
                        #temp = tag.char_read_hnd(0x19)
                        #print temp
                        Battery = tag.char_read_hnd(0x15)
                        Battery = str(Battery)
                        #print 'Battery: ' ,Battery
                        dtext1(Battery,224,380,88,28)
                        Humidity = tag.char_read_hnd(0x2c)
                        Humidity = ((Humidity[1]*255)+Humidity[0])/100
                        Humidity = str(Humidity)
                        #print 'Humidity: ' ,Humidity
                        dtext1(Humidity,224,460,88,28)
                        Temperature = tag.char_read_hnd(0x2e)
                        Temperature = ((Temperature[1]*255)+Temperature[0])/100
                        Temperature = str(Temperature)
                        #print 'Temperature: ' ,Temperature
                        dtext1(Temperature,224,500,88,28)
                        Light = tag.char_read_hnd(0x15)
                        Light = str(Light)
                        #print 'Light: ' ,Light
                        #dtext1(Light)
                        #dtext3(distt)
                        tag.notification_loop()
                        tag.notification_loop()
                        tag.notification_loop()
                        #print ox
                        #print oy
                        #print oz
                        ##print ax
                        #print ay
                        #print az
                        #print rev
                        #print rpm
        except:
                pass

        finally:
                #self.con.sendline('disconnect')
                sys.exit()
