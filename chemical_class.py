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
