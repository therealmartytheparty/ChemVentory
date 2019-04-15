from list_class import *
from chemical_class import *
from finalgu import *
from listops import *
import sys
from PyQt5 import QtGui, uic


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWin = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()

    listthing = listloader()
    size = len(listthing)

    print(listthing[0].getname())

    searchList(listthing, "Chemical 1")

    ui.setupUi(MainWin, size, listthing)
    MainWin.show()

    sys.exit(app.exec_())
