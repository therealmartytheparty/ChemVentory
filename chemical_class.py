import json

class Chemical:

    num_of_Chems = 0

    def __init__(self, name, formula, supplier, massI, massUpdate, age):
        self.barC = Chemical.num_of_Chems + 1
        self.name = name
        self.formula = formula
        self.supplier = supplier
        self.massI = massI
        self.massUpdate = massUpdate
        self.age = age

        Chemical.num_of_Chems += 1

    def file_out(self):
        temp = str(self.barC) + '.txt'
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
        outfile.close()
<<<<<<< HEAD

    def file_in(self):
        temp_in = str(self.barC) + '.txt'
        with open(temp_in) as json_file:
            data = json.load(json_file)
            for p in data['chem']:
                self.barC = p['barC']
                self.name = p['name']
                self.formula = p['formula']
                self.supplier = p['supplier']
                self.massI = p['massI']
                self.massUpdate = p['massUpdate']
                self.age = p['age']
        outfile.close()
=======

    def file_in(self):
        temp_in = str(self.barC) + '.txt'
        with open(temp_in) as json_file:
            data = json.load(json_file)
            for p in data['chem']:
                self.barC = p['barC']
                self.name = p['name']
                self.formula = p['formula']
                self.supplier = p['supplier']
                self.massI = p['massI']
                self.massUpdate = p['massUpdate']
                self.age = p['age']
        outfile.close()

    def node(self, prevnode=None, nextnode=None):
        self.prev = prevnode
        self.curr = self
        self.next = nextnode

def displaylist(head):
    currnode = head

    while currnode is not None:
        # we can then get this to display on the GUI
        print(currnode.name)
        currnode = currnode.next



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

displaylist(chem_1)
>>>>>>> master
