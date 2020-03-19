# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newreaderdialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewReaderDialog(object):
    def setupUi(self, NewReaderDialog):
        NewReaderDialog.setObjectName("NewReaderDialog")
        NewReaderDialog.resize(374, 142)
        self.verticalLayout = QtWidgets.QVBoxLayout(NewReaderDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(NewReaderDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEditName = QtWidgets.QLineEdit(NewReaderDialog)
        self.lineEditName.setObjectName("lineEditName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditName)
        self.label_2 = QtWidgets.QLabel(NewReaderDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEditSurname = QtWidgets.QLineEdit(NewReaderDialog)
        self.lineEditSurname.setObjectName("lineEditSurname")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditSurname)
        self.label_3 = QtWidgets.QLabel(NewReaderDialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEditTel = QtWidgets.QLineEdit(NewReaderDialog)
        self.lineEditTel.setObjectName("lineEditTel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditTel)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(NewReaderDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(NewReaderDialog)
        self.buttonBox.accepted.connect(NewReaderDialog.accept)
        self.buttonBox.rejected.connect(NewReaderDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(NewReaderDialog)

    def retranslateUi(self, NewReaderDialog):
        _translate = QtCore.QCoreApplication.translate
        NewReaderDialog.setWindowTitle(_translate("NewReaderDialog", "Dialog"))
        self.label.setText(_translate("NewReaderDialog", "Imie:"))
        self.label_2.setText(_translate("NewReaderDialog", "Nazwisko:                    "))
        self.label_3.setText(_translate("NewReaderDialog", "Telefon:"))
