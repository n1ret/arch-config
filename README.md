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
./scripts/install_paru
```

### Config for config)

Build a binary of the arch-cfg.py script
```sh
./build.sh
```

Update the file at the global config dir
```sh
sudo python arch-cfg.py --src path/to/file
```

Specify the config directory to update
```sh
sudo python arch-cfg.py --src path/to/file --config hyprland
```

Turn on addition of the `bin` directory to the PATH env variable using /etc/profile.d file
```sh
sudo python arch-cfg.py --install
```

Turn off addition of the `bin` directory to the PATH env variable using /etc/profile.d file
```sh
sudo python arch-cfg.py --delete
```
