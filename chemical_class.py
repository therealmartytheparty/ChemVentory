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
        with open("Chemicals/" + temp, 'w') as outfile:
            strrr = str(self.barC) +"\n"
            print(strrr)
            outfile2 = open("Chemicals/Chembarc.txt",'a')
            outfile2.write(strrr)
            json.dump(data, outfile)
        outfile.close()
        outfile2.close()


    def file_in(self):
        barcode = []
        with open("Chemicals/Chembarc.txt",'r') as file:
            line = file.readline()
            cnt = 1
            while line:
                print("Line {}: {}".format(cnt,line.strip()))
                line = file.readline()
                cnt += 1
        file.close()

'''
        temp_in = str(self.barC) + '.txt'
        with open("Chemicals/" + temp_in) as json_file:
            data = json.load(json_file)
            for p in data['chem']:
                self.barC = p['barC']
                self.name = p['name']
                self.formula = p['formula']
                self.supplier = p['supplier']
                self.massI = p['massI']
                self.massUpdate = p['massUpdate']
                self.age = p['age']
        json_file.close()
'''
