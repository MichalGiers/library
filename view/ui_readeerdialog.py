# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'readeerdialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(610, 429)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonDodaj = QtWidgets.QPushButton(Dialog)
        self.pushButtonDodaj.setObjectName("pushButtonDodaj")
        self.horizontalLayout.addWidget(self.pushButtonDodaj)
        self.pushButtonDelete = QtWidgets.QPushButton(Dialog)
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.horizontalLayout.addWidget(self.pushButtonDelete)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableViewReaders = QtWidgets.QTableView(Dialog)
        self.tableViewReaders.setProperty("showDropIndicator", False)
        self.tableViewReaders.setAlternatingRowColors(True)
        self.tableViewReaders.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableViewReaders.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableViewReaders.setSortingEnabled(True)
        self.tableViewReaders.setObjectName("tableViewReaders")
        self.tableViewReaders.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tableViewReaders)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Czytelnicy"))
        self.pushButtonDodaj.setText(_translate("Dialog", "Dodaj"))
        self.pushButtonDelete.setText(_translate("Dialog", "Usun"))
