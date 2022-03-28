## Week 0: Requirements, Setting Up

<br />

### Original Work by Kee Wang, Chen Qu, and Zhen Xie
* [GitHub](https://github.com/Kee-Wang/PES-Fitting-MSA)
* [Blog](https://scholarblogs.emory.edu/bowman/msa/)

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


## Week 1: Developing Workflow and Backend Logic

### March 8, 2022 (Day 1)
Updates:
* Begin designing template for first stage of workflow using QtDesigner. Example process shown below. 
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
* Testing inputs and outputs. 
* Explanation: User inputs three values into GUI. GUI will output and display five values for user. User can decide to proceed or not to proceed given information. 


### March 9, 2022 (Day 2)
Updates:
* Implementing backend logic for inputs and outputs. This includes number inputs and button functions.

### March 11, 2022 (Day 3)
Updates:
* Display output values onto GUI.
* Designed template for remaining workflow. Example process shown below. 
We can apply weight in the fitting, and the weight of each point is given by
wt = E0/(E0+dE), where dE is the energy of that point relative to the minium.
E0 is a user-specified parameter (in unit Hartree).

If you would like to apply the weight, please input the E0 parameter. Otherwise
please enter "n":
n


Please specify the a0 parameter (in unit Bohr) used in Morse variable
yij = exp(-rij/a0). The recommended range is 2.0-3.0 Bohr:
3
ifort: command line remark #10412: option '-mkl=sequential' is deprecated and will be removed in a future release. Please use the replacement option '-qmkl=sequential'
b'ifort -r8 -O -c basis.f90\nifort -r8 -O -c fit.f90\nifort -r8 -O -o fit.x basis.o fit.o -mkl=sequential\n'
Fitting... (This might take time)

b'3. Fitting is finished: \nOverall Root-mean-square fitting error:    0.0001163307 Hartree\nWeighted Root-mean-square fitting error:    0.0001163307 Hartree\n'
ifort: command line remark #10412: option '-mkl=sequential' is deprecated and will be removed in a future release. Please use the replacement option '-qmkl=sequential'
b'ifort -r8 -O -c basis.f90\nifort -r8 -O -c gradient.f90\nifort -r8 -O -c pes_shell.f90\nifort -r8 -O -c getpot.f90\nifort -r8 -O -o getpot.x basis.o gradient.o pes_shell.o getpot.o -mkl=sequential\n'
4. In order to run the test program, use command:
./getpot.x test.xyz

End of program
* Explanation: User will need to specify weight and a0 parameters. Then, the RMS fitting will be computed. 

### March 12, 2022 (Day 4)
Updates:
* Encountered error message whenever attempting to run GUI on Ubuntu. Tried troubleshooting and Google. Will have to ask Chen for assistance. 

qt.qpa.xcb: could not connect to display
qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

Available platform plugins are: eglfs, linuxfb, minimal, minimalegl, offscreen, vnc, wayland-egl, wayland, wayland-xcomposite-egl, wayland-xcomposite-glx, webgl, xcb.

Aborted (core dumped)


## Week 2: Overcoming Linux Error


### March 14-15, 2022 (Day 5 and 6)
Updates:
* Decided to work more on developing backend logic to not waste time. Using sample input/outputs. 
* Impemented universal dictionary to easily store and access values. 
* Added functions to existing buttons. 
* Transferred/Converted remaining msa.py code into msa_kernel.py. 

### March 17, 2022 (Day 7)
Updates:
* Installed Anaconda for Linux. 
* Installed Xming for Windows (for graphics).
* Chen's instructions for overcoming errors. 
(1) First open Xming. Xming will be running in the background so you won’t notice it’s running until you run Linux applications that has GUI.
(2) Open your Ubuntu terminal and go to your home directory. You can use a shortcut command “cd ~” to go to your home directory.
(3) Type command “ls -a” and see if you can find a file called “.bashrc” (or sometimes you cannot find “.bashrc” but a “.bash_profile” exists.) Finding either of them is fine. Note the file name starts with a dot. These files are hidden in Linux, but “-a” flag in the “ls” command allows you to see all the hidden files.
(4) Modify the “.bashrc” (or “.bash_profile”). Open it with your favorite Linux text editor and insert a line “export DISPLAY=127.0.0.1:0” (without the quotation marks) to that file and save it.
(5) Start a new Ubuntu terminal (the modification in .bashrc will only be effective in a new terminal). Try xclock in that new terminal and see if you still get that error.

### March 18-19, 2022 (Day 8 and 9)
* Asked Chen for assistance with transferring data from Fortran to Python, since fitting was performed in f90. He suggested saving in temp file and reading file to Python. He provided revised msa.py. 
* Modified Chen's code to suit msa_kernel.py. Instead of saving file as temp, I saved as txt file. 
* Fitting results are displayed on GUI. 

## Week 3: Cleaning Code and Documenting

### March 22, 2022 (Day 10)
* Made some revisions in GUI template to improve readability and design. 
* Included functions for saving data into txt files before exiting program. 
* Began documentation/guide of program.
