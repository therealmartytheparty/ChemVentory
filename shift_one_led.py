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

SDI=4 #data going in 
CLK=6 #clock
LE= 5
CLEAR=13

#===============   LED Mode Defne ================
#	You can define yourself, in binay, and convert it to Hex 
#	8 bits a group, 0 means off, 1 means on
#	like : 0101 0101, means LED1, 3, 5, 7 are on.(from left to right)
#	and convert to 0x55.
LED1 = 0xff


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
    GPIO.setwarnings(False)
    GPIO.setup(SDI, GPIO.OUT)
    GPIO.setup(LE, GPIO.OUT)
    GPIO.setup(CLK, GPIO.OUT)
    GPIO.setup(CLEAR,GPIO.OUT)
    GPIO.output(SDI, GPIO.LOW)
    GPIO.output(CLK, GPIO.LOW)
    GPIO.output(LE, GPIO.LOW)
    GPIO.output(CLEAR, GPIO.HIGH)
    '''
def send_one():
     for bit in range(0,8):
        if byte_to_send & 0x01<<bit:
            GPIO.output(SDI,GPIO.HIGH)
        GPIO.output(CLK, GPIO.HIGH)
        GPIO.output(SDI, GPIO.LOW)
        time.sleep(0.00000004)
        GPIO.output(CLK, GPIO.LOW)
'''
def send_data(byte_to_send):
    for bit in range(0,8):
        #so this if statement will go high if there 
        if (byte_to_send & 0x01<<bit)!= 0: 
            print(bit)
            #print(byte_to_send & 0x01<<bit)#shifting logic 
            GPIO.output(SDI,GPIO.HIGH)
        GPIO.output(CLK, GPIO.HIGH)
        GPIO.output(SDI, GPIO.LOW)
        time.sleep(0.001)
        GPIO.output(CLK, GPIO.LOW)
        
#clear the LEDS
def clear():
    GPIO.output(CLEAR, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(CLEAR,GPIO.LOW)
    latch()
    

def latch():
    GPIO.output(LE, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(LE, GPIO.LOW)

def loop():
    WhichLeds = LED1	# Change Mode, modes from LED0 to LED3
    sleeptime = 0.5		# Change speed, lower value, faster speed
    while True:
        send_data(WhichLeds)
        latch() 
        time.sleep(sleeptime)
        '''
        send_data(WhichLeds[i]-1)
        latch()
        time.sleep(sleeptime)
        '''
                          
def destroy():   # When program ending, the function is executed. 
    GPIO.cleanup()

if __name__ == '__main__': # Program starting from here 
    print_msg()
    setup() 
    try:
        loop()
        clear()
    except KeyboardInterrupt:
        destroy()  
