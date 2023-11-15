# Download

Clone repository
```zsh
git clone --recurse-submodules git@github.com:n1ret/arch-config.git
```

Step in dir
```zsh
cd arch-config
```

# Scripts

### Setup configs
```zsh
sudo python setup.py
```

### Install paru
```zsh
source install_paru.zsh
```

### Config for config)

Update file at configs dir of this repo
```zsh
sudo python arch-cfg.py --src path/to/file
```

Turn on adding ./bin to path with /etc/profile.d file
```zsh
sudo python arch-cfg.py --install
```

Turn off adding ./bin to path with /etc/profile.d file
```zsh
sudo python arch-cfg.py --delete
```
