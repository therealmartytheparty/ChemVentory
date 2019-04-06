#!/usr/bin/env python
#================================================
#
#	This program is for SunFounder SuperKit for Rpi.
#
#	Extend use of 8 LED with 74HC595.
#
#	Change the	WhichLeds and sleeptime value under
#	loop() function to change LED mode and speed.
#
#=================================================

import RPi.GPIO as GPIO
import time

SDI   = 4 
RCLK  = 5
SRCLK = 6 
CLEAR = 13

#===============   LED Mode Defne ================
#	You can define yourself, in binay, and convert it to Hex 
#	8 bits a group, 0 means off, 1 means on
#	like : 0101 0101, means LED1, 3, 5, 7 are on.(from left to right)
#	and convert to 0x55.

LED1 = 0x01
LED2 = 0x02
LED3 = 0x04

LEDi = [0,0,0,0,0,0,0,0]
pos = 0x0 + posi
for index in range(0,7):
    LEDi[index] = 0x01
        
def print_msg():
    print ("Program is running...")
    print ("Please press Ctrl+C to end the program...")
    
#setups up all used pins to output and sets them to low
def setup():
    #Could use this code instead the BCM version
    #GPIO.setmode(GPIO.BOARD)
    #BOARD setmode have the pins abide by the physical pin location
    #BCM setmode abides by the green boxes and their GPIO reference
    #it might be better to use Board because the PI B versions have a different config between them
    #but the 
    GPIO.setmode(GPIO.BCM)    # Number GPIOs by its physical location
    GPIO.setup(SDI,GPIO.OUT)
    GPIO.setup(RCLK,GPIO.OUT)
    GPIO.setup(SRCLK,GPIO.OUT)
    GPIO.setup(CLEAR,GPIO.OUT)
    GPIO.output(SDI,GPIO.LOW)
    GPIO.output(RCLK,GPIO.LOW)
    GPIO.output(SRCLK,GPIO.LOW)
    GPIO.output(CLEAR,GPIO.HIGH)

def hc595_in(dat):
    for bit in range(0, 8):
        GPIO.output(SDI, 0x80 & (dat << bit))
        GPIO.output(SRCLK, GPIO.HIGH)
#it says on the datasheet that under 4.5 volts the frequency is supposed to be around 25MHz
# if you convert 25 MHz to seconds then it should be 4 *10^-8
#formula for time(period) = 1/ Frequency
        time.sleep(0.001)
        GPIO.output(SRCLK, GPIO.LOW)
def hc595_out():
    GPIO.output(RCLK, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(RCLK, GPIO.LOW)

def loop(pos):
    print(pos)
    WhichLeds = LEDi	# Change Mode, modes from LED0 to LED3sleeptime = 0.1		# Change speed, lower value, faster speed
    for i in range(0, len(WhichLeds)):
            hc595_in(WhichLeds[i])
            hc595_out()
            time.sleep(sleeptime)
    for i in range(len(WhichLeds)-1, -1, -1):
            hc595_in(WhichLeds[i])
            hc595_out()
            time.sleep(sleeptime)


def destroy():   # When program ending, the function is executed. 
    GPIO.cleanup()

if __name__ == '__main__': # Program starting from here
    print_msg()
    setup()
    try:
        pos = int(input("Please type in number to light up an LED"))
        loop(pos)  
    except KeyboardInterrupt:
        destroy()  
