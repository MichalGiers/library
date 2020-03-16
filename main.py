import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *

from ui_readeerdialog import Ui_Dialog
from ui_bookdialog import Ui_BookDialog
from ui_mainwindow import Ui_MainWindow

class DatabaseManager():
    def __init__(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("127.0.0.1")
        self.db.setUserName("root")
        self.db.setPassword("123123")
        self.db.setDatabaseName("biblioteka")
        self.connect()

    def connect(self):
        isOpen = self.db.open()
        if not isOpen:
            print(self.db.lastError().text())

        else:
            print("connected")
            self.initializeOrdersModel()

    def initializeOrdersModel(self):
        self.modelOrders = QSqlTableModel()
        self.modelOrders.setTable("zamowienie")
        self.modelOrders.select()

    def initializeBooksModel(self):
        self.modelBooks = QSqlTableModel()
        self.modelBooks.setTable("ksiazka")
        self.modelBooks.select()

    def initializeReadersModel(self):
        self.modelReaders = QSqlTableModel()
        self.modelReaders.setTable("czytelnik")
        self.modelReaders.select()

dbManager = DatabaseManager()

class BookDialog(QDialog, Ui_BookDialog):
    def __init__(self):
        super(BookDialog, self).__init__()

        self.setupUi(self)
        self.setWindowTitle("Książka")

        dbManager.initializeBooksModel()
        self.tableViewBooks.setModel(dbManager.modelBooks)

class ReaderDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super(ReaderDialog, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Czytelnicy")

        dbManager.initializeReadersModel()
        self.tableViewReaders.setModel(dbManager.modelReaders)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Biblioteka")
        self.initConnections()

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