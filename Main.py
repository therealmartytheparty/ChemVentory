from list_class import *
from chemical_class import *
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(500, 500))
        self.centralwidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(250, 100))
        self.frame_2.setMaximumSize(QtCore.QSize(250, 800))
        self.frame_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.frame_2.setBaseSize(QtCore.QSize(0, 0))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(1)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listWidget = QtWidgets.QListWidget(self.frame_2)
        self.listWidget.setMinimumSize(QtCore.QSize(250, 500))
        self.listWidget.setMaximumSize(QtCore.QSize(250, 16777215))
        self.listWidget.setMouseTracking(True)
        self.listWidget.setTabletTracking(True)
        self.listWidget.setIconSize(QtCore.QSize(0, 0))
        self.listWidget.setGridSize(QtCore.QSize(0, 0))
        self.listWidget.setModelColumn(0)
        self.listWidget.setUniformItemSizes(True)
        self.listWidget.setItemAlignment(QtCore.Qt.AlignLeading)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.verticalLayout_2.addWidget(self.listWidget)
        self.horizontalLayout_4.addWidget(self.frame_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButton.setIconSize(QtCore.QSize(20, 20))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda:self.search(self.pushButton))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(lambda:self.checkin(self.pushButton_3))
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda:self.checkout(self.pushButton_2))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(lambda:self.outputfile(self.pushButton_5))
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setMinimumSize(QtCore.QSize(234, 50))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(lambda:self.newentry(self.pushButton_6))
        self.horizontalLayout_3.addWidget(self.pushButton_6)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_3.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(lambda:self.saveentry(self.pushButton_9))
        self.horizontalLayout_5.addWidget(self.pushButton_9)
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(lambda:self.delentry(self.pushButton_8))
        self.horizontalLayout_5.addWidget(self.pushButton_8)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(lambda:self.editentry(self.pushButton_7))
        self.horizontalLayout_5.addWidget(self.pushButton_7)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Chemventory MainWindow"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listloader(MainWindow)
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.pushButton_3.setText(_translate("MainWindow", "Check out"))
        self.pushButton_2.setText(_translate("MainWindow", "Check In"))
        self.pushButton_5.setText(_translate("MainWindow", "Create Output File"))
        self.pushButton_6.setText(_translate("MainWindow", "Create New Entry"))
        self.pushButton_9.setText(_translate("MainWindow", "Save Entry"))
        self.pushButton_8.setText(_translate("MainWindow", "Delete Entry"))
        self.pushButton_7.setText(_translate("MainWindow", "Edit Entry"))

    def listloader(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Base"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "HCL"))

    def search(self,b):
        print ("clicked button is "+b.text())

    def checkin(self,b):
        print ("clicked button is "+b.text())

    def checkout(self,b):
        print ("clicked button is "+b.text())

    def outputfile(self,b):
        print ("clicked button is "+b.text())

    def newentry(self,b):
        print ("clicked button is "+b.text())

    def saveentry(self,b):
        print ("clicked button is "+b.text())

    def delentry(self,b):
        print ("clicked button is "+b.text())

    def editentry(self,b):
        print ("clicked button is "+b.text())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

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


    sys.exit(app.exec_())
