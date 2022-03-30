SHELL=/bin/bash
CONDA_ENV=pysurv-dist
CONDA_ACTIVATE=source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate ; conda activate
CONDA_DEACTIVATE=source $$(conda info --base)/etc/profile.d/conda.sh ; conda deactivate ; conda deactivate

help:
	@printf "\033[36m%-30s\033[0m %s\n" pysurv-dist
	@echo ---
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' ./Makefile | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: help Makefile

lint: ## Run a linting check using flake8
	@python -m flake8

format:  ## Run a formatting check using black
	@python -m isort --settings-path pyproject.toml .
	@python -m black .

format-check:  ## Run a formatting check using black
	@python -m isort -c --settings-path pyproject.toml .
	@python -m black --check .

test:  ## Run tests using pytest
	@python -m pytest

install: lint format test  ## Install in active python environment if all checks pass
	@python -m pip install .

env: ## Create the development environment in conda
	@($(CONDA_DEACTIVATE); conda env remove -n pysurv-dist)
	@conda env create -f ./environment.yaml

coverage:  ## Run tests using pytest under coverage
	@python -m coverage run -m pytest -c pyproject.toml -m "not e2e and not model"
	@python -m coverage report -m --rcfile=pyproject.toml
	@python -m coverage html --rcfile=pyproject.toml
