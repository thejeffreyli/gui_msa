# from PyQt5 import QtCore
from msa_ui import Ui_MainWindow as Ui
from msa_kernel import MSA_Func
from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QFileDialog

from PyQt5.QtWidgets import QApplication, QMessageBox

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
        self.button2.clicked.connect(self.yes_func) # yes: saves values
        self.button3.clicked.connect(self.no_func) # no: saves and exit
        self.button4.clicked.connect(self.weights) # weights
        self.button5.clicked.connect(self.param) # parameters
        self.button6.clicked.connect(self.compute) # fitting
        self.button7.clicked.connect(self.exit_) # saves and exit
        
        self.button8.clicked.connect(self.reset_) # saves and exit
        
    # load data        
    def load(self):
        
        order = self.lineEdit.text()
        symmetry = self.lineEdit_2.text()
        train_x = self.lineEdit_3.text()
        
        
        if order == "" or symmetry == "" or train_x == "":
            QMessageBox.about(self, "Title", "Cannot read input. Please check if arguments are inputted correctly and try again.")
        else:
            self.mk.read_data(order, symmetry, train_x)
            
            self.textBrowser.setText(str(self.mk.outputs["natom"]))
            self.textBrowser_2.setText(str(self.mk.outputs["nconfig"]))
            self.textBrowser_3.setText(str(self.mk.outputs["order"]))
            self.textBrowser_4.setText(str(self.mk.outputs["symmetry"]))
            self.textBrowser_5.setText(str(self.mk.outputs["ncoeff"]))
            QMessageBox.about(self, "Title", "Basis successfully generated. Please confirm Outputs section and press 'Continue' or 'Exit.'")

    def yes_func(self):
        # save current dict as txt
        with open("output.txt", 'w') as f: 
            for key, value in self.mk.outputs.items(): 
                f.write('%s: %s\n' % (key, value))
        QMessageBox.about(self, "Title", "Successfully loaded. Please continue to the Weights section.")                
        return
    
    def no_func(self):
        # save current dict as txt
        with open("output.txt", 'w') as f: 
            for key, value in self.mk.outputs.items(): 
                f.write('%s: %s\n' % (key, value)) 
        QMessageBox.about(self, "Title", "Successfully saved. Terminating program...")   
        # exit program
        QApplication.quit() 
        return
    
    def weights(self):
        ans = self.lineEdit_4.text()
        
        if ans == "":
            QMessageBox.about(self, "Title", "Cannot read input. Please check if arguments are inputted correctly and try again.")        
        else:
            if ans=='n':
                wt = '1.e10'
            else:
                wt = ans
            self.mk.update_wt(wt)
            QMessageBox.about(self, "Title", "Successfully loaded. Please continue to the Parameters section.") 
        
    def param(self):
        ans = self.lineEdit_5.text()
        if ans == "":
            QMessageBox.about(self, "Title", "Cannot read input. Please check if arguments are inputted correctly and try again.")     
        else: 
            a0 = ans+'d0'
            self.mk.update_a0(a0)
            QMessageBox.about(self, "Title", "Successfully loaded. Please continue to the Fitting section.")
        
    def compute(self):
        self.mk.process()
        self.mk.extract_rmse()
        self.textBrowser_6.setText(str(self.mk.outputs["rmse"]))
        self.textBrowser_7.setText(str(self.mk.outputs["wrmse"]))
        QMessageBox.about(self, "Title", "Successfully completed fitting. In order to run the test program, use command: ./getpot.x test.xyz")
        
    def exit_(self):
        # save current dict as txt
        with open("output.txt", 'w') as f: 
            for key, value in self.mk.outputs.items(): 
                f.write('%s: %s\n' % (key, value))   
        
        QMessageBox.about(self, "Title", "Successfully saved. Terminating program...")
        # exit program
        QApplication.quit()                 
        return 
    
    def reset_(self):
        self.mk.clean()
        QMessageBox.about(self, "Title", "Directory successfully resetted to default. Terminating program...")
        QApplication.quit() 
        
# run GUI
def run():
    # os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "1"
    app = QtWidgets.QApplication(sys.argv)
    win = testWin()
    win.show()
    # sys.exit(app.exec_())
    app.exec_()

if __name__ == '__main__':
    run()
    
