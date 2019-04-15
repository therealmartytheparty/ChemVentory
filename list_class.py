from chemical_class import *

class listcl:

    def addToList(self, chemList):
        if len(chemList) < 96:
            chemList.append(self)

            for position in range(len(chemList)):     # by index
                print(chemList[position].name)

        else:
            print ('The chemical list is full')


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


    def searchList(self, chemstring):
        for x in range(1, len(self)):
            if self.name == chemstring:

                return self.name
