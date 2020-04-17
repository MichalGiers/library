import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *

from view.ui_bookdialog import Ui_BookDialog
from controller.databaseManager import DatabaseManager, dbManager

class BookDialog(QDialog, Ui_BookDialog):
    def __init__(self):
        super(BookDialog, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Książki")
        dbManager.initializeBooksModel()
        self.tableViewBooks.setModel(dbManager.modelBooks)