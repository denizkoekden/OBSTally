#!/usr/bin/env python
# -*- coding: utf-8 -*-

#################################
#  Tally Lights for OBS-Studio  #
#  Using OBS-Websockets         #
#  (c) 2019 Deniz K. HTBAH e.V. #
#################################


import sys
import time

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.cleanup()

import logging
logging.basicConfig(level=logging.INFO)


sys.path.append('../')
from obswebsocket import obsws, events

host = "192.168.178.68"
port = 4444
password = "howky"

#
# Scene Config
#

scene1 = "HDMI1"
scene2 = "HDMI2"
scene3 = "HDMI3"
scene4 = "HDMI4"
scene5 = "Desktop+HDMI1"
scene6 = "Desktop+HDMI2"
scene7 = "Desktop+HDMI3"
scene8 = "Desktop+HDMI4"

#
# Configure Tallys
#

GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

def on_switch(message):
    obsscene = message.getSceneName()
    if obsscene == scene1:
       print ("Kamera 1 aktiv")
       GPIO.output(18, GPIO.HIGH)
       GPIO.output(23, GPIO.LOW)
       GPIO.output(24, GPIO.LOW)
       GPIO.output(25, GPIO.LOW)
    elif obsscene == scene2:
      print ("Kamera 2 aktiv")
      GPIO.output(18, GPIO.LOW)
      GPIO.output(23, GPIO.HIGH)
      GPIO.output(24, GPIO.LOW)
      GPIO.output(25, GPIO.LOW)
    elif obsscene == scene3:
     print ("Kamera 3 aktiv")
     GPIO.output(18, GPIO.LOW)
     GPIO.output(23, GPIO.LOW)
     GPIO.output(24, GPIO.HIGH)
     GPIO.output(25, GPIO.LOW)
    elif obsscene == scene4:
     print ("Kamera 4 aktiv")
     GPIO.output(18, GPIO.LOW)
     GPIO.output(23, GPIO.LOW)
     GPIO.output(24, GPIO.LOW)
     GPIO.output(25, GPIO.HIGH)
    else:
     print ("Szene ohne Tally:")
     print (obsscene)
     GPIO.output(18, GPIO.LOW)
     GPIO.output(23, GPIO.LOW)
     GPIO.output(24, GPIO.LOW)
     GPIO.output(25, GPIO.LOW)

ws = obsws(host, port, password)
ws.register(on_switch, events.SwitchScenes)
ws.connect()

try:
   while True:
    pass

except KeyboardInterrupt:
    pass
