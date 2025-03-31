import time
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(2,gpio.OUT) //pin2 is 5v

while True:
   gpio.output(2,True)
   time.sleep(1)
   gpio.output(2,False)
   time.sleep(1)
