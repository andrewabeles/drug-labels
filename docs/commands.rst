Commands
========

The Makefile contains the central entry points for common tasks related to this project.

* `make test_environment` tests whether the python environment is setup correctly. 
* `make setup_project` ensures src is recognized as a python module
* `make requirements` pip installs the dependencies listed in requirements.txt
* `make data` downloads the raw data from OpenFDA, stores it in data/raw, processes it, and stores the processed data in data/processed.
