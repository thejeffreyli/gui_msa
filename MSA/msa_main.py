# from PyQt5 import QtCore
from msa_ui import Ui_MainWindow as Ui
from msa_kernel import MSA_Func
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

import os
import sys
import logging


# pyuic5 -x msa.ui -o msa_ui.py

# GUI Class
class testWin(QtWidgets.QMainWindow, Ui):
    def __init__(self, path=None):

        super(testWin, self).__init__()
        self.setupUi(self)
        self.mk = MSA_Func()

        self.button1.clicked.connect(self.load)
        self.button2.clicked.connect(self.load)
        # self.button3.clicked.connect()
        
        
    # load data        
    def load(self):
        outputs = self.create_dict()
        order = self.lineEdit.text()
        symmetry = self.lineEdit_2.text()
        train_x = self.lineEdit_3.text()
        
        
        # self.label_9.setText(str(4))
        outputs = self.mk.update(order, symmetry, train_x, outputs)
        
        self.textBrowser.setText(str(outputs["num_atoms"]))
        self.textBrowser_2.setText(str(outputs["num_conf"]))
        self.textBrowser_3.setText(str(outputs["poly_order"]))
        self.textBrowser_4.setText(str(outputs["symm"]))
        self.textBrowser_5.setText(str(outputs["num_coef"]))
        
    def create_dict(self):
        outputs = {"num_atoms": 0, "num_conf": 0, "poly_order": 0, "symm": 0,
                   "num_coef": 0}
        
        return outputs
    
    def  
    

# run GUI
def run():

    app = QtWidgets.QApplication(sys.argv)
    win = testWin()
    win.show()
    # sys.exit(app.exec_())
    app.exec_()

if __name__ == '__main__':
    run()
    
'''

    def load(self):
        fname = self.fname.text()
        blemish_fname = self.blemish_fname.text()
        text_fname = self.text_fname.text() 


        if not os.path.isfile(blemish_fname):
            blemish_fname = None
        if not os.path.isfile(fname):
            return

        self.sm.read_data(fname, blemish_fname, text_fname)

        self.db_cenx.setValue(self.sm.meta['bcx'])
        self.db_ceny.setValue(self.sm.meta['bcy'])
        self.db_energy.setValue(self.sm.meta['energy'])
        self.db_pix_dim.setValue(self.sm.meta['pix_dim'])
        self.db_det_dist.setValue(self.sm.meta['det_dist'])
        self.le_shape.setText(str(self.sm.shape))
        self.groupBox.repaint()
        self.plot()
'''