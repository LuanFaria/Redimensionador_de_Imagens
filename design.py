# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(505, 411)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_escolher = QtWidgets.QPushButton(self.centralwidget)
        icon = QtGui.QIcon.fromTheme("blue")
        self.btn_escolher.setIcon(icon)
        self.btn_escolher.setObjectName("btn_escolher")
        self.gridLayout.addWidget(self.btn_escolher, 1, 4, 1, 1)
        self.input_abrir = QtWidgets.QLineEdit(self.centralwidget)
        self.input_abrir.setObjectName("input_abrir")
        self.gridLayout.addWidget(self.input_abrir, 1, 0, 1, 4)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 485, 298))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_img = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_img.setText("")
        self.label_img.setObjectName("label_img")
        self.gridLayout_2.addWidget(self.label_img, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 5)
        self.largura = QtWidgets.QLineEdit(self.centralwidget)
        self.largura.setObjectName("largura")
        self.gridLayout.addWidget(self.largura, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 2, 1, 1)
        self.btn_redimensionar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_redimensionar.setObjectName("btn_redimensionar")
        self.gridLayout.addWidget(self.btn_redimensionar, 2, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.altura = QtWidgets.QLineEdit(self.centralwidget)
        self.altura.setObjectName("altura")
        self.gridLayout.addWidget(self.altura, 2, 3, 1, 1)
        self.btn_salvar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_salvar.setObjectName("btn_salvar")
        self.gridLayout.addWidget(self.btn_salvar, 3, 4, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Redimensionar Imagem"))
        self.btn_escolher.setText(_translate("MainWindow", "Escolher Arquivo"))
        self.label_2.setText(_translate("MainWindow", "Altura"))
        self.btn_redimensionar.setText(_translate("MainWindow", "Redimensionar"))
        self.label.setText(_translate("MainWindow", "Largura"))
        self.btn_salvar.setText(_translate("MainWindow", "Salvar"))
