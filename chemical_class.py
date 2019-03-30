import json

class Chemical:

    num_of_Chems = 0


    def __init__(self, name, formula, supplier, massI, massUpdate, age):
        self.name = name
        self.formula = formula
        self.supplier =supplier
        self.massI = massI
        self.massUpdate = massUpdate
        self.age = age

        Chemical.num_of_Chems += 1

chem_1 = Chemical('Chemical 1', 'CF1', 'Company1', 600, 500, 100)
chem_2 = Chemical('Chemical 2', 'CF2', 'Company2', 500, 400, 200)


print('')

print(chem_1.name)
print(chem_1.formula)
print(chem_1.supplier)
print(chem_1.massI)
print(chem_1.massUpdate)
print(chem_1.age)

print('')

print(chem_2.name)
print(chem_2.formula)
print(chem_2.supplier)
print(chem_2.massI)
print(chem_2.massUpdate)
print(chem_2.age)

data = {}
data['chem'] = []
data['chem'].append({
    'name': chem_1.name,
    'formula': chem_1.formula,
    'supplier': chem_1.supplier,
    'massI': chem_1.massI,
    'massUpdate': chem_1.massUpdate,
    'age': chem_1.age
})
data['chem'].append({
    'name': chem_2.name,
    'formula': chem_2.formula,
    'supplier': chem_1.supplier,
    'massI': chem_2.massI,
    'massUpdate': chem_1.massUpdate,
    'age': chem_2.age
})

with open('chem_1.txt', 'w') as outfile:
    json.dump(data, outfile)

#emp_str_1 = 'John-Doe-70000'
#emp_str_2 = 'Steve-Smith-30000'
#emp_str_3 = 'Jane-Doe-90000'

#name, formula, maxAge = emp_str_1.split('-')

#new_chem_1 = Chemical(name, formula, maxAge)
#new_chem_1 = Chemical.from_string(emp_str_1)

#print(new_chem_1.maxAge)

#import datetime
#my_date = datetime.date(2016, 7, 11)

#print(Chemical.is_workday(my_date))
