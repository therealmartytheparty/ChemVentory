import json

class Chemical:

    num_of_Chems = 0

    def __init__(self, name, formula, supplier, massI, massUpdate, age):
        self.barC = Chemical.num_of_Chems + 1
        self.name = name
        self.formula = formula
        self.supplier =supplier
        self.massI = massI
        self.massUpdate = massUpdate
        self.age = age

        Chemical.num_of_Chems += 1

    def file_out(self):
        temp = self.name + '.txt'
        data = {}
        data['chem'] = []
        data['chem'].append({
            'barC': self.barC,
            'name': self.name,
            'formula': self.formula,
            'supplier': self.supplier,
            'massI': self.massI,
            'massUpdate': self.massUpdate,
            'age': self.age
        })
        with open(temp, 'w') as outfile:
            json.dump(data, outfile)

    def node(self, prevnode=None, nextnode=None):
        self.prev = prevnode
        self.curr = self
        self.next = nextnode



'''
    def file_in(self):
        with open('data.txt') as json_file:
            data2 = json.load(json_file)
            for p in data2['people']:
                print('barC: ' + p['name'])
                print('Website: ' + p['website'])
                print('From: ' + p['from'])
                print('')
'''

def displaylist(head):
    currnode = head

    while currnode is not None:
        # we can then get this to display on the GUI
        print(currnode.name)
        currnode = currnode.next

def addnode(chem)
    temp = chem
    if #nothing in list
        while chem is not None

    else:
        chem.node(None,None)

chem_1 = Chemical('Chemical 1', 'CF1', 'Company1', 600, 500, 100)
chem_2 = Chemical('Chemical 2', 'CF2', 'Company2', 500, 400, 200)
chem_3 = Chemical('Chemical 3', 'CF3', 'Company3', 400, 300, 300)
chem_4 = Chemical('Chemical 4', 'CF4', 'Company4', 300, 200, 400)
chem_5 = Chemical('Chemical 5', 'CF5', 'Company5', 200, 100, 500)
chem_6 = Chemical('Chemical 6', 'CF6', 'Company6', 100, 50, 600)

chem_1.node(None,chem_2)
chem_2.node(chem_2,chem_3)
chem_3.node(chem_3,chem_4)
chem_4.node(chem_4,chem_5)
chem_5.node(chem_5,chem_6)
chem_6.node(chem_6)






chem_1.file_out()
chem_2.file_out()
