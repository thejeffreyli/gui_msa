### Software Used

Requirements: To use this software, you need a Fortran 90, a C++ compiler, a linear algebra library, Perl and Python.

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
* Helpful [link](https://estuarine.jp/2021/03/install-oneapi/?lang=en) for tips on properly initializing ifort. <!--- (i.e. source /opt/intel/oneapi/setvars.sh) -->

GUI Development:
* PyQt5 5.15.6
* pyqt5-tools > [QtDesigner](https://doc.qt.io/qt-5/qtdesigner-manual.html) 
* [Helpful tutorial](https://www.techwithtim.net/tutorials/pyqt5-tutorial/how-to-use-qtdesigner/)

Working in Ubuntu 20.04:
* [Xming](https://sourceforge.net/projects/xming/)
* [Anaconda for Linux](https://www.digitalocean.com/community/tutorials/how-to-install-the-anaconda-python-distribution-on-ubuntu-20-04)


### Instructions for Version 0.05

Using Linux environment, on CMD prompt: python3 msa_main.py 

![Interface](./msa_0408.png)

Input:
* Max Order: Input the polynomial order you would like to use for the fitting. (example: 4)
* Permutation Symmetry: Input the molecular formula (or the permutational symmetry group). (example: 2 2 1)
* Data File Name: Input the name of the data file. (example: points.dat)
* Generate Basis: Uses the data provided in previous steps to generate basis. 

Output: 
* The program displays the number of coefficients and the number of configurations in the data file. If the number of coefficients is too small (which leads to large fitting error) or too large (which may cause over-fitting), you can Exit the program and then pick another polynomial order. You can Continue if satisfied.
* Continue: Saves the values in an output.txt file. Moves on to next step.
* Exit: Saves the values in an output.txt file and terminates program.

Weights: 
* Input: If you would like to apply weight, input the parameter. If you do not want to add weight, enter "n". Moves on to next step.

Parameters: 
* Input: Enter the a0 parameter you would like to use. We recommend values between 2.0 and 3.0 Bohr. Moves on to next step.

Fitting: The program fits the potential energy surface and when it finishes, the root-mean-square fitting error (RMSE) and weighted RMSE are displayed. The coefficients of the fit is written in "coeff.dat", and three Fortran code files "pes_shell.f90", "basis.f90", and "gradient.f90" are also generated.
* Compute: Generates fits and displays RMSE.
* Exit: Saves the values in an output.txt file and terminates program.

Reset:
* Resets the directory to default. Removes everything, including ALL output files. Be sure to save all desired files in another location prior to resetting.
* Terminates program when finished.



