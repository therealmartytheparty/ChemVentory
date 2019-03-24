import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
#GPIO.setwarnings(False)
GPIO.setup(8,GPIO.OUT)



GPIO.output(9,GPIO.HIGH)
time.sleep(3)
  
    

