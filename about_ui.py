
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QShortcut
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore

class Ui_About(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(QtCore.QSize(544, 365))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMaximumSize(QtCore.QSize(544, 365))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./assets/img/icons8-camera-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(0, 10, 541, 351))
        self.groupBox.setObjectName("groupBox")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 20, 531, 321))
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "About"))
        self.groupBox.setTitle(_translate("Dialog", "About"))
        self.plainTextEdit.setPlainText(_translate("Dialog", "------------Image Detector---------\n"
"Version 1.0:\n"
"-----Uses--------------------------------\n"
"1.Classify between images of cats/dogs\n"
"2.Classify between Rotten Apples and Fresh Apples\n"
"3.Classify between Rotten Oranges and Fresh Oranges\n"
"4.Classify between Rotten Bananas and Fresh Bananas\n"
"5.Classify and Detect Random Objects\n"
"6.Classify Male and Female faces\n"
"\n"
"Requirements:\n"
"1.Python 3.7\n"
"2.TensorFlow 1.15.0+\n"
"3.PyQT5 5.13.0\n"
"4.OpenCV 2\n"
"5.Numpy \n"
"\n"
"\n"
"---------- Submitted by---------------------------------\n"
"Swathi Korrapatti - 8667968\n"
"Chandrashekar Katherashala - 8641849"
))