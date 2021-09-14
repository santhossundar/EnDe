'''
Name: EnDe
About: Password Manager with GUI
Project Link: https://github.com/santhoshsunthar/EnDe

'''

from PyQt5 import QtCore, QtGui, QtWidgets
from endeSecondWindow import Ui_Dialog
from endeEncrypter import ende
import sqlite3
from endeMainWindow import Ui_MainWindow

class secondWindow(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super(secondWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('logos/EnDeLogo.ico'))

        self.ui.pushButton.clicked.connect(self.insertData)

    def dbConnection(self):
        self.db = sqlite3.connect("data.db")
        self.cur = self.db.cursor()
        self.cur = self.cur.execute("CREATE TABLE IF NOT EXISTS datas(account TEXT, password TEXT)")

    def insertData(self):
        self.dbConnection()
        acc = self.ui.lineEdit.text()
        passw = self.ui.lineEdit_2.text()
        key = self.ui.lineEdit_3.text()

        en_password = ende(key, passw).createCipher()

        if (acc != '' and passw != '' and key != ''):
            self.cur.execute("INSERT INTO datas (account, password) VALUES (?,?)" ,(acc, memoryview(en_password)))
            self.db.commit()
            self.cur.close()
            self.db.close()
            QtWidgets.QDialog.close(self)
            
        else:
            QtWidgets.QMessageBox.information(QtWidgets.QMessageBox(), 'Error', 'All Fields are required!')
            


        



    

