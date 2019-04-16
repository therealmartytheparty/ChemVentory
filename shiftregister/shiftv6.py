import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#class that controls the 
class shiftnum:
    #function that lights up the LED
    def shiftout(byte,data,latch,clock):
        self.data = data
        self.latch = latch
        self.clock = clock
        GPIO.setwarnings(False)
        GPIO.setup(data, GPIO.OUT)
        GPIO.setuvp(latch, GPIO.OUT)
        GPIO.setup(clock,GPIO.OUT)
        #part that makes it work
        GPIO.output(latch,0)
        for x in range(8):
            GPIO.output(data, 0x80 & (byte << x))
            GPIO.output(clock,1)
            GPIO.output(clock,0)
        GPIO.output(latch,1)

#making 4 objects for 4 different shift registers
shift1 = shiftnum()
shift2 = shiftnum()
shift3 = shiftnum()
shift4 = shiftnum()

#making objects from the class shiftnum
while True:
    ledNum = 3
    print ledNum
    if ledNum <= 8:
        #pins for 1st shift register: d=4,l=5,c=6
        ledNum_1=int(ledNum)
        shift1.shiftout(ledNum_1,4,5)

    elif ledNum > 8 and ledNum <= 16:
        ledNum_2 = int(ledNum-8)
        #pins for 1st shift register: d=17,l= 22,c=27
        shift2.shiftout(ledNum_2,17,22,27)

    elif ledNum > 16 and ledNum <= 24:
        #pins for 3rd shift register: d=8,l=23,c=24
        ledNum_3 = int(ledNum-16)
        shift3.shiftout(ledNum_3,8,23,24)

    elif ledNum > 24 and ledNum <= 32:
        #pins for 4th shift register: d=13,l=19.c=16
        ledNum_4 = int(ledNum-24)
        shift4.shiftout(ledNum_4,13,19,16)

    else:
        print "not within the range 1-32"

    time.sleep(100)
