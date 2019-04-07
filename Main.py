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

    ui.setupUi(MainWin, size, list)
    MainWin.show()



    sys.exit(app.exec_())
