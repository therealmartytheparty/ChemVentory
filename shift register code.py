# shift register code to interface with the raspberry pi that is from a instrutibles 
# this code is made for a 3d led cube so keep that in mind

class Mutliplexer():
  def_init_(self):
    self.running = True
    self.register1 = ShiftRegister(10,12,13)
    self.register2 = ShiftRegister(22,16,18)

  #the second parameter has to exist for the thread to run, but doens nothing
  def multiplex(self,p):
    while self.running:
        for y in range(len(points))
           #turn previous layer off before updating LEDS
           GPIO.output(transistors[y-1],0)
         
        for x in range(len(points[y])):
            for z in range(len(points[y][x])):
              #pick which register to write to - each controls half 
              # of the cube
              if x < 2:
                  self.register.clock(points[y][x][z])
              else:
                  self.register.clock(points[y][x][z])
              
        #write register values to cube and enable layer
        self.register1.latch()
        self.register2.latch()
        GPIO.output(transistors[y],1)
      
        sleep(0.001)
