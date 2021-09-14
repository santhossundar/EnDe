'''
Name: EnDe
About: Password Manager with GUI
Project Link: https://github.com/santhoshsunthar/EnDe

'''

import sys
from PyQt5 import QtGui, QtWidgets
from mainWindow import MainWindow

def main():
    app = QtWidgets.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

