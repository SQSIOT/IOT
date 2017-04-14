import serial
import string
import time
import threading
#import at
from at import conna

port_1= conna.port
gps_c= conna()
gps_c.conn()
from ddials import *
#######################################
port_1.flushOutput()
port_1.flushInput()
port_1.write('AT'+'\r\n')
time.sleep(2)
c = port_1.read(48)
print c
#################
port_1.flushOutput()
port_1.write('AT'+'\r\n')
time.sleep(2)
c = port_1.read(48)
#################
port_1.flushOutput()
port_1.write('AT+CSTT="www"'+'\r\n')
time.sleep(2)
c = port_1.read(48)
print c
#################
port_1.flushOutput()
port_1.write('AT+CIICR'+'\r\n')
time.sleep(2)
c = port_1.read(48)
################
port_1.flushOutput()
port_1.write('AT+CIFSR'+'\r\n')
time.sleep(2)
c = port_1.read(48)
print c
################

##################################################################
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
    except Exception as e:
        print e
        app= 'speed=='+ str(ls)
        return app

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

def temp_a(code):
    if len(code)>4:
        a= code.split(':',8)
        h= a[0]
        code= h[:len(h)-1]
    ls= 0000
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
def mil(code):
    code= hex_to_bitstring(code)
    #print 'code' ,code
    code= str(code[:1])
    code2= '0'
    try:
        if code[0]== code2:
            ii= 'OFF'
        else:
            ii= 'ON'
        app= 'mil=='+str(ii)
        return app
    except:
        ii= 'OFF'
        app= 'mil=='+str(ii)
        return app

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
    VAR_vin2= 'Waiting...'
    VAR_vin1= 0
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

    def sec_to_min(self, code):
        VAR_sec_to_min=0
        self.VAR_sec_to_min0= self.VAR_sec_to_min1
        self.VAR_sec_to_min1= self.VAR_sec_to_min2
        try:
            code = hex_to_int(code)
            code=  code / 60
            if (code)!=0:
                self.VAR_sec_to_min2 = code
                if self.VAR_sec_to_min2== self.VAR_sec_to_min1: 
                    return self.VAR_sec_to_min2

                elif self.VAR_sec_to_min2== self.VAR_sec_to_min0:
                    return self.VAR_sec_to_min2

                elif self.VAR_sec_to_min2== (self.VAR_sec_to_min1+1):
                    return self.VAR_sec_to_min2

                elif self.VAR_sec_to_min2== (self.VAR_sec_to_min0+1):
                    return self.VAR_sec_to_min2
        except:
            return VAR_sec_to_min1

    def vin(self,code):
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
            return app 
    
bbbb= abab()
############################
def read_buf_rv():
    repeat_count=1
    buffer= ""
    while 1:
        p = port.read(1)
        #print p
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
        buf= buffer 
        code = string.split(buf)
        code = string.join(code,"")
        #print code
        return code

############################
class ggppss:
    port_2= conna.port
    infi= ['00.00.0000','00:00','0000','0000','0000']
    ccc= conna()
    ccc.conn()
    def pain_gps(self):      
        date_1_p= 'DATE:'
        dtext1(date_1_p,850,80,80,20)
        time_1_p= 'TIME:'
        dtext1(time_1_p,850,102,80,20)
        st_4= 'Location Status:'
        dtext1(st_4,850,420,160,20)
        dtext1('LONGITUDE:',850,442,120,20)
        lati_p= 'LATITUDE:'
        dtext1(lati_p,850,462,120,20)
        longi_p= 'ALTITUDE:'
        dtext1(longi_p,850,482,120,20)
    def pain_gps_1(self):
        self.infi= self.ccc.get_cor()
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
        self.port_2.flushInput()
        self.port_2.flushOutput()
        self.port_2.write('AT+CIPSTART="TCP","api.thingspeak.com",80'+'\r\n')
        time.sleep(0.5)
        self.port_2.flushInput()
        self.port_2.flushOutput()
        self.port_2.write('AT+CIPSEND= 120'+'\r\n')
        time.sleep(0.5)
        self.port_2.write('GET https://api.thingspeak.com/update?api_key=GAFPJLKKFEAC3M1B&field1=%s&field2=%s&field3=%s'%(self.infi[2],self.infi[3],self.infi[4])+'\r\n')
gps_1= ggppss()

############################
st_1= 'Vehicle Status:'
dtext1(st_1,850,140,160,20)
mil_p= 'MIL:'
dtext1(mil_p,850,162,120,20)
bat_p= 'BATTERY VOLTAGE:'
dtext1(bat_p,850,182,160,20)
cool_1_p= 'COOLANT TEMP:'
dtext1(cool_1_p,850,202,160,20)
cool_1_p= 'INTAKE AIR TEMP:'
dtext1(cool_1_p,850,222,160,20)
st_2= 'Journey Status:'
dtext1(st_2,850,260,160,20)
journ_p= 'JOURNEY TIME:'
dtext1(journ_p,850,282,160,20)
dtext1('0 min',1050,282,160,20)
idle_p= 'IDLE TIME:'
dtext1(idle_p,850,302,120,20)
run_p= 'RUN TIME:'
dtext1(run_p,850,322,120,20)
dtext1('0 min',1050,322,120,20)
dtext1('0 min',1050,302,120,20)
st_3= 'Vehicle Information'
dtext1(st_3,850,360,180,20)
vin_p= 'VIN'
dtext1(vin_p,850,382,120,20)
dtext1('Waiting...',1050,202,120,20)
dtext1('Waiting...',1050,225,120,20)
dtext1('Waiting...',1050,162,120,20)
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
counter_c_a= 4
cool_f= False
jri_handle= 0

flap= 0
RPM='0'
SPEED='0'
ACCELERATION='0'
THROTTLE='0'

port_3= conna.port
while True:
    gps_1.pain_gps()
    gps_1.pain_gps_1()
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


            cmd= 'ATrv'
            write_buf(cmd)
            time.sleep(0.8)
            code_rv=read_buf_rv()
            code_rv_v= code_rv[4:]+ ' V'
            dtext1(code_rv_v,1050,182,120,20)
            #print code_rv[4:]
            
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
                    RPM= str(code[5:])
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
                    SPEED= str(code[7:])
                    #print code

            curr_time= time.time()
            lap_time= curr_time- start_time
            ch_speed= (acc_speed_2- acc_speed_1)
            mps_speed= ch_speed * (5/18)
            code_acce= ((ch_speed/lap_time))
            acc_speed_1= acc_speed_2
            #print 'code_acce= ' ,code_acce
            if (code_acce>= 0):
                ddial_acce(int(code_acce/10))
                ACCELERATION= str(code_acce/10)
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
                    THROTTLE= str(a_1)
####################################################################
            port_3.flushInput()
            port_3.flushOutput()
            port_3.write('AT+CIPSTART="TCP","api.thingspeak.com",80'+'\r\n')
            time.sleep(0.2)
            port_3.flushInput()
            port_3.flushOutput()
            port_3.write('AT+CIPSEND= 120'+'\r\n')
            time.sleep(0.2)
            port_3.write('GET https://api.thingspeak.com/update?api_key=I7U7DH9MZJ536JLW&field1=%s&field2=%s&field3=%s&field4=%s'%(RPM,SPEED,ACCELERATION,THROTTLE)+'\r\n')
####################################################################
                    
            ################
            counter_c_a= counter_c_a + 1 
            ################
            if (counter_c_a >3):
                cmd= 'at sp 6'
                write_buf(cmd)            
                time.sleep(0.1)
                ################
                cmd= '0105'
                write_buf(cmd)            
                time.sleep(0.2)
                code_cool= read_buf()
                if code_cool!= 'NO DATA':
                    code_cool_1=temp_c(code_cool)
                    if (int(code_cool_1[9:])>0) and (int(code_cool_1[9:])<300):
                        #print code_cool_1
                        dtext1(code_cool_1[9:12],1050,202,180,25)
                        cool_f= True
                ################
                cmd= 'at sp 6'
                write_buf(cmd)            
                time.sleep(0.1)
                ################
                cmd= '010F1'
                write_buf(cmd)            
                time.sleep(0.2)
                code_air= read_buf()
                if code_air!= 'NO DATA':
                    code_air_1=temp_a(code_air)
                    if(int(code_air_1[5:])>0) and (int(code_air_1[5:])<300):
                        #print code_air_1
                        dtext1(code_air_1[5:8],1050,225,180,25)
                        if cool_f== True: 
                            counter_c_a= 0
                            cool_f= False
                ################
    #MIL        ##################################################################
            
            if MIL_flag!= True:
                cmd= 'at sp 6'
                write_buf(cmd)            
                time.sleep(0.1)
                ################
                cmd= '01011'
                write_buf(cmd)            
                time.sleep(0.2)
                ################
                code_mil= read_buf()
                
                if code_mil!= 'NO DATA':
                    code_mil_1= mil(code_mil)
                    
                    mil_v_1 = str(code_mil_1[5:])
                    dtext1(mil_v_1,1050,162,120,20)
                    if (mil_v_1== 'OFF'):
                        MIL_flag= True
            

    #VIN        ##################################################################
            if VIN_flag == False:
                cmd= 'at sp 6'
                write_buf(cmd)          
                time.sleep(0.2)
                ################
                cmd='09025'
                write_buf(cmd)
                time.sleep(0.2)
                code_vin=read_buf()
                if code_vin!= 'NO DATA':
                    
                    code_vin_1=bbbb.vin(code_vin)
                    #print code_vin_1
                    if (code_vin_1[:5]== 'vin==') and len(code_vin_1[5:])== 17:
                        #print code_vin_1
                        vin_v= code_vin_1[5:]
                        dtext1(vin_v,1050,382,120,20)
                        if code_vin_1[5:] != 'Waiting...       ':
                            dtext1(vin_v,1050,382,220,22)
                            VIN_flag= True
                
            ################
            ################
    #Run Time        ##################################################################
            cmd= 'at sp 6'
            write_buf(cmd)
            time.sleep(0.1)
##            ################
            cmd= '011F'
            write_buf(cmd)            
            time.sleep(0.2)
##            ################
            code_run= read_buf()
##            print code_run
            if code_run!= 'NO DATA':
                code_run_1=bbbb.sec_to_min(code_run)
                #if (jri_handle <= code_run_1) and (code_run_1 >= 0):
                    #jri_handle= code_run_1
                if (code_run_1<= 45) and (code_run_1 != None):
                    runt_v= str(code_run_1) + ' min' 
                    dtext1(str(runt_v),1050,282,120,20)
                    j_time= code_run_1
                    if (acc_speed_2==  0)and (j_time> i_time): 
                        i_time= j_time- r_time
                        i_time_v= str(i_time)+ ' min' 
                        dtext1(i_time_v,1050,302,120,20)

                    elif (acc_speed_2!=  0)and (j_time> r_time):
                        r_time= j_time- i_time
                        r_time_v=str(r_time)+ ' min' 
                        dtext1(r_time_v,1050,322,120,20)
                        
                    l_j_time= j_time
                    if (j_time< l_j_time):
                        j_time= 0
                        r_time= 0
                        i_time= 0
                        l_j_time=0
            ##################################################
    except:
        continue
