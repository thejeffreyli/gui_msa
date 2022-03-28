## Python Graphical User Interface (GUI) Application for Monomial Symmetrization for Potential Energy Surface (PES) Fitting

### Description

TBA

### Original Work by Kee Wang, Chen Qu, Zhen Xie, and Joel Bowman
* [GitHub](https://github.com/Kee-Wang/PES-Fitting-MSA)
* [Blog](https://scholarblogs.emory.edu/bowman/msa/)

### Contents

* [Readings](./Readings): Available PDFs of helpful literature.
* [versions](./versions): Repository for current and past versions of program. Last updated 03/22/2022.
* [DailyLog.md](./DailyLog.md): Day-to-day journals documenting updates that occur when working on the project.
* [Original_MSA](./Original_MSA): Original source code by Wang and group. 


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
* Helpful [link](https://estuarine.jp/2021/03/install-oneapi/?lang=en) for tips on properly installing iFort. <!--- (i.e. source /opt/intel/oneapi/setvars.sh) -->

GUI Development:
* PyQt5 5.15.6
* pyqt5-tools > [QtDesigner](https://doc.qt.io/qt-5/qtdesigner-manual.html) 
* [Helpful tutorial](https://www.techwithtim.net/tutorials/pyqt5-tutorial/how-to-use-qtdesigner/)

Working in Ubuntu 20.04:
* [Xming](https://sourceforge.net/projects/xming/)
* [Anaconda for Linux](https://www.digitalocean.com/community/tutorials/how-to-install-the-anaconda-python-distribution-on-ubuntu-20-04)

### Instructions on Running Program

![Interface](./versions/gui_msa_0.02/msa_0322.png)



(1) Input Section

    (A) Max Order: Input the polynomial order you would like to use for the fitting.
        In our example we use 4. The number of coefficients increases
        rapidly when the polynomial order becomes larger. So you may want
        to start with low polynomial orders.
    (B) Input the molecular formula (or the permutational symmetry group)
        Our example is H2-H2O, and we use 2 2 1 here. The full symmetry is
        4 1, but we don't expect any H exchange between H2 and H2O, so
        2 2 1 is also a reasonable choice.
    (C) Input the name of the data file, which is "points.dat".

(3) The program tells you the number of coefficients and the number of
    points in the data file. And it asks you if you would like to continue.
    If the number of coefficients is too small (which leads to large
    fitting error), or too large (which may cause over-fitting), you can
    type "n" to terminate and then pick another polynomial order. If you
    would like continue, just enter y, and the program will continue.

(4) The program asks you if you would like to apply weight to the points
    in the fitting. If you would like to apply weight, just input the
    parameter, as instructed by the program. If you don't want to weight
    data, just enter "n".

(5) The program asks you to input the a0 parameter (in unit Bohr) used
    in the Morse variable yij = exp(-rij/a0). Just enter the value you
    would like to use. We recommend values between 2.0 and 3.0 Bohr.

(6) The program fits the potential energy surface and when it finishes,
    the root-mean-square fitting error is printed on the screen.
    The coefficients of the fit is written in "coeff.dat", and three
    Fortran code files "pes_shell.f90", "basis.f90", and "gradient.f90"
    are also generated.

(7) The test program "getpot.x" is compiled, and if you would like to run
    the test, use the command
    ./getpot.x test.xyz
    The results is written in test.out, and if you use polynomial order 4
    and symmetry group 2 2 1 as we did in the video, the results in the
    "test.out" should be the same as those in "expected.out". Of course,
    small numerical error is allowed.

(8) If you would like to use the fit in your own program, pes_shell.f90,
    basis.f90, gradient.f90, and coeff.dat are necessary. Copy these four
    files to the folder that contains your own program, and in your own
    Fortran code, insert "use pes_shell", and "call pes_init()", (as we
    do in the "getpot.f90" example), and you can calculate the potential
    of any configuration using the "f" function, and the gradient using the
    "g" function.


### Acknowledgements

Collaborators: Dr. Joel Bowman, Dr. Chen Qu
If you have any questions, please contact [Jeffrey Li](jeffrey.k.li98@gmail.com).






