import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *

from view.ui_readeerdialog import Ui_Dialog
from controller.databaseManager import DatabaseManager, dbManager
from view.newReaderDialog import AddReaderDialog

class ReaderDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super(ReaderDialog, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Czytelnicy")
        self.pushButtonDodaj.clicked.connect(self.addReader)
        self.pushButtonDelete.clicked.connect(self.deleteReader)

        self.pushButtonDelete.setEnabled(0)
        self.tableViewReaders.clicked.connect(self.enableDeleteButton)

        dbManager.initializeReadersModel()
        self.tableViewReaders.setModel(dbManager.modelReaders)
        self.tableViewReaders.hideColumn(0)

    def enableDeleteButton(self):
        self.pushButtonDelete.setEnabled(1)

    def addReader(self):
        addReaderDialog = AddReaderDialog()
        if addReaderDialog.exec_():
            dbManager.addNewReader(addReaderDialog.lineEditName.text(), addReaderDialog.lineEditSurname.text(), addReaderDialog.lineEditTel.text())

    def deleteReader(self):
        idx = self.tableViewReaders.currentIndex()
        row = idx.row()
        id = dbManager.modelReaders.data(dbManager.modelReaders.index(row, 0))
        dbManager.removeReader(id)
        print(id)


