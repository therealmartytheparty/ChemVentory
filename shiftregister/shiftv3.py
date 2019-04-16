import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

data = 4
latch = 5
clock = 6
GPIO.setwarnings(False)
GPIO.setup(data, GPIO.OUT)
GPIO.setup(latch, GPIO.OUT)
GPIO.setup(clock,GPIO.OUT)

def shiftout(byte):
    GPIO.output(latch,0)
    for x in range(8):
        GPIO.output(data, 0x80 & (byte << x))
        GPIO.output(clock,1)
        GPIO.output(clock,0)
    GPIO.output(latch,1)

#for x in range(255):
while True:
    y = 0b00110010
    x = 0b00100100
    print(y)
    p
    shiftout(y)
    time.sleep(100)
