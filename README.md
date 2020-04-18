# somappy | A Self Organizing Map Utility
Implements a Self Organizing Map algorithm based on the 
[R Kohonen SOM](https://cran.r-project.org/web/packages/kohonen/kohonen.pdf)
in Python. 


## Run the Self Organizing Map
The SOM can be run by calling the graphical user interface script (GUI):

`>> python som_selector_gui.py`

The SOM can also be run from a python script :

* Examples/SOM-Driver-Example.py
    * A simple example of how to make calls to run an SOM in a script


## Requirements for Windows
* Python 3.7+
* Numpy 
* Scipy 
* Matplotlib 
* Pandas 
* PyQt4
* Rtree 
* Scikit-Learn 
* Scikit-Image
* PySimpleGUI

If developing on Windows and unample to `>> pip install package` , 
pre-built solutions can be found at 
(https://www.lfd.uci.edu/~gohlke/pythonlibs/) where links can 
be downloaded from that site, making sure you select the correct download 
depending on your version of Python. These downloads are pre-compiled and 
made for easy Windows install. Once downloaded they can be installed from a 
command line like follows:

`>> pip install GDAl-2.3.2-cp37-cp37m-win_amd64.whl`
If you don't have __pip__ it will give you a message and tell you how to
get it.

* Microsoft Visuall C++ Build Tools (https://www.microsoft.com/en-us/download/confirmation.aspx?id=48159)
    * Download and click through setup helper


Required Packages

- numpy (Gohlke for Windows) numpy-1.14.5+mkl-cp27-cp27m-win32.whl
- scipy (Gohlke for Windows) scipy-1.1.0-cp27-cp27m-win32.whl
- scikit-learn
- scikit-image
- pandas
- matplotlib

How To:

WINDOWS:
First install numpy. If you're on Windows download numpy via the below link:
https://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy

Make sure that you download the version for you, for me it's python 2.7 and win 32, 
but perhaps you're running Python 3.6 and win 64 (probably)
Once downloaded do:

>> pip install numpy-1.14.5+mkl-cp27-cp27m-win32.whl

This can be done from the command line

Do the same for Scipy

** When a package doesn't install via pip for Windows download and install from https://www.lfd.uci.edu/~gohlke/pythonlibs/ **

MAC / Linux: ( I think )
>> pip install numpy
>> pip install scipy
>> pip install scikit-learn
>> pip install scikit-image
>> pip install pandas
>> pip install matplotlib

