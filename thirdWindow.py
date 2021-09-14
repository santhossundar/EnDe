'''
Name: EnDe
About: Password Manager with GUI
Project Link: https://github.com/santhoshsunthar/EnDe

'''

from PyQt5 import QtCore, QtGui, QtWidgets
from endeThirdWindow import Ui_Dialog
import hashlib
from Cryptodome.Cipher import AES
import sqlite3

class thirdWindow(QtWidgets.QDialog):
    def __init__(self, passw, parent = None):
        super(thirdWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('logos/EnDeLogo.ico'))

        self.passw = passw
        self.dbConnection()
        self.ui.pushButton.clicked.connect(self.decrypt)

    def dbConnection(self):
        db = sqlite3.connect('data.db')
        cur = db.cursor()

        cur.execute("SELECT * FROM datas")
        data = cur.fetchall()

        for i in range(len(data)):
            if(str(data[i][1]) == self.passw):
                self.bytePassw = data[i][1]
            elif (data[i][0] == self.passw):
                self.bytePassw = data[i][1]
            
        cur.close()
        db.close()

    def decrypt(self):
        key = self.ui.lineEdit.text()
        
        hashedKeySalt = dict()
        userKey = bytes(key, "utf-8")
        userSalt = bytes(key[::-1], "utf-8")
        hashType = "SHA256"
        hash = hashlib.new(hashType)
        hash.update(userKey)
        hashedKeySalt["key"] = bytes(hash.hexdigest()[:32], "utf-8")
        hash = hashlib.new(hashType)
        hash.update(userSalt)
        hashedKeySalt["salt"] = bytes(hash.hexdigest()[:16], "utf-8")

        deCipherObject = AES.new(hashedKeySalt["key"],AES.MODE_CFB,hashedKeySalt["salt"])
        decryptedContent = deCipherObject.decrypt(self.bytePassw)
        
        self.ui.lineEdit_2.setText(str(decryptedContent).replace('b', '').replace('\'',''))
    
    