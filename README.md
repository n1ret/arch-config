# Download

Clone repository
```sh
git clone --recurse-submodules https://github.com/n1ret/arch-config.git
```

Step in dir
```sh
cd arch-config
```

# Scripts

### Setup config
Execute without `-c` to setup only global config

```sh
sudo python setup.py [-c cfg_name]
```

### Install paru
```sh
./install_paru.sh
```

### Config for config)

Update file at global config dir of this repo
```sh
sudo python arch-cfg.py --src path/to/file
```

Specify config dir
```sh
sudo python arch-cfg.py --src path/to/file --config hyprland
```

Turn on add ./bin to path by /etc/profile.d file
```sh
sudo python arch-cfg.py --install
```

Turn off add ./bin to path by /etc/profile.d file
```sh
sudo python arch-cfg.py --delete
```
