import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
#for the first shift regiser 
data1 = 4
latch1 = 5
clock1 = 6
#for the second shift register
data2 = 17
latch2 = 22
clock2 = 27
#for the third shift regiser 
data3 = 8
latch3 = 23
clock3 = 24
#for the fourth shift register
data4 = 13
latch4 = 19
clock4 = 16

GPIO.setwarnings(False)

GPIO.setup(data1, GPIO.OUT)
GPIO.setup(latch1, GPIO.OUT)
GPIO.setup(clock1,GPIO.OUT)
GPIO.setup(data2,GPIO.OUT)
GPIO.setup(latch2,GPIO.OUT)
GPIO.setup(clock2,GPIO.OUT)

GPIO.setup(data3, GPIO.OUT)
GPIO.setup(latch3, GPIO.OUT)
GPIO.setup(clock3,GPIO.OUT)
GPIO.setup(data4,GPIO.OUT)
GPIO.setup(latch4,GPIO.OUT)
GPIO.setup(clock4,GPIO.OUT)
#for the first shift register
def shiftout1(byte1):
    GPIO.output(latch1,0)
    for x in range(8):
        GPIO.output(data1, 0x80 & (byte1 << x))
        GPIO.output(clock1,1)
        GPIO.output(clock1,0)
    GPIO.output(latch1,1)
#for the second shift register
def shiftout2(byte2):
    GPIO.output(latch2,0)
    for x in range(8):
        GPIO.output(data2, 0x80 & (byte2 << x))
        GPIO.output(clock2,1)
        GPIO.output(clock2,0)
    GPIO.output(clock2,1)
#for the third shift register
def shiftout3(byte3):
    GPIO.output(latch3,0)
    for x in range(8):
        GPIO.output(data3, 0x80 & (byte3 << x))
        GPIO.output(clock3,1)
        GPIO.output(clock3,0)
    GPIO.output(latch3,1)
#for the fourth shift register
def shiftout4(byte4):
    GPIO.output(latch4,0)
    for x in range(8):
        GPIO.output(data4, 0x80 & (byte4 << x))
        GPIO.output(clock4,1)
        GPIO.output(clock4,0)
    GPIO.output(clock4,1)
#for x in range(255):

while True:
    y = 2
    x = 256
    print(y)
    shiftout1(y)
    shiftout2(x)
    shiftout3(x)
    shiftout4(x)
    time.sleep(100)
