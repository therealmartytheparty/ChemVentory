from list_class import *
from chemical_class import *
from GUI.finalgu import *
import sys
from PyQt5 import QtGui, uic


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWin = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWin)
    MainWin.show()
    #additems


    chem_1 = Chemical('Chemical 1', 'CF1', 'Company1', 600, 500, 100)
    chem_2 = Chemical('Chemical 2', 'CF2', 'Company2', 500, 400, 200)
    chem_3 = Chemical('Chemical 3', 'CF3', 'Company3', 400, 300, 300)
    chem_4 = Chemical('Chemical 4', 'CF4', 'Company4', 300, 200, 400)
    chem_5 = Chemical('Chemical 5', 'CF5', 'Company5', 200, 100, 500)
    chem_6 = Chemical('Chemical 6', 'CF6', 'Company6', 100, 50, 600)

    list = list()
    list.add(chem_1)
    list.add(chem_2)
    list.add(chem_3)
    list.add(chem_4)
    list.add(chem_5)
    list.add(chem_6)

    list.print()

    chem_1.file_out()
    chem_2.file_out()
    chem_3.file_out()
    chem_4.file_out()
    chem_5.file_out()
    chem_6.file_out()

    chem_1.file_in()

    sys.exit(app.exec_())
