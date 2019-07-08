# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(700, 400))
        MainWindow.setMaximumSize(QtCore.QSize(700, 400))
        font = QtGui.QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(60, 10, 581, 301))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(60)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QtCore.QSize(581, 301))
        self.listWidget.setMaximumSize(QtCore.QSize(581, 301))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("background-color: rgb(221, 221, 221);\n"
"border-color: rgb(0, 0, 0);")
        self.listWidget.setObjectName("listWidget")
        self.downloadButton = QtWidgets.QPushButton(self.centralwidget)
        self.downloadButton.setGeometry(QtCore.QRect(60, 360, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.downloadButton.setFont(font)
        self.downloadButton.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.downloadButton.setObjectName("downloadButton")
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(520, 360, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.stopButton.setFont(font)
        self.stopButton.setStyleSheet("background-color: rgb(255, 0, 0)")
        self.stopButton.setObjectName("stopButton")
        self.lblStatus = QtWidgets.QLabel(self.centralwidget)
        self.lblStatus.setGeometry(QtCore.QRect(250, 320, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lblStatus.setFont(font)
        self.lblStatus.setText("")
        self.lblStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.lblStatus.setObjectName("lblStatus")
        self.downloadCheckedButton = QtWidgets.QPushButton(self.centralwidget)
        self.downloadCheckedButton.setGeometry(QtCore.QRect(280, 360, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.downloadCheckedButton.setFont(font)
        self.downloadCheckedButton.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.downloadCheckedButton.setObjectName("downloadCheckedButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.downloadButton.setText(_translate("MainWindow", "Скачать все"))
        self.stopButton.setText(_translate("MainWindow", "Стоп"))
        self.downloadCheckedButton.setText(_translate("MainWindow", "Скачать выбранные"))

