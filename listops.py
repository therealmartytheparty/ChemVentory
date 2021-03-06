import json
from chemical_class import *
from finalgu import *

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
        'age': chem.age,
        'insys': chem.insys
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
            tempchem.setinsys(p['insys'])
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
    #find the size of the list
    size = listsizer()
    array = []
    index = 1

    # iterate until youve reached the size of the file list
    while size > 0:
        array.append(file_in(index))

        index += 1
        size -= 1
    return array

def addToList(chemList, chemnew):
    if len(chemList) < 96:
        chemList.append(chemnew)

    else:
        print ('The chemical list is full')


def removeFromList(chemList, chemrm):
    for x in range(1, len(chemList)):
        if chemList[x].name == chemrm.name:
            del chemList[x]

def sortList(chemList):
    chemList.sort(key=lambda x: x.name)

def searchList(chemlist, chemstring):
    for x in range(0, len(chemlist)):
        if chemlist[x].name == chemstring:
            return chemlist[x]
