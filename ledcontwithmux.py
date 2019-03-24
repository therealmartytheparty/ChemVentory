#this code will control a multiplex in order to drive leds 
from gpiozero import LED
from time import sleep

#initialize the led pins to variables
led = LED(14)
led1 = LED(15)
led2 = LED(18)
led3 = LED(23)

while True: 
    #ask what led you would like to go on and store in x
    print("What LED woudl you like to turn on? 1 through 4")
    x = input()
    #if statements that will go through different cases of the multiplex
    if x == 1:
        led.on()
        sleep(4)
        led.off()
        sleep(4)
    elif x == 2:
        led1.on() 
        sleep(4)
        led1.off()
        sleep(4)
    elif x == 3:
        led2.on()
        sleep(4)
        led2.off()
        sleep(4)
    elif x == 4:
        led3.on()
        sleep(4)
        led4.off()
        sleep(4)
    #to quit the program press 0
    elif x==0:
        break
    #if anything else is type give an error
    else:
        print("Please type in the right thing please you dipshit")
    
