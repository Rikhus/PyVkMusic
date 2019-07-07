# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginDesign.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(524, 392)
        MainWindow.setStyleSheet("background-color: rgb(241, 241, 241);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(524, 392))
        self.centralwidget.setMaximumSize(QtCore.QSize(524, 392))
        self.centralwidget.setObjectName("centralwidget")
        self.loginLine = QtWidgets.QLineEdit(self.centralwidget)
        self.loginLine.setGeometry(QtCore.QRect(60, 200, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.loginLine.setFont(font)
        self.loginLine.setStyleSheet("QLineEdit { border: 2px groove gray;}")
        self.loginLine.setObjectName("loginLine")
        self.passLine = QtWidgets.QLineEdit(self.centralwidget)
        self.passLine.setGeometry(QtCore.QRect(60, 260, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.passLine.setFont(font)
        self.passLine.setStyleSheet("QLineEdit { border: 2px groove gray;}")
        self.passLine.setObjectName("passLine")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(180, 330, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.loginButton.setFont(font)
        self.loginButton.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.loginButton.setObjectName("loginButton")
        self.lblImg = QtWidgets.QLabel(self.centralwidget)
        self.lblImg.setGeometry(QtCore.QRect(140, 0, 241, 181))
        self.lblImg.setText("")
        self.lblImg.setPixmap(QtGui.QPixmap("vk_login.png"))
        self.lblImg.setScaledContents(True)
        self.lblImg.setObjectName("lblImg")
        self.lblStatus = QtWidgets.QLabel(self.centralwidget)
        self.lblStatus.setGeometry(QtCore.QRect(20, 340, 131, 21))
        self.lblStatus.setText("")
        self.lblStatus.setObjectName("lblStatus")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loginButton.setText(_translate("MainWindow", "Login"))

