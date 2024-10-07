# Mac Installation Items

## Installs
### PKG Downloads
1. [Chrome](https://www.google.com/chrome/)
2. [FireFox](https://www.mozilla.org/en-US/firefox/new/)
3. [iTerm2](https://iterm2.com/downloads.html)
4. [Stillcolor](https://github.com/aiaf/Stillcolor)

### CLI
1. Xcode

    `xcode-select --install`

2. [Brew](https://brew.sh)
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   brew update
   brew install magic-wormhole bluesnooze pyenv git
   brew install readline xz # for pyenv python installs
   brew install --cask docker pycharm spotify sublime-text obsidian
   ```
3. Rosetta
   
   `softwareupdate --install-rosetta`
4. Oh My Zsh

   `sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"`


### AppStore
1. MS Teams
2. MS Office

## Configuration
1. Pycharm
2. Keys
   1. SSH keygen
    ```bash
    ssh-keygen -t rsa -b 4096 -f /path/to/keys/my_key
    chmod 400 ~/.ssh/my_key
    ```

   2. Git & GitLab Keys


# TODO Potential adds
1. Poetry