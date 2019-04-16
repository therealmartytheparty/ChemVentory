import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#function that lights up the LED
def shiftout(byte,data,latch,clock):
    GPIO.setwarnings(False)
    GPIO.setup(data, GPIO.OUT)
    GPIO.setup(latch, GPIO.OUT)
    GPIO.setup(clock,GPIO.OUT)
    #part that makes it work
    GPIO.output(latch,0)
    for x in range(8):
        GPIO.output(data, 0x80 & (byte << x))
        GPIO.output(clock,1)
        GPIO.output(clock,0)
    GPIO.output(latch,1)
    
while True:
    ledNum = 15
    print ledNum
    if ledNum <= 8:
        #pins for 1st shift register: d=4,l=5,c=6
        ledNum_1=int(ledNum)
        shiftout(ledNum_1,4,5,6)
    elif ledNum > 8 and ledNum <= 16:
        ledNum_2 = int(ledNum-8)
        #pins for 1st shift register: d=23,l= 24,c=25
        shiftout(ledNum_2,23,24,25)

    elif ledNum > 16 and ledNum <= 24:
        #pins for 3rd shift register: d=17,l=18,c=19
        ledNum_3 = int(ledNum-16)
        shiftout(ledNum_3,17,18,19)

    elif ledNum > 24 and ledNum <= 32:
        #pins for 4th shift register: d=13,l=19.c=16
        ledNum_4 = int(ledNum-24)
        shiftout(ledNum_4,13,19,16)

    else:
        print "not within the range 1-32"

    time.sleep(100)
