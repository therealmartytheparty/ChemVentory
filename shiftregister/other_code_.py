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

SDI   = 4  #pin 4 for data pin
RCLK  = 5  #pin 5 for the clock pin
SRCLK = 6  #pin 6 for the latch

#===============   LED Mode Defne ================
#	You can define yourself, in binay, and convert it to Hex 
#	8 bits a group, 0 means off, 1 means on
#	like : 0101 0101, means LED1, 3, 5, 7 are on.(from left to right)
#	and convert to 0x55.

LED0 = [0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80]	#original mode
LED1 = [0x01,0x03,0x07,0x0f,0x1f,0x3f,0x7f,0xff]	#blink mode 1
LED2 = [0x01,0x05,0x15,0x55,0xb5,0xf5,0xfb,0xff]	#blink mode 2
LED3 = [0x02,0x03,0x0b,0x0f,0x2f,0x3f,0xbf,0xff]	#blink mode 3
LED4 = [0x02,0x02,0x02,0x02,0x02,0x02,0x02,0x02]
LED5 = 0x05
#=================================================

def print_msg():
	print ("Program is running...")
	print ("Please press Ctrl+C to end the program...")

def setup():
	GPIO.setmode(GPIO.BCM)    # Number GPIOs by its physical location
	GPIO.setwarnings(False)
	GPIO.setup(SDI, GPIO.OUT)
	GPIO.setup(RCLK, GPIO.OUT)
	GPIO.setup(SRCLK, GPIO.OUT)
	GPIO.output(SDI, GPIO.LOW)
	GPIO.output(RCLK, GPIO.LOW)
	GPIO.output(SRCLK, GPIO.LOW)

#this puts in the bits into the shift register
def hc595_in(dat):
	#should change this from 8 to 16 for two shift 
	for bit in range(0, 8):	
		GPIO.output(SDI, 0x80 & (dat << bit)) #data in and it shifts it 
		GPIO.output(SRCLK, GPIO.HIGH) #the latcch is enacted
		time.sleep(0.001)
		GPIO.output(SRCLK, GPIO.LOW)#the latch is then closed

def hc595_out():
	#this makes the clock high so that the data can go into it
	GPIO.output(RCLK, GPIO.HIGH)
	time.sleep(0.001)
	GPIO.output(RCLK, GPIO.LOW)

def loop():
	WhichLeds = LED4	# Change Mode, modes from LED0 to LED3
	sleeptime = 0.1		# Change speed, lower value, faster speed
	while True:
                '''
		hc595_in(WhichLeds)
		hc595_out()
		time.sleep(sleeptime)
		'''
                for i in range(0, len(WhichLeds[i])):
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
		loop()  
	except KeyboardInterrupt:  
		destroy()  
