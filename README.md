# Clean architecture: python

A Clean Archtiecture template for a Rest API in python

# Dev

### Installing

I personnaly use [pipx](https://github.com/pypa/pipx/), [pyenv](https://github.com/pyenv/pyenv) & [pipenv](https://github.com/pypa/pipenv).

```bash
pipenv install -r requirements.txt
# OR
pip install -r requirements.txt
```

### Running

```bash
python main.py
```

### Code quality

using setup.cfg to centralise all the config

```bash
autopep8 -i -r --global-config=setup.cfg ./src
pylint --rcfile=setup.cfg ./src
flake8 --config=setup.cfg ./src
mypy --config-file=setup.cfg ./src
```
