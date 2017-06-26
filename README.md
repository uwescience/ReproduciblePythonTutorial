# Tips for Reproducible Python

#### Directory Structure
---
* 	create an empty project with a base structure 

```
.
+-- data
|   +-- raw
|   +-- processed
|
+-- src
|   +-- submodules
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
+-- README.md
+-- LICENSE.txt
```

Comprehensive Project Templates:

* [Data Science Cookiecutter](https://drivendata.github.io/cookiecutter-data-science/#contributing)
* [Shablona - Python Package Template] (https://github.com/uwescience/shablona)

	
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

```
	pip install nose
```


* Remotely:
	*  [Travis-CI (free for public repos)](https://travis-ci.org/)
	*  [AppVeyor (for Windows)](https://www.appveyor.com/) 
	*  [CircleCI](https://circleci.com/)
	*  [Wercker](http://www.wercker.com/) (based on [Docker](https://www.docker.com/) containters)
	*  [Jenkins](https://jenkins.io/) - need to configure it

	Coverage
	* [Coveralls](https://coveralls.io/)

	Testing:
	unit testing
	integration testing
	regression testing
	


### Distributions & Package Managers
---
Conda vs pip


What is Conda? 

* Conda distribution is slightly different from the default python distribution.

* Conda packages come in the form of .whl files (wheel files). They are precompiled packages: i.e. they are compiled for each specific operating system. 
They are fast to install. (Installing Numpy from scratch takes forever compiling C code)
Anaconda/ Miniconda(bare bones)

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



  
Trick with 2 distributions under Jupyter notebook???
* Saving environments (.yml, pip freeze, pip install -r)
* Installing Jupyter within virtual environment
* Workflows with notebooks: 
  * move function to a module
  * paths for modules
  * reloading modules
  * submodules
  *
  

#### Editors
---
  * [PyCharm](https://www.jetbrains.com/pycharm/) -integration with GitHub
  * [Atom](https://atom.io/) - coloring in Github (extra packages)
  * [JupyterLab](https://) (web based -> can run on server)
  * [Spyder](https://pythonhosted.org/spyder/) Matlab-like IDE
  	* [PEP8](https://pythonhosted.org/spyder/) - linters

#### Documentation
---
  * [Reveal.js](http://lab.hakim.se/reveal-js/#/):  Jupyter notebook -> slides
  * [Nbconvert]()
  * css styles for notebook
  * [Sphinx](http://www.sphinx-doc.org/en/stable/) readthedocs, ...  - maybe referring more to shablona
    
  * [Binder (of notebooks)] (http://mybinder.org/) (free sharing of github jupyter notebooks)(Microsoft Notebooks?)
  * [Jupyter Hub](https://jupyterhub.readthedocs.io/en/latest/) + [Kubernetes](https://kubernetes.io/)
  
  [Docker](), [Vagrant](), ...
  

  

https://drivendata.github.io/cookiecutter-data-science/

Something about naming conventions?
Recloning.

[Choosing a License](https://choosealicense.com/)

#### Extra Resources



