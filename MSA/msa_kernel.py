#!/usr/bin/env python
import subprocess
import os
import shlex
import sys


if sys.version_info > (3, 0):
	raw_input = input

class MSA_Func:
    def __init__(self):
        self.test = None

    def load_meta(self, fname):
        return
    
    def cl(self, command):
        #ip::string, command line as string input
        #op::string, return value is the output of command line
        #Notice, each time when change directly, cl starts from currect directory.
        #Use three \' if you want to input multiple line
        arg = shlex.split(command)
        p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        print (output)
        return output

    # read data
    def read_data(self, order, symmetry, train_x):
        
        print("pass_1")
        
        arg = order +' '+ symmetry

        self.cl('''
        cd src
        cd emsa
        make
        cp msa ../
        cd ../
        ./msa '''+ arg +  '''
        ./postemsa.pl ''' + arg + '''
        ./derivative.pl ''' + arg + '''
        '''
        )
        
        f = open(train_x)
        nol = 0
        for line in f:
          nol=nol+1
          if nol==1:
            natom=int(line)
        nconfig = nol/(natom+2)
        f.close()        
        
        #  natom, nconfig
        
        
        f = open('./src/basis.f90')
        nol=1 #Num of lines in file
        for line in f:
          if nol==8:
            ncoeff = int(line.split(':')[1].split(')')[0])
            ncoeff = ncoeff + 1
          if nol==24:
            nmonomial = int(line.split(':')[1].split(')')[0])
            nmonomial = nmonomial + 1
            break
          nol=nol+1
        f.close()
        
        # order, symmetry, ncoeff
        
        
        return natom, nconfig, order, symmetry, ncoeff
        

    def update(self, order, symmetry, train_x, outputs):
        
        natom, nconfig, order, symmetry, ncoeff = self.read_data(order, symmetry, train_x)
        print("pass_2")
        
        outputs["num_atoms"] = natom
        outputs["num_conf"] = nconfig
        outputs["poly_order"] = order
        outputs["symm"] = symmetry
        outputs["num_coef"] = ncoeff
        
        
        
        return outputs