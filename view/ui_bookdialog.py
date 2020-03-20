# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bookdialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BookDialog(object):
    def setupUi(self, BookDialog):
        BookDialog.setObjectName("BookDialog")
        BookDialog.resize(477, 362)
        self.verticalLayout = QtWidgets.QVBoxLayout(BookDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableViewBooks = QtWidgets.QTableView(BookDialog)
        self.tableViewBooks.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableViewBooks.setObjectName("tableViewBooks")
        self.verticalLayout.addWidget(self.tableViewBooks)
        self.tableViewBooks.setSortingEnabled(True)


        self.retranslateUi(BookDialog)
        QtCore.QMetaObject.connectSlotsByName(BookDialog)

    def retranslateUi(self, BookDialog):
        _translate = QtCore.QCoreApplication.translate
        BookDialog.setWindowTitle(_translate("BookDialog", "Dialog"))

