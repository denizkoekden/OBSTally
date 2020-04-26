#!/usr/bin/env python
# -*- coding: utf-8 -*-

#################################
#  Tally Lights for OBS-Studio  #
#  Using OBS-Websockets         #
#  (c) 2019 Deniz K. HTBAH e.V. #
#################################


import sys
import time
import xml.etree.ElementTree as ET

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.cleanup()

import logging
logging.basicConfig(level=logging.INFO)


sys.path.append('../')
from obswebsocket import obsws, events, requests

from gpiozero import LED

tree = ET.parse('tally.xml')
root = tree.getroot()
host = root[0].text
port = root[1].text
password  = root[2].text

#
# Scene Config
#
scene1 = root[3].text
scene2 = root[4].text
scene3 = root[5].text
scene4 = root[6].text

#
# Configure Tallys
#
pv_tally_1 = LED(root[7].text)
pgm_tally_1 = LED(root[8].text)
pv_tally_2 = LED(root[9].text)
pgm_tally_2 = LED(root[10].text)
pv_tally_3 = LED(root[11].text)
pgm_tally_3 = LED(root[12].text)
pv_tally_4 = LED(root[13].text)
pgm_tally_4 = LED(root[14].text)

#
# Set them to OFF (Inverted)
#

pv_tally_1.on()
pv_tally_2.on()
pv_tally_3.on()
pv_tally_4.on()
pgm_tally_1.on()
pgm_tally_2.on()
pgm_tally_3.on()
pgm_tally_4.on()


#
# Intialize all 
#

pv_tally_1.off()

time.sleep(0.5)

pv_tally_1.on()
pv_tally_2.off()

time.sleep(0.5)

pv_tally_2.on()
pv_tally_3.off()

time.sleep(0.5)

pv_tally_3.on()
pv_tally_4.off()

time.sleep(0.5)

pv_tally_4.on()
pgm_tally_1.off()

time.sleep(0.5)

pgm_tally_1.on()
pgm_tally_2.off()

time.sleep(0.5)

pgm_tally_2.on()
pgm_tally_3.off()

time.sleep(0.5)

pgm_tally_3.on()
pgm_tally_4.off()

time.sleep(0.5)

pgm_tally_4.on()
time.sleep(0.5)

#
# Set them to OFF (Inverted) once again
#

pv_tally_1.on()
pv_tally_2.on()
pv_tally_3.on()
pv_tally_4.on()
pgm_tally_1.on()
pgm_tally_2.on()
pgm_tally_3.on()
pgm_tally_4.on()

def on_switch(message):
    obsscene = message.getSceneName()
    if obsscene == scene1:
       print ("Kamera 1 aktiv")
       pgm_tally_1_on()
    elif obsscene == scene2:
      print ("Kamera 2 aktiv")
      pgm_tally_2_on()
    elif obsscene == scene3:
     print ("Kamera 3 aktiv")
     pgm_tally_3_on()
    elif obsscene == scene4:
     print ("Kamera 4 aktiv")
     pgm_tally_4_on()
    else:
     print ("Szene ohne Tally:")
     print (obsscene)

def on_preview(message):
    pv_scene = message.getSceneName()
    if pv_scene == scene1:
       print ("Kamera 1 Preview")
       pv_tally_1_on()
    elif pv_scene == scene2:
      print ("Kamera 2 Preview")
      pv_tally_2_on()
    elif pv_scene == scene3:
     print ("Kamera 3 Preview")
     pv_tally_3_on()
    elif pv_scene == scene4:
     print ("Kamera 4 Preview")
     pv_tally_4_on()
    else:
     print ("Szene ohne Tally:")
     print (pv_scene)

def pv_tally_1_on():
   pv_tally_1.off()
   pv_tally_2.on()
   pv_tally_3.on()
   pv_tally_4.on()
#   pgm_tally_1.on()
#  pgm_tally_2.on()
#   pgm_tally_3.on()
#   pgm_tally_4.on()
def pgm_tally_1_on():
   pgm_tally_1.off()
   pgm_tally_2.on()
   pgm_tally_3.on()
   pgm_tally_4.on()

def pv_tally_2_on():
   pv_tally_1.on()
   pv_tally_2.off()
   pv_tally_3.on()
   pv_tally_4.on()

def pgm_tally_2_on():
   pgm_tally_1.on()
   pgm_tally_2.off()
   pgm_tally_3.on()
   pgm_tally_4.on()

def pv_tally_3_on():
   pv_tally_1.on()
   pv_tally_2.on()
   pv_tally_3.off()
   pv_tally_4.on()

def pgm_tally_3_on():
   pgm_tally_1.on()
   pgm_tally_2.on()
   pgm_tally_3.off()
   pgm_tally_4.on()

def pv_tally_4_on():
   pv_tally_1.on()
   pv_tally_2.on()
   pv_tally_3.on()
   pv_tally_4.off()

def pgm_tally_4_on():
   pgm_tally_1.on()
   pgm_tally_2.on()
   pgm_tally_3.on()
   pgm_tally_4.off()

ws = obsws(host, port, password)
ws.register(on_switch, events.SwitchScenes)
ws.register(on_preview, events.PreviewSceneChanged)
ws.connect()

try:
   while True:
    pass

except KeyboardInterrupt:
    pass
