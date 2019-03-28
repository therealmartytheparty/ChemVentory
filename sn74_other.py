import RPi.GPIO as IO         # calling for header file which helps us use GPIO’s of PI
import time                             # calling for time to provide delays in program
IO.setwarnings(False)           # do not show any warnings
x=1                
IO.setmode (IO.BCM)        # programming the GPIO by BCM pin numbers. (like PIN29 as‘GPIO5’)
IO.setup(4,IO.OUT)            # initialize GPIO Pins as an output.
IO.setup(5,IO.OUT)
IO.setup(6,IO.OUT)
while 1:                               # execute loop forever
    for y in range(8):            # loop for counting up 8 times
        IO.output(4,1)            # pull up the data pin for every bit.
        time.sleep(0.1)            # wait for 100ms
        IO.output(5,1)            # pull CLOCK pin high
        time.sleep(0.1)
        IO.output(5,0)            # pull CLOCK pin down, to send a rising edge
        IO.output(4,0)            # clear the DATA pin
        IO.output(6,1)            # pull the SHIFT pin high to put the 8 bit data out parallel
        time.sleep(0.1)
        IO.output(6,0)            # pull down the SHIFT pin

    for y in range(8):            # loop for counting up 8 times
        IO.output(4,0)            # clear the DATA pin, to send 0
        time.sleep(0.1)            # wait for 100ms
        IO.output(5,1)            # pull CLOCK pin high
        time.sleep(0.1)
        IO.output(5,0)            # pull CLOCK pin down, to send a rising edge
        IO.output(4,0)            # keep the DATA bit low to keep the countdown
        IO.output(6,1)            # pull the SHIFT pin high to put the 8 bit data out parallel
        time.sleep(0.1)
        IO.output(6,0)
