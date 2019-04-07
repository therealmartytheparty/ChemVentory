from chemical_class import *

chem_1 = Chemical('Chemical 1', 'CF1', 'Company1', 600, 500, 100)
chem_2 = Chemical('Chemical 2', 'CF2', 'Company2', 500, 400, 200)
chem_3 = Chemical('Chemical 3', 'CF3', 'Company3', 400, 300, 300)
chem_4 = Chemical('Chemical 4', 'CF4', 'Company4', 300, 200, 400)
chem_5 = Chemical('Chemical 5', 'CF5', 'Company5', 200, 100, 500)
chem_6 = Chemical('Chemical 6', 'CF6', 'Company6', 100, 50, 600)

chemList = [chem_3, chem_2, chem_1, chem_4, chem_5, chem_6]

chemListMax = 96


class list:

    def addToList(self):
        if len(chemList) < 96:
            chemList.append(self)
            #chemList.sortList(self)
            print ('The chemical ' + self.name + ' was added!')

            for position in range(len(chemList)):     # by index
                print(chemList[position].name)

            print('')

        else:
            print ('The chemical list if full')


    def removeFromList(self):
        #print(self.name)
        #print('')
        for x in range(1, len(chemList)):
            #print(x)
            if self.name == chemList[x].name:
                #print(chemList[x].name)
                del chemList[x]
                #chemList.remove(self)
        for position in range(len(chemList)):     # by index
            print(chemList[position].name)


    def sortList():
        #chemList.name.sort()
        chemList.sort(key=lambda x: x.name)

        for position in range(len(chemList)):     # by index
            print(chemList[position].name)


    def searchList(self):
        #print('Start searching')
        for x in range(1, len(chemList)):
            #print(x)
            if self.name == chemList[x].name:
                #print(chemList[x].name)
                print(chemList[x].name)
                #chemList.remove(self)


    addToList(Chemical('Chemical 7', 'CF7', 'Company7', 600, 500, 100))
    addToList(Chemical('Chemical 8', 'CF8', 'Company8', 600, 500, 100))

    removeFromList(Chemical('Chemical 8', 'CF8', 'Company8', 600, 500, 100))

    print('')
    sortList()

    searchList(Chemical('Chemical 6', 'CF6', 'Company6', 100, 50, 600))
