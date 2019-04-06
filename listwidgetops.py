import json
from chemical_class import *
from list_class import *

def additems(chem,window):
    trans = QtCore.QCoreApplication.translate

def file_out(chem):

    # increments the chemical list size file
    barcodefile = open("Chemicals/Chembarc.txt",'w')
    barcodefile.write(chem.barC)
    barcodefile.close()

    #opens file for chemical file dumping with json
    temp = str(chem.barC) + '.txt'
    data = {}
    data['chem'] = []
    data['chem'].append({
        'barC': chem.barC,
        'name': chem.name,
        'formula': chem.formula,
        'supplier': chem.supplier,
        'massI': chem.massI,
        'massUpdate': chem.massUpdate,
        'age': chem.age
    })

    # dumps the data into the file that was opened
    with open("Chemicals/" + temp, 'w') as outfile:
        json.dump(data, outfile)
    outfile.close()


def file_in(size):
    #opens existing file to fill out chemical object
    tempchem = Chemical()
    temp_in = str(size) + '.txt'
    with open("Chemicals/" + temp_in) as json_file:
        data = json.load(json_file)
        for p in data['chem']:
            tempchem.setbarC(p['barC'])
            tempchem.setname(p['name'])
            tempchem.setformula(p['formula'])
            tempchem.setsupplier(p['supplier'])
            tempchem.setmassI(p['massI'])
            tempchem.setmassUpdate(p['massUpdate'])
            tempchem.setage(p['age'])
    json_file.close
    return tempchem

def listsizer():
    # finds the amount of chemicals within the list
    barcodefile = open("Chemicals/Chembarc.txt")
    listsize = barcodefile.readline()
    barcodefile.close()
    listsize = int(listsize)
    return listsize

def listloader():
    size = listsizer()
    array = []
    index = 1

    while size > 0:
        array.append(file_in(index))

        index += 1
        size -= 1
    return array
