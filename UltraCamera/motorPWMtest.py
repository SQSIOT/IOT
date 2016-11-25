import RPi.GPIO as GPIO                      #Import GPIO library
import time                                  #Import time library

GPIO.setmode(GPIO.BCM)                       #Set GPIO pin numbering

M1P = 16                                     #Motor 1 terminal F.
M1N = 20                                     #Motor 1 terminal R.
M2P = 26                                     #Motor 2 terminal F.
M2N = 19                                     #Motor 2 terminal R.

GPIO.setup(M1P,GPIO.OUT)
GPIO.setup(M1N,GPIO.OUT)
GPIO.setup(M2P,GPIO.OUT)
GPIO.setup(M2N,GPIO.OUT)

GPIO.output(M1P,GPIO.LOW)
GPIO.output(M1N,GPIO.LOW)
GPIO.output(M2P,GPIO.LOW)
GPIO.output(M2N,GPIO.LOW)

M1 = GPIO.PWM(M1P , 50)
M2 = GPIO.PWM(M2P , 50)

M1.start(0)
M2.start(0)

M1.ChangeDutyCycle(100)
M2.ChangeDutyCycle(100)

time.sleep(2)                   #sleep for 200ms

M1.ChangeDutyCycle(0)
M2.ChangeDutyCycle(0)

GPIO.cleanup()


