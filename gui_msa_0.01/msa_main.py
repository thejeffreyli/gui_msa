# from PyQt5 import QtCore
from msa_ui import Ui_MainWindow as Ui
from msa_kernel import MSA_Func
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

from PyQt5.QtWidgets import QApplication

import os
import sys
import logging
import time

# pyuic5 -x msa.ui -o msa_ui.py
# source /opt/intel/oneapi/setvars.sh

# GUI Class
class testWin(QtWidgets.QMainWindow, Ui):
    def __init__(self, path=None):

        super(testWin, self).__init__()
        self.setupUi(self)
        self.mk = MSA_Func()

        self.button1.clicked.connect(self.load) # generate basis
        self.button2.clicked.connect(self.test_1) # yes: saves values
        self.button3.clicked.connect(self.test_2) # no: saves and exit
        self.button4.clicked.connect(self.weights) # weights
        self.button5.clicked.connect(self.param) # parameters
        # self.button5.clicked.connect(self.test_2) # save
        
    # load data        
    def load(self):
        order = self.lineEdit.text()
        symmetry = self.lineEdit_2.text()
        train_x = self.lineEdit_3.text()
        
        # self.label_9.setText(str(4))
        self.mk.read_data(order, symmetry, train_x)
        
        self.textBrowser.setText(str(self.mk.outputs["natom"]))
        self.textBrowser_2.setText(str(self.mk.outputs["nconfig"]))
        self.textBrowser_3.setText(str(self.mk.outputs["order"]))
        self.textBrowser_4.setText(str(self.mk.outputs["symmetry"]))
        self.textBrowser_5.setText(str(self.mk.outputs["ncoeff"]))
        

    def test_1(self):
        # TODO
        return
    
    def test_2(self):
        # TODO
        QApplication.quit() 
        return
    
    def weights(self):
        ans = self.lineEdit_4.text()
        if ans=='n':
            wt = '1.e10'
        else:
            wt = ans
        print(wt)
        self.mk.update_wt(wt)
        
    def param(self):
        ans = self.lineEdit_5.text()
        a0 = ans+'d0'
        print(a0)
        self.mk.update_a0(a0)
        
        
        
# run GUI
def run():

    app = QtWidgets.QApplication(sys.argv)
    win = testWin()
    win.show()
    # sys.exit(app.exec_())
    app.exec_()

if __name__ == '__main__':
    run()
    
