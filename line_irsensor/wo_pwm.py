
import RPi.GPIO as GPIO                      #Import GPIO library
import time                                  #Import time library

GPIO.setmode(GPIO.BCM)
Left_sensor = 6
Right_sensor = 13

GPIO.setup(Left_sensor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #Right sensor connection
GPIO.setup(Right_sensor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 

GPIO.setup(16, GPIO.OUT)    #motor A
GPIO.setup(20, GPIO.OUT)    #motor A

GPIO.setup(19, GPIO.OUT)    #motor B
GPIO.setup(26, GPIO.OUT)    #motor B

try:
    while True:
        i=GPIO.input(Left_sensor)                          #Reading output of right IR sensor
        j=GPIO.input(Right_sensor) 

        if i == 1 and j == 1:
            print "motor running forward"
            GPIO.output(16, GPIO.HIGH)  #Forward
            GPIO.output(20, GPIO.LOW)
            GPIO.output(19, GPIO.LOW)  #Forward
            GPIO.output(26, GPIO.HIGH)

            time.sleep(0.1)
        if i == 1 and j == 0:
            print "motor running forward"
            GPIO.output(16, GPIO.HIGH)  #Forward
            GPIO.output(20, GPIO.LOW)
            GPIO.output(19, GPIO.LOW)  #Forward
            GPIO.output(26, GPIO.LOW)

            time.sleep(0.1)
        if i == 0 and j == 1:
            print "motor running forward"
            GPIO.output(16, GPIO.LOW)  #Forward
            GPIO.output(20, GPIO.LOW)
            GPIO.output(19, GPIO.LOW)  #Forward
            GPIO.output(26, GPIO.HIGH)

            time.sleep(0.1)
        if i == 0 and j == 0:
            print "motor running forward"
            GPIO.output(16, GPIO.LOW)  #Forward
            GPIO.output(20, GPIO.LOW)
            GPIO.output(19, GPIO.LOW)  #Forward
            GPIO.output(26, GPIO.LOW)

            time.sleep(0.1)


              
    
finally:
    GPIO.cleanup()    
