import serial
import string
import time
import threading
import at
from ddials import *
##################################################################
class atThread(threading.Thread):
    def __init__(self):
        self.ccc= at.conna()
        self.ccc.conn()
        self.infi= ['00.00.0000','00:00','0000','0000','0000']
        threading.Thread.__init__(self)
        date_1_p= 'DATE:'
        dtext1(date_1_p,850,80,80,20)
        time_1_p= 'TIME:'
        dtext1(time_1_p,850,102,80,20)
        st_4= 'Location Status:'
        dtext1(st_4,850,420,80,20)
        dtext1('LONGITUDE:',850,442,80,20)
        lati_p= 'LATITUDE:'
        dtext1(lati_p,850,462,80,20)
        longi_p= 'ALTITUDE:'
        dtext1(longi_p,850,482,0,0)
    def run (self):
        while 1:
            self.infi= self.ccc.get_cor()
##            print self.infi
            date_1_v= self.infi[0]
            dtext1(date_1_v,1050,80,100,20)
            time_1_v= self.infi[1]
            dtext1(time_1_v,1050,102,100,20)
            longi_v= self.infi[2]#longi
            dtext1(longi_v,1050,442,120,20)
            lati_v= self.infi[3]#lati
            dtext1(lati_v,1050,462,120,20)
            alti_v= self.infi[4]#alti
            dtext1(alti_v,1050,482,120,20)
            
thread_at= atThread()
thread_at.start()

####################################################################

######################
portnum= '/dev/rfcomm0'
baud     = 38400
databits = 8
par      = serial.PARITY_NONE  
sb       = 1
to       = 2
State = 1 
port = None

port = serial.Serial(portnum,baud, \
            parity = par, stopbits = sb, bytesize = databits,timeout = to)
########################


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
        buf= buffer [10:]
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
    except:
        app= 'speed=='+ str(ls)
        return app

def temp_c(code):
    if len(code)>4:
        a= code.split(':',8)
        h= a[0]
        code= h[:len(h)-1]
        #print 'modified coolant=> ',code
    ls= 0
    try:
        code = hex_to_int(code)
        c = code - 40 
        ls= 32 + (9 * c / 5)
        app= 'coolant=='+ str(ls)
        return app 
    except:
        app= 'coolant=='+ str(ls)
        return app 

def temp_a(code):
    if len(code)>4:
        a= code.split(':',8)
        h= a[0]
        code= h[:len(h)-1]
        #print 'modified AIR=> ',code
    ls= 0
    try:
        code = hex_to_int(code)
        c = code - 40 
        ls= 32 + (9 * c / 5)
        app= 'AIR=='+ str(ls)
        return app 
    except:
        app= 'AIR=='+ str(ls)
        return app 
############################
def vin(code):
    self.VAR_vin2= 'Waiting...       '
    try:
        code = code[4:10]+code[12:26]+code[28:42]
        aa= code.decode("hex")
        if self.VAR_vin1 != 5:
            self.VAR_vin2= aa
            self.VAR_vin1=self.VAR_vin1 + 1
            app= 'vin=='+str(self.VAR_vin2)
            return app
        if self.VAR_vin1 == 3:
            app= 'vin=='+str(self.VAR_vin2)
            return app
    except:
        app= 'vin=='+str(self.VAR_vin2)
        return app ##MEXC15600FT084687
def mil(code):
    code= hex_to_bitstring(code)
    code2= '0'
    try:
        if code[0]== code2:
            ii= 'OFF'
        else:
            ii= 'ON'

        app= '5=='+str(ii)
        return app
    except:
        ii= 'OFF'
        app= '5=='+str(ii)
        return app

##def sec_to_min(code):
##    VAR_sec_to_min=0
##    ls=0
##    try:
##        code = hex_to_int(code)
##        #print code
##        VAR_sec_to_min = code
##        aa= code / 60
##        app= '7=='+ str(aa)
##        return app
##    except:
##        app= '7=='+ str(ls)
##        return app

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
class abab:
    VAR_sec_to_min0= 0
    VAR_sec_to_min1= 0
    VAR_sec_to_min2= 0
    def hex_to_int(self,str):
        ls= 0
        try:
            i = eval("0x" + str, {}, {})
            return i
        except:
            return ls

        def sec_to_min(self,code):
            try:
                code = hex_to_int(code)
                code= code/60
                self.VAR_sec_to_min0= self.VAR_sec_to_min1
                self.VAR_sec_to_min1= self.VAR_sec_to_min2
                if (code)!=0:
                    if (code > (self.VAR_sec_to_min2 + 1)) and (self.VAR_sec_to_min1 <= 4):
                        self.VAR_sec_to_min1 = self.VAR_sec_to_min1 + 1
                        app= 'runt=='+ str(self.VAR_sec_to_min2)
                        return app
                    else:
                        self.VAR_sec_to_min2 = code
                        self.VAR_sec_to_min1 = 0
                        app= 'runt=='+ str(code)
                        return app
            except:
                app= 'runt=='+ str(self.VAR_sec_to_min2)

bbbb= abab()
############################
st_1= 'Vehicle Status:'
dtext1(st_1,850,140,0,0)
mil_p= 'MIL:'
dtext1(mil_p,850,162,0,0)
bat_p= 'BATTERY VOLTAGE:'
dtext1(bat_p,850,182,0,0)
cool_1_p= 'COOLANT TEMP:'
dtext1(cool_1_p,850,202,0,0)
cool_1_p= 'INTAKE AIR TEMP:'
dtext1(cool_1_p,850,222,0,0)
st_2= 'Journey Status:'
dtext1(st_2,850,260,0,0)
journ_p= 'JOURNEY TIME:'
dtext1(journ_p,850,282,0,0)
idle_p= 'IDLE TIME:'
dtext1(idle_p,850,302,0,0)
run_p= 'RUN TIME:'
dtext1(run_p,850,322,0,0)
st_3= 'Vehicle Information'
dtext1(st_3,850,360,0,0)
vin_p= 'VIN'
dtext1(vin_p,850,382,0,0)

############################
MIL_flag= False
VIN_flag= False
first_run= False
start_time= 0
curr_time= 0
acc_speed_2=0
acc_speed_1=0
j_time= 0
r_time= 0
i_time= 0
l_j_time=0
while True:
    try:
        if first_run == False:
            cmd= 'atz'
            write_buf(cmd)
            time.sleep(0.8)
            code_z=read_buf()

            first_run= True

            cmd= '0100'
            write_buf(cmd)
            time.sleep(3)
            code_00= read_buf()
            #print code_00

        else:
    #rpm        ##################################################################
            cmd= 'at sp 6'
            write_buf(cmd)          
            time.sleep(0.1)
            ################
            cmd='010C'
            write_buf(cmd)
            time.sleep(0.2)
            ################
            code_rpm= read_buf()
            if code_rpm!= 'NO DATA':
                code=rpm(code_rpm)
                if(code[:5]=='rpm==' )and (int(code[5:]) > 500) and(int(code[5:]) < 5500):
                    ddial_rpm(int(code[5:]))
                    #print code
    #speed        ##################################################################
            cmd= 'at sp 6'
            write_buf(cmd)
            time.sleep(0.1)
            ################
            cmd= '010D'
            write_buf(cmd)
            time.sleep(0.2)
            ################
            code_speed= read_buf()
            if code_speed!= 'NO DATA':
                code=speed(code_speed)
                if (code[:7]=='speed==')and(int(code[7:]) >= 0) and(int(code[7:]) < 240):
                    acc_speed_2 = int(code[7:])
                    start_time= time.time()
                    ddial_mph(int(code[7:]))
                    #print code

            curr_time= time.time()
            lap_time= curr_time- start_time
            ch_speed= (acc_speed_2- acc_speed_1)
            mps_speed= ch_speed * (5/18)
            code_acce= ((ch_speed/lap_time))
            acc_speed_1= acc_speed_2
            print 'code_acce= ' ,code_acce
            if (code_acce>= 0):
                ddial_acce(int(code_acce))
            
    #Throttle        ##################################################################
            cmd= 'at sp 6'
            write_buf(cmd)            
            time.sleep(0.1)
            ################
            cmd= '01111'

            write_buf(cmd)            
            time.sleep(0.2)
            ################
            code_thro= read_buf()
            
            if code_thro!= 'NO DATA':
                code= throttle_pos(code_thro)
                hh= code[6:]
                a_1= int(hh[:2])
                if(code[:6]=='thro=='):
                    ddial_thro(a_1)
                    

    #VIN        ##################################################################
##            if VIN_flag == False:
##                cmd= 'at sp 6'
##                write_buf(cmd)          
##                time.sleep(0.2)
##                ################
##                cmd='09021'
##                write_buf(cmd)
##                time.sleep(0.2)
##                code_vin=read_buf()
##                if code_vin!= 'NO DATA':
##                    code_vin_1=vin(code_vin)
##                    if (code_vin_1[:5]== 'vin==') and len(code_vin_1[5:])== 17:
##                        print code_vin_1
##                        vin_v= code_vin_1[5:]
##                        dtext1(vin_v,1050,382,120,20)
##                        if code_vin_1[5:] != 'Waiting...       ':
##                            dtext1(vin_v,1050,382,120,20)
##                            VIN_flag= True
                
            ################


    #Run Time        ##################################################################
##            cmd= 'at sp 6'
##            write_buf(cmd)
##            time.sleep(0.1)
##            ################
##            cmd= '011F'
##            write_buf(cmd)            
##            time.sleep(0.2)
##            ################
##            code_run= read_buf()
##            if code_run!= 'NO DATA':
##                code=bbbb.sec_to_min(code_run)
##                if(code[:6]=='runt==')and(int(code[6:]) >= 0) and(int(code[6:]) < 300):
##                    dtext1(journ_v,1050,282,120,20)
##                    print code
##                    if (acc_speed_2==  0)and (j_time> i_time): 
##                        i_time= j_time- r_time
##                        dtext1(i_time,1050,302,120,20)
##
##                    elif (acc_speed_2!=  0)and (j_time> r_time):
##                        r_time= j_time- i_time
##                        dtext1(r_time,1050,322,120,20)
##                    l_j_time= j_time
##                    if (j_time< l_j_time):
##                        j_time= 0
##                        r_time= 0
##                        i_time= 0
##                        l_j_time=0
##


   #Acceleration        ##################################################################
##            cmd= 'at sp 6'
##            write_buf(cmd)
##            time.sleep(0.2)
            ################
##            cmd= '010F'
##            write_buf(cmd)            
##            time.sleep(0.2)
            ################
            #code_acce= read_buf()
            #if code_acce!= 'NO DATA':
##                code=temp_a(code_air)
##                if(code[:5]=='AIR==')and(int(code[5:]) >= 0) and(int(code[5:]) < 300):
##                    ddial_air(int(code[5:]))
##                    print code

            ##################################################
            ##################################################
    except:
        continue
