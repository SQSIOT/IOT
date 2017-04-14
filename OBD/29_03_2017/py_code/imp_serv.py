###!/usr/bin/python           # This is server.py file
##
##import socket               # Import socket module
##
##s = socket.socket()         # Create a socket object
##host = '192.168.0.6'#socket.gethostname() # Get local machine name
##port = 12346                # Reserve a port for your service.
##s.bind((host, port))        # Bind to the port
##
##s.listen(5)                 # Now wait for client connection.
##c, addr = s.accept()     # Establish connection with client.
##while True:
##
##   print 'Got connection from', addr
##   c.send('Thank you for connecting')
##
##c.close()    

#!/usr/bin/python           # This is client.py file
import MySQLdb
from random import random
import random
import socket               # Import socket module


class ssss:
    s = socket.socket()         # Create a socket object
##    host = '192.168.43.123'#socket.gethostname() # Get local machine name
##    host = '192.168.163.248'
    host = '192.168.1.103'
    port = 1234              # Reserve a port for your service.


    # Open database connection
    ##db = MySQLdb.connect("192.168.162.72","obd","obd","obd")

    # prepare a cursor object using cursor() method
    ##cursor = db.cursor()
    s.connect((host, port))
    ack=True
    hh= ['0.0','0.0']
    def s1(self):
        #while True:
        try:
           tab= self.s.recv(21)
           self.s.send('ok')
           if (len(tab)>= 0) and (tab != 'error...'):
               stab= tab.split("&")
##               print stab
               return stab
               self.hh= stab
           # Execute the SQL command
    ##       sql= 'INSERT INTO para(RPM,SPEED)VALUES(%s,%s)'%(random.randint(1000,5000),random.randint(0,50))
    ##       cursor.execute(sql)
    ##       db.commit()
    ##       sql= 'INSERT INTO gps(longi,lati,alti)VALUES(%s,%s,%s)'%((float(stab[0])/100),(float(stab[1])/100),(float(stab[2])/100))
    ##       cursor.execute(sql)
    ##       db.commit()
        except:
           print "Error: unable to fecth data"        
    ##    print s.recv(6)+'\n'
    ##    print s.recv(7)+'\n'
    ##    print s.recv(7)+'\n'
    ##    print s.recv(7)+'n'

    s.close
##    db.close()

##
##ss= ssss()
##while True:
##    dd= ss.s1()
##    print dd
