import json
import datetime
from datetime import timedelta

class Chemical:

    num_of_Chems = 0

    def __init__(self, name=None, formula=None, supplier=None, massI=None, massUpdate=None, age=None, inout = None):
        if name != None:
            self.name = name

            if formula != None:
                self.formula = formula
                self.supplier = supplier
                self.massI = massI
                self.massUpdate = massUpdate
                self.age = age
                self.insys = inout
                self.barC = Chemical.num_of_Chems + 1


        Chemical.num_of_Chems += 1

    def setbarC(self,barC):
        self.barC = barC

    def setname(self,name):
        self.name = name

    def getname(self):
        return self.name

    def setformula(self,formula):
        self.formula = formula

    def setsupplier(self,supplier):
        self.supplier = supplier

    def setmassI(self,massI):
        self.massI = massI

    def setmassUpdate(self,massUpdate):
        self.massUpdate = massUpdate
        dateSystemEntry = datetime.datetime.now()
        dateExpire = datetime.datetime.now() + timedelta(days = 365)
        #chemLocation

    def setage(self,age):
        self.age = age

    def setinsys(self, inout):
        self.insys = inout
