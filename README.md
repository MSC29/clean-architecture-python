# Clean architecture: python

A Clean Architecture template for a Rest API in python

# How it works

Motivations, explanations, requirements & more details in my article [Practical Clean Architecture in Typescript, Rust & Python](https://dev.to/msc29/practical-clean-architecture-in-typescript-rust-python-3a6d)

# Installing

I personally use [pipx](https://github.com/pypa/pipx/), [pyenv](https://github.com/pyenv/pyenv) & [pipenv](https://github.com/pypa/pipenv).

```bash
pipenv install -r requirements.txt
# OR
pip install -r requirements.txt
```

# Running

define the environment on which we're running by adding `ENV=<env>`, which will use the `.env.<env>` file

```bash
ENV=dev python main.py
```

# Code quality & security

Used in CI/CD; using setup.cfg to centralize all the config

```bash
autopep8 -i -r --global-config=setup.cfg ./src
pylint --rcfile=setup.cfg ./src
flake8 --config=setup.cfg ./src
mypy --config-file=setup.cfg ./src
```

# Testing

Here's what done in order to mock the SPI

- db: through pytest's `conftest.py`'s fixtures that execute before the tests, the database is created & the test data is added
- http: here the "real" requests to the "real" API were recorder by `vcrpy` and they're referenced from `test/fixtures/vcr_cassettes` for each test in order to get the same request to be replayed

```bash
ENV=test pytest
```

# API Documentation

swagger: `http://127.0.0.1:8000/docs`
