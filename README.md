# KPIM24COM Machine Learning and Computer Vision

This repository contains the code examples you will work on during lectures and labs and afterwards when you are working on your assignments.

Code and documentation comes in Jupyter notebook files (.ipynb), or directly in Python script files (.py). Note that you can import functions and objects defined in Python scripts inside Jupyter notebooks. That way you can interactively work with data inside your notebooks, but encapsulate your code inside script files.

## Updates

The repository will be added to during the running of the module, both to correct any mistakes and also to add new material including new files. Therefore please ensure you keep your local copies up to date with any changes.

Since you will want to make your own changes locally, the standard method for keeping things updated is to have two git remotes associated with the repository: your own private one, and the original one. If you wish to do this, please take the following steps after creating an empty private repository on https://github.com/Pramod645/Mechine-Learning-Algorithms

```bash
# clone to a new directory
git clone <this repository URL> <name of directory>
# go in to the new local copy
cd <name of directory>
# change the remote name to upstream
git remote rename origin upstream
# add a second remote for your own changes
git remote add origin <your private repository URL>
```

*Alternative recommendation:* Since resolving conflicts between Jupyter notebooks can be time consuming, an alternative and easier approach is simply *not to edit your local clone* and instead to copy any files you wish to work on elsewhere. That way there will be no git conflicts when you do an update.

Either way, to update the lab code you need to run the following command from within your local git directory.

```bash
git pull
```

This will try to merge any new changes appearing in the remote. If there are conflicts with your own changes you will need to resolve them at this point.

## About

The code was written and tested with Python 3.6, though other Python versions (including Python 2.7) should work in nearly all cases.

The code uses the core libraries essential for working with data in Python: particularly [IPython](http://ipython.org), [NumPy](http://numpy.org), [Pandas](http://pandas.pydata.org), [Matplotlib](http://matplotlib.org), [Scikit-Learn](http://scikit-learn.org), and related packages. See the *Anaconda* section below for instructions on getting all of these set up quickly on any platform, and the *Additional Packages* section for how to add new modules.

Familiarity with Python as a language is assumed; if you need a quick introduction to the language itself, see the free project [A Whirlwind Tour of Python](https://github.com/jakevdp/WhirlwindTourOfPython).

Familiarity with using Git to manage code repositories is assumed; if you need a quick introduction or reminder covering version control with Git, see the official Github tutorial [Try Git](https://try.github.io/) or the simple Git guide [Git Guide](http://rogerdudler.github.io/git-guide/).

## Anaconda

Anaconda is a package and environment manager for Python, geared towards scientists and researchers. It removes almost all of the effort in setting up and managing an environment for scientific computing.

The [Official Guide](https://conda.io/docs/user-guide/getting-started.html) should take around 25 minutes to work through. This will get you a working installation of Anaconda on any platform, which contains all of the main packages. Please ensure you install the full Anaconda environment using Python 3.x. This includes Numpy, Scipy, Sklearn, etc.

## Additional Packages

To add any new package or library you need to your environment, the command to use is:

```bash
conda install <name of library to install>
```

#### Requirements File

Once Anaconda is installed, you can install all of the additional requirements for this module with the following command. NB: ensure your active environment is the one you wish to install OpenCV to by issuing the command `source activate <name_of_your_environment>` if necessary, and also ensure your current directory is the one with the `requirements.txt` file in it.

```bash
$ conda install -f requirements.txt
```

The requirements file contains the names of the additional requirements not included in Anaconda by default.

You will not need to build or link any libraries or install any dependencies as Conda will do this for you! To check that it worked run `ipython` and from within the REPL try to import one of the additional libraries listed in `requirements.txt`, for example:

```python
In [1]: import cv2
```

There should be no errors if OpenCV installed correctly. You are now ready to run the notebooks and scripts contained in this repository.

## Running the Notebooks

The easiest way to access the code contained in this repository is as follows.

* Clone this repository locally using `git clone`.
* Change directory in to the local copy.
* From the command line run `jupyter notebook`.

This will launch a browser window containing a directory tree where you can browse the notebooks and files. Click on any to open up an editor or preview in the browser window. (Note that you can also edit the Python `.py` files directly in your text editor or IDE, of course.)

**TIP**: Open up a second command line to run scripts that you are working with. When you run `jupyter` the current shell will show the standard output from the Jupyter server.

## Sources

Various open source (Creative Commons and MIT licensed) repositories have been used to create these notebooks, including the following.

* [Scikit-Learn Online Documentation](http://scikit-learn.org/stable/documentation.html)
* [Python Data Science Handbook](http://shop.oreilly.com/product/0636920034919.do) by Jake VanderPlas
