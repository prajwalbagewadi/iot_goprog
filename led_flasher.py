import time
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(18,gpio.OUT)
gpio.setup(17,gpio.OUT)
gpio.setup(22,gpio.IN,pull_up_down=gpio.PUD_UP)


while True:
   gpio.output(18,True)
   gpio.output(17,True)
   time.sleep(1)
   gpio.output(18,False)
   gpio.output(17,False)
   time.sleep(1)
   state = gpio.input(22)
   print(f"GPIO 22 STATE:{state}")
   time.sleep(1)
   
