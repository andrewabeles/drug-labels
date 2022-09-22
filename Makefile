.PHONY: test_environment setup_project requirements data

#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_NAME = drug-labels
PYTHON_INTERPRETER = python3

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Test python environment is setup correctly
test_environment:
	$(PYTHON_INTERPRETER) test_environment.py

## Setup Project
setup_project: test_environment
	pip install . 

## Install Python Dependencies
requirements: setup_project
	$(PYTHON_INTERPRETER) -m pip install -U pip setuptools wheel
	$(PYTHON_INTERPRETER) -m pip install -r requirements.txt

## Make Dataset
data: requirements
	$(PYTHON_INTERPRETER) src/data/get_raw_data.py
	$(PYTHON_INTERPRETER) src/data/make_dataset.py data/raw data/processed
