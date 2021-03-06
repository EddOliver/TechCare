#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ibmiotf.application
import json
import RPi.GPIO as GPIO
import time

i=0

try:
  options = {
    "org": "YOUR_ORG",
    "id": "ANY_ID",
    "auth-method": "apikey",
    "auth-key": "YOUR_KEY",
    "auth-token": "YOUR_TOKEN",
    "clean-session": 1
  }
  clients = ibmiotf.application.Client(options)
except ibmiotf.ConnectionException  as e:
    ...

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.output(18,GPIO.LOW)

def myEventCallback(event):
      str = "%s event '%s' received from device [%s]: %s"
      print(str % (event.format, event.event, event.device, json.dumps(event.data)))
      if (event.event == "open" and event.device =="Tech:001"):
          print("YES")
          GPIO.output(18,GPIO.HIGH)
          time.sleep(5)
          GPIO.output(18,GPIO.LOW) 

clients.connect()
clients.deviceEventCallback = myEventCallback
clients.subscribeToDeviceEvents()
while 1:
    i=i
