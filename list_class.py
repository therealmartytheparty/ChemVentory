from chemical_class import *

class list:

    def addToList(self, chemList):
        if len(chemList) < 96:
            chemList.append(self)

            for position in range(len(chemList)):     # by index
                print(chemList[position].name)

        else:
            print ('The chemical list if full')


    def removeFromList(self, chemList):
        for x in range(1, len(chemList)):
            if self.name == chemList[x].name:
                del chemList[x]
                
        for position in range(len(chemList)):     # by index
            print(chemList[position].name)


    def sortList(self, chemList):
        chemList.sort(key=lambda x: x.name)

        for position in range(len(chemList)):     # by index
            print(chemList[position].name)


    def searchList(self, chemList):
        for x in range(1, len(chemList)):
            if self.name == chemList[x].name:

                print(chemList[x].name)
