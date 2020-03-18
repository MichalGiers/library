import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *

class DatabaseManager():
    def __init__(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("127.0.0.1")
        self.db.setUserName("mat")
        self.db.setPassword("s")
        # self.db.setUserName("root")
        # self.db.setPassword("123123")
        self.db.setDatabaseName("biblioteka")
        self.connect()

    def connect(self):
        isOpen = self.db.open()
        if not isOpen:
            print(self.db.lastError().text())

        else:
            print("connected")
            self.initializeOrdersModel()

    def addNewReader(self, name, surname, tel):
        query = QSqlQuery(self.db)
        query.prepare("INSERT INTO czytelnik (`imie`, `nazwisko`, `telefon`) VALUES (:imie, :nazwisko, :telefon)")
        query.bindValue(":imie", name)
        query.bindValue(":nazwisko", surname)
        query.bindValue(":telefon", tel)

        if not query.exec_():
            print(query.lastError().text())
            print("add reader error")

        self.modelReaders.select()

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
        self.modelReaders.setHeaderData(1, Qt.Horizontal, "IMIE")
        self.modelReaders.setHeaderData(2, Qt.Horizontal, "NAZWISKO")
        self.modelReaders.setHeaderData(3, Qt.Horizontal, "TELEFON UŻYTKOWNIKA")
        self.modelReaders.select()

    def getModelDetails(self, id):
        self.modelDetails = QSqlQueryModel()
        que = "SELECT * FROM zamowienieKsiazka where zamowienie_id="
        que += str(id)
        self.modelDetails.setQuery(que)
        return self.modelDetails

    def removeReader(self, id):
        print('removeReader')
        query = QSqlQuery(self.db)
        queryStr = "delete from czytelnik where id_czytelnik="
        queryStr += str(id)

        query.prepare(queryStr)
        if not query.exec_():
            print(query.lastError().text())
            print("removeReader error")

        self.modelReaders.select()


dbManager = DatabaseManager()