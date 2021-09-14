'''
Name: EnDe
About: Password Manager with GUI
Project Link: https://github.com/santhoshsunthar/EnDe

'''

from PyQt5 import QtGui, QtWidgets
from endeMainWindow import Ui_MainWindow
from secondWindow import secondWindow
from thirdWindow import thirdWindow
import sqlite3
import sys

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.secondWindow)
        self.ui.pushButton_2.clicked.connect(self.refresh)
        self.ui.pushButton_3.clicked.connect(self.delete)

        self.ui.tableWidget.cellDoubleClicked.connect(self.tableClick)
        
        self.setData()

    def dbConnection(self):
        self.db = sqlite3.connect("data.db")
        self.cur = self.db.cursor()

    def delete(self):
        try:
            ind = self.ui.tableWidget.selectionModel().selectedRows()
            ind2 = self.ui.tableWidget.selectionModel().currentIndex()
            val = ind2.sibling(ind2.row(), ind2.column()).data()
            
            for i in sorted(ind):
                self.ui.tableWidget.removeRow(i.row())
                
            self.dbConnection()
            self.cur.execute("DELETE FROM datas WHERE account = (?)", (val,))
            self.db.commit()
            self.cur.close()
            self.db.close()
            
        except Exception:
            print('Nothing Selected')


    def tableClick(self):
        index = self.ui.tableWidget.selectionModel().currentIndex()
        value = index.sibling(index.row(), index.column()).data()

        self.thirdWin = thirdWindow(value)
        self.thirdWin.show()
     
    def setData(self):
        try:
            self.dbConnection()
            self.cur.execute("SELECT * FROM datas")
            data = self.cur.fetchall()
            self.cur.close()
            self.db.close()
            
            self.ui.tableWidget.setRowCount(1)

            for i in range(self.ui.tableWidget.rowCount()):
                accCount = len(data)
                self.ui.tableWidget.setRowCount(accCount)
                i+=1

                for j in range(0,accCount):
                        self.ui.tableWidget.setItem(j,0, QtWidgets.QTableWidgetItem(data[j][0]))
                        self.ui.tableWidget.setItem(j,1, QtWidgets.QTableWidgetItem(str(data[j][1])))
                        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
                        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        except Exception as e:
            print(e)

    def secondWindow(self):
        self.secondWin = secondWindow()
        self.secondWin.show()

    def refresh(self):
        self.setData()
