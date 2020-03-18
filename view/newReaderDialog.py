import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *

from view.ui_newreaderdialog import Ui_NewReaderDialog
from controller.databaseManager import *

class AddReaderDialog(QDialog, Ui_NewReaderDialog):
    def __init__(self):
        super(AddReaderDialog, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Nowy czytelnik")
