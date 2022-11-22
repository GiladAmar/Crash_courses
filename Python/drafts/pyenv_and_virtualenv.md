# Installation

## Run
```bash
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl

curl https://pyenv.run | bash
```

## Add env vars to .bashrc
```bash
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

## Reload shell
```bash
exec "$SHELL"
```


# Installing a Python Version
## View options
These include  pypy, jython, anaconda etc.
```bash
pyenv install --list
# 3.6.0
# 3.6-dev
# 3.6.1
# ...
```

## Un/Install Python versions
These are all installed in _~/.pyenv/versions/_
```bash
pyenv install 3.6.9
pyenv uninstall 3.6.9
```

## View installed versions
```bash
pyenv versions
```

# Activating a python version

## Global - The default python used in shells:
This command sets the ~/.pyenv/version to 3.6.8.
```bash
pyenv global 3.6.8
```

## Local - Set version to be used in this folder
This command creates a .python-version file in your current directory(which auto activate this version when in this folder)
```bash
pyenv local 2.7.15
```

## Shell - Set version to be used just for this shell
```bash
pyenv shell 3.6.9
```

# Virtual Environments

## Create
```bash
pyenv virtualenv 2.7.10 my-virtual-env-name
```

## List
```bash
pyenv virtualenvs
```

## Assign to project and Activate
```bash
pyenv local my-virtual-env-name
```
Now when you enter that dir that will be the env by default

Otherwise, these are what's happening underneath
```bash
pyenv activate my-virtual-env-2.7.10
pyenv deactivate my-virtual-env-2.7.10
```
