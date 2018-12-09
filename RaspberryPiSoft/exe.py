
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from threading import Thread
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.output(18,GPIO.LOW)
code = "1234"

def runA():
    while True:
        codein = input("Introduce the code:")
        if(code == codein):
            print("YES")
            GPIO.output(18,GPIO.HIGH)
            time.sleep(10)
            GPIO.output(18,GPIO.LOW)
        else:
            print("NO")
            GPIO.output(18,GPIO.LOW)
            
if __name__ == "__main__":
    t1 = Thread(target = runA)
    t1.setDaemon(True)
    t1.start()
    while True:
        pass
