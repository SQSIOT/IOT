from flask import Flask
from flask_ask import Ask, statement, convert_errors
import RPi.GPIO as GPIO
import logging

GPIO.setmode(GPIO.BCM)

app = Flask(__name__)
ask = Ask(app, '/')


logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.intent('GPIOControlIntent', mapping={'status': 'status', 'pin': 'pin'})
def gpio_control(status, pin):

##    try:
##        pinNum = int(pin)
##    except Exception as e:
##        return statement('Pin number not valid.')
##    print"Status is", status          Debugging purpose
##    print"pin is", pin                Debugging purpose
    if pin == 'AC':
        pinNum = 13
    if pin == 'TV':
        pinNum = 6
    if pin == 'kitchenlamp':
        pinNum = 19
    if pin == 'bedroomlamp':
        pinNum = 26



    GPIO.setup(pinNum, GPIO.OUT)

    if status in ['on', 'high']:    GPIO.output(pinNum, GPIO.LOW)
    if status in ['off', 'low']:    GPIO.output(pinNum, GPIO.HIGH)

    return statement('Turning pin {} {}'.format(pin, status))
if __name__=='__main__':
	port = 5000
	app.run(host='0.0.0.0', port=port)

GPIO.cleanup()
