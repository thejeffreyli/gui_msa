## Week 0: Requirements, Setting Up

<br />

### Original Work
* [GitHub](https://github.com/Kee-Wang/PES-Fitting-MSA)
* [Blog](https://scholarblogs.emory.edu/bowman/msa/)

### Requirements
To use MSA software, you need a
* Fortran 90 and a C++ compiler;
* "dgelss" subroutine from LAPACK
* Perl and Python

### Software Used
MSA Software:
* Python 3.8.8 / Spyder
* [Perl 5.34.0](https://www.activestate.com/products/perl/)
* Ubuntu 20.04 - Linux Environment (Windows Store)
* build-essential (g++ compiler, sudo apt-get install build-essential)
* [Intel® oneAPI Base Toolkit for Linux](https://www.intel.com/content/www/us/en/developer/tools/oneapi/base-toolkit-download.html): 
    (1) Intel® oneAPI Math Kernel Library

* [Intel® oneAPI HPC Toolkit for Linux](https://www.intel.com/content/www/us/en/developer/tools/oneapi/hpc-toolkit-download.html):
    (1) Intel® Fortran Compiler Classic
    (2) Intel® C++ Compiler Classic
* Helpful [link](https://estuarine.jp/2021/03/install-oneapi/?lang=en) for tips on properly installing iFort. (i.e. source /opt/intel/oneapi/setvars.sh)

GUI Development:
* PyQt5 5.15.6
* pyqt5-tools > [QtDesigner](https://doc.qt.io/qt-5/qtdesigner-manual.html) 
* [Helpful tutorial](https://www.techwithtim.net/tutorials/pyqt5-tutorial/how-to-use-qtdesigner/)


## Week 1: 

### March 8, 2022 (Day 1)
Updates:
* Designing template for GUI. Testing inputs and outputs. 
* Inputs: 
    (1) Please input the maximum order of the polynomial: int value, ex: 4
    (2) Please input the maximum order of the polynomial: int values separated by space, ex: 2 2 1
    (3) Please input the name of the data file: string name of file, ex: points.dat
* Outputs: 
    1. Input file info:
    Number of atoms is : 5
    Number of configurations is: 44623.0

    2. Polynomial info:
    Given polynomial order: 4
    Given symmetry: 2 2 1
    Number of coefficients is: 323


### March 9, 2022 (Day 2)
Updates:
* Implementing backend logic. 