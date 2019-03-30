import json

class Chemical:

    num_of_Chems = 0
    max_age = 365

    def __init__(self, name, formula, supplier, massI, massUpdate, maxAge):
        self.name = name
        self.formula = formula
        self.supplier =supplier
        self.massI = massI
        self.massUpdate = massUpdate
        self.maxAge = maxAge

        Chemical.num_of_Chems += 1

#    def fullname(self):
#        return '{} {}'.format(self.name, self.formula)

    def apply_maxAge(self):
        self.maxAge = int(self.max_age)

    @classmethod
    def set_max_age(cls, age):
        cls.max_age = age

#    @classmethod
#    def save_to_file(cls):
#        cls.

#    @classmethod
#    def from_string(cls, emp_str):
#        name, formula, supplier, maxAge = emp_str.split('-')
#        return cls(name, formula, supplier, maxAge)

#    @staticmethod
#    def is_workday(day):
#        if day.weekday() == 5 or day.weekday() == 6:
#            return False
#        return True


chem_1 = Chemical('Chemical 1', 'CF1', 'Company1', 600, 500, 1)
chem_2 = Chemical('Chemical 2', 'CF2', 'Company2', 500, 400, 1)

#Chemical.set_max_age(350)

print(Chemical.max_age)

print('')

print(chem_1.name)
print(chem_1.formula)
print(chem_1.supplier)
print(chem_1.massI)
print(chem_1.massUpdate)
print(chem_1.max_age)

print('')

print(chem_2.name)
print(chem_2.formula)
print(chem_2.supplier)
print(chem_2.massI)
print(chem_2.massUpdate)
print(chem_2.max_age)

with open('chem_1.txt', 'w') as outfile:
    json.dump(chem_1.name, chem_1.formula, outfile)

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
