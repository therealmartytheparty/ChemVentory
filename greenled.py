#this code will be used to light up green leds
#only test code becuse we watnt to use multiplexing in this 
from gpiozero import LED
from time import sleep

led = LED(14)
led1 = LED(15)
led2 = LED(18)
led3 = LED(23)

while True:
    led.on()
    led1.on()
    led2.on()
    led3.on()
    sleep(3)
    led.off()
    led1.off()
    led2.off()
    led3.off()
    sleep(3)
    
