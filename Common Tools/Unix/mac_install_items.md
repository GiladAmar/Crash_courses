# Mac Installation Items

## Installs
### PKG Downloads
1. [Chrome](https://www.google.com/chrome/)
2. [FireFox](https://www.mozilla.org/en-US/firefox/new/)
3. [iTerm2](https://iterm2.com/downloads.html)
4. [Stillcolor](https://github.com/aiaf/Stillcolor)

### CLI
1. [Brew](https://brew.sh)

    `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
2. Xcode

    `xcode-select --install`
3. Brew installations
   ```bash
   brew update
   brew install magic-wormhole bluesnooze pyenv git
   brew install readline xz # for pyenv python installs
   brew install --cask docker
   ```

4. Rosetta
   
   `softwareupdate --install-rosetta`
5. Oh My Zsh

   `sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"`
6. Spotify

   `brew install --cask spotify`
7. Sublime

   `brew install --cask sublime-text`
8. Pycharm

   `brew install --cask pycharm`
9. Obsidian

   `brew install --cask obsidian`

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