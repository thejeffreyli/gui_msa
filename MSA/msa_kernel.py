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

    def read_data(self, order, symmetry, train_x):
        
        arg = order +' '+ symmetry

        print("")
        print("Generating the fitting bases... (This might take time) \n")

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
        print("PASS")
        
        print('1. Input file info:')
        print('Number of atoms is : ' + str (natom))
        print('Number of configurations is: '+str(nconfig)+'\n')