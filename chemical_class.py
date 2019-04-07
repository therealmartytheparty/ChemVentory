import json
import datetime
from datetime import timedelta

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
        dateSystemEntry = datetime.datetime.now()
        dateExpire = datetime.datetime.now() + timedelta(days = 365)
        #chemLocation

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
            'age': self.age,
            'dateSystemEntry': self.dateSystemEntry,
            'dateExpire': self.dateExpire,
            'chemLocation': self.chemLocation
        })
        with open(temp, 'w') as outfile:
            json.dump(data, outfile)
        outfile.close()


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
                slef.dateSystemEntry = p['dateSystemEntry']
                self.dateExpire = p['dateExpire']
                self.chemLocation = p['chemLocation']

        outfile.close()
