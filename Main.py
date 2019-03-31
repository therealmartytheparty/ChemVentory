from list_class import *
from chemical_class import *

if __name__ == "__main__":

    chem_1 = Chemical('Chemical 1', 'CF1', 'Company1', 600, 500, 100)
    chem_2 = Chemical('Chemical 2', 'CF2', 'Company2', 500, 400, 200)
    chem_3 = Chemical('Chemical 3', 'CF3', 'Company3', 400, 300, 300)
    chem_4 = Chemical('Chemical 4', 'CF4', 'Company4', 300, 200, 400)
    chem_5 = Chemical('Chemical 5', 'CF5', 'Company5', 200, 100, 500)
    chem_6 = Chemical('Chemical 6', 'CF6', 'Company6', 100, 50, 600)

    d = list()
    d.add(chem_1)
    d.add(chem_2)
    d.add(chem_3)
    d.add(chem_4)
    d.add(chem_5)
    d.add(chem_6)

    d.print()





    chem_1.file_out()
    chem_2.file_out()
