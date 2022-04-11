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
Updates:
* Asked Chen for assistance with transferring data from Fortran to Python, since fitting was performed in f90. He suggested saving in temp file and reading file to Python. He provided revised msa.py. 
* Modified Chen's code to suit msa_kernel.py. Instead of saving file as temp, I saved as txt file. 
* Fitting results are displayed on GUI. 

## Week 3 - : Cleaning Code and Documenting

### March 22, 2022 (Day 10)
Updates:
* Made some revisions in GUI template to improve readability and design. 
* Included functions for saving data into txt files before exiting program. 
* Began documentation/guide of program.

### March 28, 2022 (Day 11)
Updates:
* Implemented documentation and release information on GitHub repo.

### March 29-30, 2022 (Day 12-13)
Bugs reported in 0.02 by Chen:
* Texts may still be incomplete on other platforms.
* Modify the third line in the file “src/Makefile” by changing “LIBS = -mkl=sequential” to “LIBS = -qmkl=sequential”. The new Intel MKL changes its syntax a bit so the latest is
-qmkl=xxx instead of -mkl=xxx.
* In msa_kernel.py, replace “./postemsa.pl” and “./derivative.pl” with “perl postemsa.pl” and “perl derivative.pl”, respectively. 

Updates:
* Addressed issue regarding scalability across different screen resolutions. Reached out to Miaoqi from Argonne APS. 
* Completely redesigned msa.ui with Qt designer. Used Layouts for textlabels. 
* Made changes to Makefile and msa_kernel.py.

### March 31, 2022 (Day 14)
Bugs reported in 0.03 by Chen:
* Recurring text visibility issue on different platforms. 
* temp_rmse.txt is not generated. Error occurs when the program later attempts to open this file and read the RMSE.

Updates:
* Troubleshooting issues with qlabel. Figured it might have to do with screen resolution I am developing in. 
* Redesigned ui template again with smaller laptop resolution rather than desktop monitor resolution. Seems to resolve issue.
* Added function for resetting directory to default.


### April 7, 2022 (Day 15)
Bugs:
* GUI crashes when computing. Missing temp_rmse.txt file.
make: ifort: Command not found
make: *** [Makefile:10: basis.o] Error 127
cp: cannot stat './src/fit.x': No such file or directory
/bin/sh: 2: ./fit.x: not found
rm: cannot remove 'fit.x': No such file or directory
make: ifort: Command not found
make: *** [Makefile:10: basis.o] Error 127
Traceback (most recent call last):
  File "/mnt/c/users/jeffr/downloads/gui_msa_0.02/msa_main.py", line 80, in compute
    self.mk.extract_rmse()
  File "/mnt/c/users/jeffr/downloads/gui_msa_0.02/msa_kernel.py", line 337, in extract_rmse
    with open('temp_rmse.txt') as f:
FileNotFoundError: [Errno 2] No such file or directory: 'temp_rmse.txt'
Aborted (core dumped)

Updates:
* Minor changes to GitHub repo directory.
* Meeting with Dr. Bowman and Chen on GUI. New bug reported. GUI crashes at 'Compute' module. Error message shown above. 
* Appears all previous and current versions crash upon computing, despite previously working fine. 
* Files that are not generated by GUI: 'coeff.dat', 'points.eng', 'temp_rmse.txt'. Files created during 'Compute.'
* Error found. Did not initialize oneAPI environment. I forgot to intitialize mine when starting Ubuntu. Without intializing, I would receive errors when computing fits. Chen did not have issue when he ran the GUI on his end so I did not suspect this to be a problem for all users. More info on [OneAPI](https://www.intel.com/content/www/us/en/develop/documentation/get-started-with-intel-oneapi-dlfd-linux/top/before-you-begin.html). 


### April 8, 2022 (Day 16)
Updates:
* Added new Read section on GUI template to warn users of software requirements.
* Added software requirements/used on ReadMe files. 


### April 11, 2022 (Day 17)
Updates:
* Updated Read section to reference instructions on GitHub. Added text instructions on Fitting section. Updated text on Reset Section.
* Chen suggested having texts show up on the GUI after the users click buttons. This will help users know what to do next. Currently, nothing appears in the frontend when 'Continue,' 'Exit' (2x), 'Input' (2x), etc. are pressed. 
* Implemented popup messages that appear whenever buttons are clicked to inform users on successful backend actions and provide information on what to do next. 
* Improved backend logic. If inputs are left blank, an error message will pop up for users to check arguments and try again. 