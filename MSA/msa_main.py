# from PyQt5 import QtCore
from msa_ui import Ui_MSA as Ui
from msa_kernel import MSA_Func
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

import os
import sys
import logging


# pyuic5 -x test.ui -o test_ui.py


class testWin(QtWidgets.QMainWindow, Ui):
    def __init__(self, path=None):

        super(testWin, self).__init__()
        self.setupUi(self)
        self.mk = MSA_Func()
        
        
        # self.button1.clicked.connect(self.button_click)
        
        
        self.button1.clicked.connect(self.load)
    def load(self):
        # shost is a QString object
        order = self.lineEdit.text()
        symmetry = self.lineEdit_2.text()
        train_x = self.lineEdit_3.text()
        self.mk.read_data(order, symmetry, train_x)
        


def run():

    app = QtWidgets.QApplication(sys.argv)
    win = testWin()
    win.show()
    # sys.exit(app.exec_())
    app.exec_()

if __name__ == '__main__':
    run()
    
