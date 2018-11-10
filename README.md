# Cornora
Simple Hot Corner Launcher for X11

## Dependencies

- `bash`
- `xdotool`
- `xprop` from `xorg-xprop`

## Installation

#### Arch Linux

You can install it from your favourite aur helper

[cornora-git at AUR](https://aur.archlinux.org/packages/cornora-git/)

#### Manual

1. Make sure you're already have those dependencies installed
2. clone this repo into your local storage:
```
$ git clone https://github.com/yuune/Cornora.git
$ cd Cornora
```
3. install it :
```
$ sudo make install
```

## Usage

| args                            | conditions                                              |
| ------------------------------- | ------------------------------------------------------- |
| -tl "command"                   | top-left                                                |
| -tr "command"                   | top-right                                               |
| -bl "command"                   | bottom-left                                             |
| -br "command"                   | bottom-right                                            |
| -isf, --ignore-steam-fullscreen | disable command when steam game is active in fullscreen |
| -v                              | verbose mode                                            |
| -h                              | show the help                                           |

Example
```
$ cornora -tl "skippy-xd"
# or with multi conditions
$ cornora -tl "skippy-xd" -tr "rofi -show run"      
```
      
## License

The code is available under the [MIT license](LICENSE).
