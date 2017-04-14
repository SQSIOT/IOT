import httplib, urllib
import ssl
key = 'I7U7DH9MZJ536JLW'
#######################
import serial
import string
import time
import threading

portnum= '/dev/rfcomm0'
baud     = 38400
databits = 8
par      = serial.PARITY_NONE  
sb       = 1
to       = 1
State = 1 
port = None

port = serial.Serial(portnum,baud, \
            parity = par, stopbits = sb, bytesize = databits,timeout = to)


########################
def write_buf(cmd):
    port.flushInput()
    port.flushOutput()
    #time.sleep(0.5)
    for c in cmd:
        port.write(c)
    port.write("\r\n")
    
    
def read_buf():
    repeat_count=1
    buffer= ""
    while 1:
        p = port.read(1)
        if len(p) == 0:
            if(repeat_count == 5):
                continue
            repeat_count = repeat_count + 1
            continue
        if p == '\r':
            continue
            
        if p == ">":
            break;
             
        if buffer != "" or p != ">": 
            buffer = buffer + p
    #print buffer
    port.flushInput()
    port.flushOutput()
    if buffer[4:] == 'NO DATA':
        return 'NO DATA'
    else:
##        buf= buffer [10:]
        buf= buffer [1:]
        code = string.split(buf)
        code = string.join(code,"")
        #print code
        return code
#########################
def hex_to_int(str):
    ls= 0
    try:
        i = eval("0x" + str, {}, {})
        return i
    except:
        return ls

def rpm(code):
    ls= 0
    if len(code)>=7:
        a= code.split(':',8)
        h= a[0]
        code= h[:len(h)-1]
        #print 'modified rpm=> ',code
    try:    
        code = hex_to_int(code)
        ls= code/4
        app= 'rpm=='+ str(ls)
        return app
    except:
        app= 'rpm=='+ str(ls)
        return app
########################
def speed(code):
    ls= 0
    if len(code)>4:
        a= code.split(':',8)
        h= a[0]
        code= h[:len(h)-1]
        #print 'modified speed=> ',code
    try:
        code = hex_to_int(code)
        ls= code
        app= 'speed=='+ str(ls)
        return app
    except Exception as e:
        print e
        app= 'speed=='+ str(ls)
        return app
########################
def temp_c(code):
    if len(code)>4:
        a= code.split(':',8)
        h= a[0]
        code= h[:len(h)-1]
    ls= 0000
    try:
        code = hex_to_int(code)
        c = code - 40 
        ls= 32 + (9 * c / 5)
        #print ls
        app= 'coolant=='+ str(ls)
        return app 
    except:
        app= 'coolant=='+ str(ls)
        return app 
########################
def throttle_pos(code):
    ls= 0
    if len(code)>=7:
        a= code.split(':',8)
        h= a[0]
        code= h[:len(h)-1]
        #print 'modified rpm=> ',code
    try:
        code = hex_to_int(code)
        aa= (code * 100.0) / 255.0
        app= 'thro=='+ str(aa)
        #print app
        return app
    except:
        app= 'thro=='+ str(ls)
        return app

########################
def hex_to_bitstring(str):
    bitstring = ""
    try:
        for i in str:
            if type(i) == type(''): 
                v = eval("0x%s" % i)
                if v & 8 :
                    bitstring += '1'
                else:
                    bitstring += '0'
                if v & 4:
                    bitstring += '1'
                else:
                    bitstring += '0'
                if v & 2:
                    bitstring += '1'
                else:
                    bitstring += '0'
                if v & 1:
                    bitstring += '1'
                else:
                    bitstring += '0'                
        return bitstring
    except:
        return '0'

############################
first_run= False
RPM= ''
SPEED= ''
THROT= ''
ACCEL= ''
COOL= ''
LONGI= ''
LATI= ''

##import imp_serv
##ss= imp_serv.ssss()

while True:
    try:
##        hh= ss.s1()
##        LATI= hh[1]
##        LONGI= hh[0]

        if first_run == False:
            cmd= ' at sp 6'
            write_buf(cmd)
##            time.sleep(0.2)
            first_run= True
###############################################
        cmd= ' 01050C'#' 01050C0D'
        write_buf(cmd)
##            time.sleep(0.8)
        code_z=read_buf()
##        print code_z
        if code_z[6:10]== '4105':
            cool= temp_c((code_z[10:12]))
            print cool
            COOL= int(cool[9:])
        if code_z[12:14]== '0C':
            rpm_v= rpm((code_z[14:18]))
            RPM= int(rpm_v[5:])
            print rpm_v
###############################################
        cmd= ' 010D11'#' 01050C0D'
        write_buf(cmd)
##            time.sleep(0.8)
        code_z=read_buf()
##        print code_z
        if code_z[6:10]== '410D':
            speed_v= speed((code_z[10:12]))
            print speed_v
            SPEED= int(speed_v[7:])
        if code_z[12:14]== '11':
            throw_v= throttle_pos((code_z[14:16]))
            print throw_v
            THROT= (throw_v[6:8])
            
###############################################
        LONGI= ''
        LATI= ''
        import random
        ACCEL= random.randint(0,100)

        params = urllib.urlencode({'field1': RPM, 'field2': SPEED, 'field3': ACCEL, 'field4': THROT, 'field5':key, 'field6':LONGI,'field7':LATI, 'field8':COOL})
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        #conn = httplib.HTTPConnection("35.154.211.9:8083")
##       conn = httplib.HTTPConnection("103.6.167.65:8080")
        conn = httplib.HTTPSConnection("clda.sqs.com:22")
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print response.status, response.reason
        data = response.read()


###############################################
    except Exception as e:
        print e










