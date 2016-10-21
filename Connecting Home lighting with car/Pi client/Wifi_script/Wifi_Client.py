import socket
from subprocess import call
import shlex
import time

msg = "Hello I'm Pi"
call(shlex.split('sh hello.sh'))

## Open the file with read only permit

## use readlines to read all lines in the file
## The variable "lines" is a list containing all lines

## close the file after reading the lines.
try:
 while True:
  f = open('Essid.txt')
  lines = f.read().strip()
  if lines == "IoT":
   print "IOT connected"
   s = socket.socket()        
   host = '192.168.163.150' 
   port = 10000               
   s.connect((host, port))
   s.send(msg)
   msg = s.rev(1024)
   print(msg)
   s.close()
  else:
   print "Not connected"
   time.sleep(10) 
except: 
 f.close()
