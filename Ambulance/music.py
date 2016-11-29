#!/usr/bin/env python
# -*- coding: utf-8 -*-

path = '/home/pi/Desktop/Ambulance/siren.mp3'
from subprocess import Popen
import time

while True:
    omx = Popen(['omxplayer', path])
    time.sleep(11)
