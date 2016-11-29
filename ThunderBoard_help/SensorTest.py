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
        cmd = 'char-write-cmd 0x%02x 0%x' % (handle, value)
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
        while True:
            try:
                pnum = self.con.expect('Notification handle = .*? \r', timeout=4)
            except pexpect.TIMEOUT:
                print "TIMEOUT exception!"
                break
            if pnum==0:
                after = self.con.after
                print after
                hxstr = after.split()[3:]
                print hxstr
                handle = long(float.fromhex(hxstr[0]))
                #try:
            #if True:
            #      self.cb[handle]([long(float.fromhex(n)) for n in hxstr[2:]])
                #except:
                #  print "Error in callback for %x" % handle
                #  print sys.argv[1]
            #    pass
            else:
                print "TIMEOUT!!"
        #pass

    def register_cb( self, handle, fn ):
        self.cb[handle]=fn;
        return

class SensorCallbacks:

    data = {}

    def __init__(self,addr):
        self.data['addr'] = addr

    def tmp006(self,v):
        objT = (v[1]<<8)+v[0]
        ambT = (v[3]<<8)+v[2]
        targetT = calcTmpTarget(objT, ambT)
        self.data['t006'] = targetT
        print "T006 %.1f" % targetT

    def accel(self,v):
        (xyz,mag) = calcAccel(v[0],v[1],v[2])
        self.data['accl'] = xyz
        print "ACCL", xyz

    def humidity(self, v):
        rawT = (v[1]<<8)+v[0]
        rawH = (v[3]<<8)+v[2]
        (t, rh) = calcHum(rawT, rawH)
        self.data['humd'] = [t, rh]
        print "HUMD %.1f" % rh

    def baro(self,v):
        global barometer
        global datalog
        rawT = (v[1]<<8)+v[0]
        rawP = (v[3]<<8)+v[2]
        (temp, pres) =  self.data['baro'] = barometer.calc(rawT, rawP)
        print "BARO", temp, pres
        self.data['time'] = long(time.time() * 1000);
        # The socket or output file might not be writeable
        # check with select so we don't block.
        (re,wr,ex) = select.select([],[datalog],[],0)
        if len(wr) > 0:
            datalog.write(json.dumps(self.data) + "\n")
            datalog.flush()
            pass

    def magnet(self,v):
        x = (v[1]<<8)+v[0]
        y = (v[3]<<8)+v[2]
        z = (v[5]<<8)+v[4]
        xyz = calcMagn(x, y, z)
        self.data['magn'] = xyz
        print "MAGN", xyz

    def gyro(self,v):
        print "GYRO", v
from importDials import ddial
import pexpect
import sys
import time
#ddial()
bluetooth_adr='00:0B:57:0C:24:23'
while True:
    try:
        print "[re]starting.."

        tag = SensorTag(bluetooth_adr)
        cbs = SensorCallbacks(bluetooth_adr)
        
        #tag.register_cb(0x25,cbs.tmp006)
        #tag.char_write_cmd(0x37,0x0100)
        while True:
            temp = tag.char_read_hnd(0x33)
            print temp[0]
            #dial = temp[0]
            #ddial()
            key = cv2.waitKey(1) & 0xFF

            # if the `q` key was pressed, break from the loop
            if key == ord("q"):
                break                            
        tag.notification_loop()
    except:
        pass


