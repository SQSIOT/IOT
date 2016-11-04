
 #!/usr/bin/env python


import serial
import string
import time
from math import ceil
from datetime import datetime
import ddials
from ddials import ddial_rpm
from ddials import ddial_temp
from ddials import ddial_mph
from ddials import ddial_fuel
import obd_sensors 

from obd_sensors import hex_to_int

GET_DTC_COMMAND   = "03"
CLEAR_DTC_COMMAND = "04"
GET_FREEZE_DTC_COMMAND = "07"

from debugEvent import debug_display

#__________________________________________________________________________
def decrypt_dtc_code(code):
    """Returns the 5-digit DTC code from hex encoding"""
    dtc = []
    current = code
    for i in range(0,3):
        if len(current)<4:
            raise "Tried to decode bad DTC: %s" % code

        tc = obd_sensors.hex_to_int(current[0]) #typecode
        tc = tc >> 2
        if   tc == 0:
            type = "P"
        elif tc == 1:
            type = "C"
        elif tc == 2:
            type = "B"
        elif tc == 3:
            type = "U"
        else:
            raise tc

        dig1 = str(obd_sensors.hex_to_int(current[0]) & 3)
        dig2 = str(obd_sensors.hex_to_int(current[1]))
        dig3 = str(obd_sensors.hex_to_int(current[2]))
        dig4 = str(obd_sensors.hex_to_int(current[3]))
        dtc.append(type+dig1+dig2+dig3+dig4)
        current = current[4:]
    #print "decrypt_dtc_code dtc= " ,dtc
    return dtc
#__________________________________________________________________________

class OBDPort:
     """ OBDPort abstracts all communication with OBD-II device."""
     def __init__(self,portnum,_notify_window,SERTIMEOUT,RECONNATTEMPTS):
         """Initializes port by resetting device and gettings supported PIDs. """
         # These should really be set by the user.
         baud     = 38400
         databits = 8
         par      = serial.PARITY_NONE  # parity
         sb       = 1                   # stop bits
         to       = SERTIMEOUT
         self.ELMver = "Unknown"
         self.State = 1 #state SERIAL is 1 connected, 0 disconnected (connection failed)
         self.port = None
         
         self._notify_window=_notify_window
         debug_display(self._notify_window, 1, "Opening interface (serial port)")

         try:
             self.port = serial.Serial(portnum,baud, \
             parity = par, stopbits = sb, bytesize = databits,timeout = to)
             
         except serial.SerialException as e:
             print e
             self.State = 0
             return None
             
         debug_display(self._notify_window, 1, "Interface successfully " + self.port.portstr + " opened")
         debug_display(self._notify_window, 1, "Connecting to ECU...")
         
         try:
            self.send_command("atz")   # initialize
            time.sleep(1)
         except serial.SerialException:
            self.State = 0
            return None
            
         self.ELMver = self.get_result()
         if(self.ELMver is None):
            self.State = 0
            return None
         
         debug_display(self._notify_window, 2, "atz response:" + self.ELMver)
         self.send_command("ate0")  # echo off
         debug_display(self._notify_window, 2, "ate0 response:" + self.get_result())
         self.send_command("0100")
         ready = self.get_result()
         
         if(ready is None):
            self.State = 0
            return None
            
         debug_display(self._notify_window, 2, "0100 response:" + ready)
         return None
              
     def close(self):
         """ Resets device and closes all associated filehandles"""
         
         if (self.port!= None) and self.State==1:
            self.send_command("atz")
            self.port.close()
         
         self.port = None
         self.ELMver = "Unknown"

     def send_command(self, cmd):
         """Internal use only: not a public interface"""
         if self.port:
             self.port.flushOutput()
             self.port.flushInput()
             for c in cmd:
                 self.port.write(c)
             self.port.write("\r\n")
             #debug_display(self._notify_window, 3, "Send command:" + cmd)

     def interpret_result(self,code):
         """Internal use only: not a public interface"""
         # Code will be the string returned from the device.
         # It should look something like this:
         # '41 11 0 0\r\r'
         
         # 9 seems to be the length of the shortest valid response
         if len(code) < 7:
             #raise Exception("BogusCode")
             print "boguscode?"+code
         
         # get the first thing returned, echo should be off
         code = string.split(code, "\r")
         code = code[0]
         
         #remove whitespace
         code = string.split(code)
         code = string.join(code, "")
         
         #cables can behave differently 
         if code[:6] == "NODATA": # there is no such sensor
             return "NODATA"
             
         # first 4 characters are code from ELM
         code = code[4:]
         return code
     def sen_data(self,code):
         #if code[:6] == "NODATA": # there is no such sensor
          #   return "NODATA"
             
         code = code[:5]
         #print 'code= ',code
         oc= '41 0C'
         o5= '41 05'
         od= '41 0D'
         tf= '41 0F'
         #print 'p= ',oc
         if oc == code:
             #print 'got the code rpm'
             return "rpm"
         elif o5 == code:
             #print 'got the code temp'
             return "temp"
         elif od == code:
             #print 'got the code mph'
             return "mph"
         elif tf == code:
             #print 'got the code mph'
             return "fuel"
            
         else:
             #print 'code failed'
             return False
            
     def get_result(self):
         """Internal use only: not a public interface"""
         #time.sleep(0.01)
         repeat_count = 0
         if self.port is not None:
             buffer = ""
             while 1:
                 c = self.port.read(1)
                 #print "c in get_result =" ,c
                 if len(c) == 0:
                    if(repeat_count == 5):
                        break
                    #print "Got nothing\n"
                    repeat_count = repeat_count + 1
                    continue
                    
                 if c == '\r':
                    continue
                    
                 if c == ">":
                    break;
                     
                 if buffer != "" or c != ">": #if something is in buffer, add everything
                    buffer = buffer + c
                 #print "get_result buffer= " , buffer
             #debug_display(self._notify_window, 3, "Get result:" + buffer)
             if(buffer == ""):
                return None
             return buffer
         else:
            debug_display(self._notify_window, 3, "NO self.port!")
         return None

     # get sensor value from command
     def get_sensor_value(self,sensor):
         """Internal use only: not a public interface"""
         cmd = sensor.cmd
         self.send_command(cmd)
         data = self.get_result()
         #print 'data 1=' ,data
         true= self.sen_data(data)
         
         if data:
             data = self.interpret_result(data)
             #print 'data 2=' ,data
             if data != "NODATA":
                 if data != "#":
                     data = sensor.value(data)
                     if true== "rpm":
                         dial_1= data
                         ddial_rpm(dial_1)
                         #print 'data 3=' ,data
                     if true== "temp":
                         dial_2= data
                         ddial_temp(dial_2)
                     if true== "mph":
                         dial_3= data
                         ddial_mph(dial_3)
                     if true== "fuel":
                         dial_4= data
                         ddial_fuel(dial_4)


         else:
             return "NORESPONSE"
         if data != "#":
             #print "data =" ,data
             return data
         else:
             return "NORESPONSE"
         


     # return string of sensor name and value from sensor index
     def sensor(self , sensor_index):
         """Returns 3-tuple of given sensors. 3-tuple consists of
         (Sensor Name (string), Sensor Value (string), Sensor Unit (string) ) """
         sensor = obd_sensors.SENSORS[sensor_index]
         #print "sensor() sensor= " ,sensor
         r = self.get_sensor_value(sensor)
         #print 'sensor r=' ,r
         return (sensor.name,r, sensor.unit)

     def sensor_names(self):
         """Internal use only: not a public interface"""
         names = []
         for s in obd_sensors.SENSORS:
             names.append(s.name)
         return names
         
     def get_tests_MIL(self):
         statusText=["Unsupported","Supported - Completed","Unsupported","Supported - Incompleted"]
         
         statusRes = self.sensor(1)[1] #GET values
         #print "get_tests_MIL() statusRes = " ,statusRes
         statusTrans = [] #translate values to text
         
         statusTrans.append(str(statusRes[0])) #DTCs
         
         if statusRes[1]==0: #MIL
            statusTrans.append("Off")
         else:
            statusTrans.append("On")
         if statusRes != "NODATA":  
             for i in range(2,len(statusRes)): #Tests
                  statusTrans.append(statusText[statusRes[i]]) 
         
         return statusTrans
          
     #
     # fixme: j1979 specifies that the program should poll until the number
     # of returned DTCs matches the number indicated by a call to PID 01
     #
     def get_dtc(self):
          """Returns a list of all pending DTC codes. Each element consists of
          a 2-tuple: (DTC code (string), Code description (string) )"""
          dtcLetters = ["P", "C", "B", "U"]
          r = self.sensor(1)[1] #data
          #print 'inside get_dtc r =' ,r
          ##for i in range(0, len(r)):
              ##r1 = str.join(r[i])
          ##print "my_r1= " +r1
          ##r2 = int(r1,2)
          dtcNumber = r[0]
          #print 'dtcNumber = ' ,dtcNumber
          mil = r[1]
          DTCCodes = []
          
          
          #print "Number of stored DTC:" + str(dtcNumber) + " MIL: " + str(mil)
          # get all DTC, 3 per mesg response
          if r != "NODATA":
              for i in range(0, ((dtcNumber+ 2)/3)):
                self.send_command(GET_DTC_COMMAND)
                res = self.get_result()
                #print "DTC result: " + res
                for i in range(0, 3):
                    val1 = 2#hex_to_int(res[3+i*6:5+i*6])
                    #print "get_dtc() readmod 6 val1= " ,val1
                    val2 = 141#hex_to_int(res[6+i*6:8+i*6]) #get DTC codes from response (3 DTC each 2 bytes)
                    #print "get_dtc() readmod 6 val2= " ,val2
                    val  = (val1<<8)+val2 #DTC val as int
                
                    if val==0: #skip fill of last packet
                      break
                   
                    #DTCStr=dtcLetters[(val&0xC000)>14]+str((val&0x3000)>>12)+str((val&0x0f00)>>8)+str((val&0x00f0)>>4)+str(val&0x000f)
                    DTCStr=dtcLetters[(val&0xC000)>>14]+str((val&0xf000)>>12)+str((val&0x0f00)>>8)+str((val&0x00f0)>>4)+str((val&0x000f)>>2)
                    DTCCodes.append(["Active",DTCStr])
                          
          #read mode 7
              self.send_command(GET_FREEZE_DTC_COMMAND)
              res = self.get_result()
          #print "freez_res = " ,res           
          #if res[:7] == "NODATA": #no freeze frame
          #DTCCodes = 0
              #print "DTCCodes = " ,DTCCodes
              return DTCCodes
          
              #print "DTC freeze result:" + res
              for i in range(0, 3):
                  val1 = 2#hex_to_int(res[3+i*6:5+i*6])
                  #print "get_det() readmod 7 val1= " ,val1
                  val2 = 141#hex_to_int(res[6+i*6:8+i*6]) #get DTC codes from response (3 DTC each 2 bytes)
                  #print "get_det() readmod 7 val2= " ,val2
                  val  = (val1<<8)+val2 #DTC val as int
                
                  if val==0: #skip fill of last packet
                    break
                   
                  #DTCStr=dtcLetters[(val&0xC000)>14]+str((val&0x3000)>>12)+str((val&0x0f00)>>8)+str((val&0x00f0)>>4)+str(val&0x000f)
                  DTCStr=dtcLetters[(val&0xC000)>>14]+str((val&0xf000)>>12)+str((val&0x0f00)>>8)+str((val&0x00f0)>>4)+str((val&0x000f)>>2)
                  #print "DTCStr in readmod 7= " ,DTCStr
                  DTCCodes.append(["Passive",DTCStr])
              #print "DTCCodes in readmod 7= " ,DTCCodes
              return DTCCodes
              
     def clear_dtc(self):
         """Clears all DTCs and freeze frame data"""
         self.send_command(CLEAR_DTC_COMMAND)     
         r = self.get_result()
         return r
     
     def log(self, sensor_index, filename): 
          file = open(filename, "w")
          start_time = time.time() 
          if file:
               data = self.sensor(sensor_index)
               file.write("%s     \t%s(%s)\n" % \
                         ("Time", string.strip(data[0]), data[2])) 
               while 1:
                    now = time.time()
                    data = self.sensor(sensor_index)
                    line = "%.6f,\t%s\n" % (now - start_time, data[1])
                    file.write(line)
                    file.flush()
          
