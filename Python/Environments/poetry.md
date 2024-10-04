## NB:
- Install Poetry in its own venv
- Do not activate that venv when using Poetry
- Poetry does NOT install an interpreter for you.
  
  Use pyenv for that
- It **DOES** create a venv however on init 

## Install:
`curl -sSL https://install.python-poetry.org | python3 -`

Enable auto-complete
`poetry completions bash >> ~/.bash_completion`
## Update
`poetry self update`

## Init
1. From scratch `poetry new project_name`
2. Existing `poetry init`

## Modes
1. Package: requires `name` and `version` to package as publish, also installs the project as an *editable* package itself
2. non-package mode: Just for dependency management

## Dependencies
1. Add sources: `poetry source add pypi-test https://test.pypi.org/simple/`
2. `poetry add package_name`
3. add to [tool.poetry.dependencies]
4. `poetry update` to install the latest valid packages and update the `poetry.lock`
5. `poetry check` to confirm installed packages are in line with lock file

## Venv
Either
1. use `poetry run python something.py` to implicitly run with the venv
2. activate the env with `poetry shell`

## Installing Dependencies
`poetry install` - creates a `poetry.lock` if one does not already exist

`poetry install --no-root` if you DON'T want the project to be installed in editable mode itself

## Dev or other dependency groups

```toml
[tool.poetry.dependencies]  # main dependency group
httpx = "*"
pendulum = "*"
[tool.poetry.group.dev.dependencies]
pytest = "^6.0.0"
pytest-mock = "*"
```
`poetry add pytest --group dev` to install to a particular group

Remove dependency: `poetry remove pytest --group dev`

## Packaging

1. `poetry build`
   Will include files:
   1. LICENSE.*
   2. COPYING.*
   3. LICENSES/**
2. `poetry publish`
   Will require set-up credentials
   `poetry publish -r private_respository`