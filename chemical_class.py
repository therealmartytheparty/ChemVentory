class Chemical:

    num_of_Chems = 0

    def __init__(self, name=None, formula=None, supplier=None, massI=None, massUpdate=None, age=None):
        if name != None:
            self.barC = Chemical.num_of_Chems + 1
            self.formula = formula
            self.name = name
            self.supplier = supplier
            self.massI = massI
            self.massUpdate = massUpdate
            self.age = age

        Chemical.num_of_Chems += 1

    def setbarC(self,barC):
        self.barC = barC

    def setname(self,name):
        self.name = name

    def setformula(self,formula):
        self.formula = formula

    def setsupplier(self,supplier):
        self.supplier = supplier

    def setmassI(self,massI):
        self.massI = massI

    def setmassUpdate(self,massUpdate):
        self.massUpdate = massUpdate

    def setage(self,age):
        self.age = age
