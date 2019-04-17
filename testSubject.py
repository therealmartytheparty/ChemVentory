from chemical_class import *

class testSubject(Chemical):

    def __init__(self):
        codeName = 'Aaron (Autonomous Aerial Raptor Operating Network)'
        self.purpose = 'World Domination. Making Raptors great again.'

        Chemical.__init__(self,codeName,"KAIAMIMAR","WIT", 650, 650, 21, 1)
