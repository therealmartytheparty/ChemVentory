from list_class import *
from chemical_class import *
from GUI.finalgu import *
from listwidgetops import *
import sys
from PyQt5 import QtGui, uic


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWin = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()

    list = listloader()
    size = len(list)

    ui.setupUi(MainWin, list, size)
    MainWin.show()

    print(list[0].name)
    print(list[0].barC)

    sys.exit(app.exec_())
