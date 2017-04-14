import MySQLdb
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer

class S(BaseHTTPRequestHandler):
    key = 'I7U7DH9MZJ536JLW'
    key2 = None
    stab= None
    LONGI= None
    LATI= None
    ALTI= None
    rpm= None
    speed= None
    accel= None
    throt= None
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("<html><body><h1>hi!</h1></body></html>")

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        self.wfile.write("<html><body><h1>POST!</h1></body></html>")
        content_lenth= int (self.headers['Content-Length'])
        post_data= self.rfile.read(content_lenth)
        self.stab= post_data.split("&")
        self.rpm= self.stab[3].split("=")
        self.speed= self.stab[1].split("=")
        self.accel= self.stab[2].split("=")
        self.throt= self.stab[6].split("=")
        self.key2= self.stab[7].split("=")
        self.LATI= self.stab[4].split("=")
        self.LONGI= self.stab[5].split("=")
        self.cool= self.stab[0].split("=")
        self._set_headers()
        db= MySQLdb.connect("192.168.162.72","obd","obd","obd")
        cursor= db.cursor()
##        print self.stab
##        print self.accel
##        print self.cool
##        print self.throt
        print 'LONGI {}'.format(self.LONGI)
        print 'LATI {}'.format(self.LATI)
##        print 'ALTI {}'.format(self.ALTI)
        if(self.key == self.key2[1]) :    
            try:
                sql= 'INSERT INTO para(RPM,SPEED,COOLANT,THROT,ACCEL) VALUES(%s, %s, %s, %s, %s)'%(self.rpm[1],self.speed[1],self.cool[1],self.throt[1],self.accel[1])
                cursor.execute(sql)
                db.commit()
##                sql= 'INSERT INTO gps(longi,lati)VALUES(%s,%s)'%(self.LONGI[1],self.LATI[1])
##                cursor.execute(sql)
##                db.commit()
                
            except Exception as e: 
                print e# "Error: unable to fetch data"
    
            
            db.close()
        
def run(server_class=HTTPServer, handler_class=S, port=22):
    server_address = ('192.168.162.72', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
