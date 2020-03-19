import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *
from PyQt5.QtGui import *

from view.ui_mainwindow import Ui_MainWindow
from view.bookDialog import BookDialog
from view.readerDialog import ReaderDialog
from controller.databaseManager import DatabaseManager, dbManager

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Biblioteka")
        self.initConnections()
        self.tableViewOrders.clicked.connect(self.displayDetails)
        self.actionNoweZamowienie.setIcon(QIcon("resources/newOrder.png"))
        self.actionCzytelnik.setIcon(QIcon("resources/readers.png"))
        self.actionKsiazka.setIcon(QIcon("resources/books.png"))
        self.actionZamknij.setIcon(QIcon("resources/iconClose.png"))

    def displayDetails(self, idx):
        row = idx.row()
        id = dbManager.modelOrders.data(dbManager.modelOrders.index(row, 0))
        self.tableViewDetails.setModel(dbManager.getModelDetails(id))



    def initConnections(self):
        self.actionCzytelnik.triggered.connect(self.openReadersDialog)
        self.actionKsiazka.triggered.connect(self.openBooksDialog)
        self.tableViewOrders.setModel(dbManager.modelOrders)

    def openReadersDialog(self):
        readerDialog = ReaderDialog()
        readerDialog.exec_()

    def openBooksDialog(self):
        booksDialog = BookDialog()
        booksDialog.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_())
