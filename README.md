# Tips for Reproducible Python

### Directory Structure
---
* 	create an empty project with a base structure 

```
.
+-- data
|   +-- raw
|   +-- processed
|
+-- src
|   +-- PythonModules
|   +-- tests
|   
+-- notebooks
|   +-- exploratory
|   +-- expositionary
|
+-- references
|   +-- papers
|   +-- tutorials
|
+-- results 
+-- README.md
+-- LICENSE.txt
```

Comprehensive Project Templates:

* [Data Science Cookiecutter](https://drivendata.github.io/cookiecutter-data-science/#contributing)
* [Shablona](https://github.com/uwescience/shablona) - Python Package Template]

	
### Cross-platform Directory Paths
---

* Make paths independent of platform and all relative to directory structure

```python
	import os
	
	# current path
	current_path = os.getcwd()
	
	# join paths for Windows and Unix
	code_path = os.path.join(current_path, "src")
	
	# make sure paths/files exist before reading
	os.path_exists() 
	os.path.isfile()
```

### Testing
---
* Locally 
	* [nose](http://nose.readthedocs.io/en/latest/)

	```
		pip install nose
	```

	For each function write a test function:

	```
	+-- src
	|   +-- PythonModules
	|       +-- function1.py
	|       +-- function2.py 
	|   +-- tests
	|       +-- test_function1.py
	|       +-- test_function2.py
	```
	Use [`numpy.testing`](https://docs.scipy.org/doc/	numpy-1.12.0/reference/routines.testing.html) module.
	
	Example:
	
	
	```
		def ArraySum(array1,array2):
		   # function which sums two arrays
			return(array1 + array2)	
	```
	
	
	```
	   import numpy as np
	   
	   
	   def test_ArraySum:
	       # testing ArraySum function
			array1 = 2*np.ones(100)
			array2 = np.ones(100)
			res = arraySum(array1,array2)
			npt.assert_allequal(res, 3*np.ones(100))
	```

	Run the tests:

	```bash
		nosetests
	```

	* [pytest](https://docs.pytest.org/en/latest/)
	* [Jenkins](https://jenkins.io/) -  automatic testing, needs to be configured	 
	 





* Remotely:
	*  [Travis-CI](https://travis-ci.org/) (free for public repos)
		* specification by a [travis.yml](https://github.com/scikit-learn/scikit-learn/blob/master/.travis.yml)
	*  [AppVeyor (for Windows)](https://www.appveyor.com/) 
	*  [CircleCI](https://circleci.com/)
	*  [Wercker](http://www.wercker.com/) (based on [Docker](https://www.docker.com/) containters)
	*  [Jenkins](https://jenkins.io/) - need to configure it

	Types of tests:
	
	* unit testing
	* integration testing
	* regression testing
	* functional testing 
	
	Test Coverage - [Coveralls](https://coveralls.io/)

* Testing for Data Scientists - (PyData talk)[https://www.youtube.com/watch?v=GEqM9uJi64]	


### Distributions & Package Managers
---
Conda vs pip


What is Conda? 

* Anaconda is a Python distribution slightly different from the default Python distribution, and comes with its own package manager (conda).

* Conda packages come in the form of .whl files (wheel files). They are precompiled packages: i.e. they are compiled for each specific operating system. 
They are fast to install. (Installing Numpy from scratch takes forever compiling C code)
Miniconda is even faster to install as it is bare bones: better for deploying: have only what you need.

What is [pip](https://pip.pypa.io/en/stable/)?

Package manager for Python. Install packages from [PyPy](https://pypy.org/). There are packages in pip which are not in conda. 


`pip install` vs `conda install`

```
pip freeze

conda list
```


### Virtual Environments
---
What is a virtual environment?

A folder with all python executables and libraries and a link to them. Virtual environments take space!

Pure Python: [virtualenv](https://virtualenv.pypa.io/en/stable/)

If using anaconda distribution create envs by:

```
	conda create --name newEnv python=2 extra_packages
```

View environments:

```
	conda env list
```

On Unix:

```
source activate newEnv
do stuff
conda install more_packages
source deactivate
```

On Windows:

```
activate newEnv
do stuff
conda install more_package
deactivate
```

Saving environments:

```
	conda env export -f exported_env.yml
```

Load an environment from .yml file:

```
	conda env create -f exported_env.yml
```

You can do the same thing with pip:

```
	pip freeze > requirements.txt
	pip install -r requirements.txt
```

* Make sure to instal Jupyter within virtual environment

### More Virtualization
---
 
 * [Docker](https://www.docker.com/) 
 * [Vagrant](https://www.vagrantup.com/) 
 *  AWS public AMIs 
 *  friend's laptop

### Modules & Packages
---


  * move functions from notebooks to a module
  * paths for modules
  * reloading modules
    * python2 vs python3
  * install module as a package - setup.py (distutils)
  * submodules 
     *	put `__init__.py` in every folder
  * [git submodules](https://github.com/blog/2104-working-with-submodules) 
  
  

### Editors
---
  * [PyCharm](https://www.jetbrains.com/pycharm/) -integration with GitHub
  * [Atom](https://atom.io/) - coloring in Github (extra packages)
  * [JupyterLab](https://) (web based -> can run on server)
  * [Spyder](https://pythonhosted.org/spyder/) Matlab-like IDE
  
 Linters 
 	* for [PEP8](https://www.python.org/dev/peps/pep-0008/) style
  	* for errors: [pyflakes](https://pypi.python.org/pypi/pyflakes)   		
  	* for both: [flake8](http://flake8.pycqa.org/en/latest/)
 
 Plugins for most editors: e.g. [atom flake8 linter](https://atom.io/packages/linter-flake8).
 


### Documentation
---
  * [Nbconvert](https://nbconvert.readthedocs.io/en/latest/) - to pdf, to html
  * [Reveal.js](http://lab.hakim.se/reveal-js/#/):  Jupyter notebook -> slides  ([Instructions](http://veekaybee.github.io/presentations-the-hard-way/))
  * [css styles for notebook](https://github.com/transcranial/jupyter-themer)
  * [Sphinx](http://www.sphinx-doc.org/en/stable/) [readthedocs](https://readthedocs.org/) ...  
  * [gh-pages](https://pages.github.com/)
  * [Binder (of notebooks)] (http://mybinder.org/) (free sharing of github jupyter notebooks)(Microsoft Notebooks?)
  * [Jupyter Hub](https://jupyterhub.readthedocs.io/en/latest/) + [Kubernetes](https://kubernetes.io/) - sharing reliably with many people
  * [SageMathCloud - CoCalc](http://blog.sagemath.com/cocalc/2017/05/20/smc-is-now-cocalc.html)
  

  



### Extra Resources
---
[Assessing Reproducibility](https://www.practicereproducibleresearch.org/core-chapters/2-assessment.html)

[R Reproducible Curriculum](https://github.com/Reproducible-Science-Curriculum)

[Hitchhikers Guide for packaging](https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/)








