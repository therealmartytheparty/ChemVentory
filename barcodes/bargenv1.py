from processing import *
#import processing
from random import randint


def decimalToBinary(x):
    #This function converts a Decimal into a Binary
    #It generates a nibble (4 digits binary number)
    binaryNumber=bin(x)[2:]
    return (4-len(binaryNumber)) * "0" + binaryNumber

def drawBarCode(height): 
    #Generates a 13-digit bar code.
    marginLeft=30
    marginTop=40
    for i in range(1,14):  
        digit=randint(0,9)
        nibble=decimalToBinary(digit)
        for j in range(0,4):  
            if nibble[j:j+1]=="1":
                fill(0,0,0)
                stroke(0,0,0)
            else
                fill(255,255,255)
                stroke(255,255,255)
            rect(marginLeft+i*8+2*j, marginTop, 2, height)
        
        #Display the digit in Decimal
        fill(0,0,0)
        stroke(0,0,0)
        #textSize(10)
        text(digit,marginLeft+i*8,marginTop+20+height)
                

def setup():
    strokeWeight(12)
    size(200,200)
    background(255,255,255)
    fill(0,0,0)
    stroke(0,0,0)
    drawBarCode(80)
    
#if __name__ == '__main__':
 #   setup()

setup()
