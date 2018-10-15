<div align="center">
	<h1>Cornora</h1>
	<p>Simple Hotcorner Launcher for X</p>
</div>


## Dependencies

- python (version 3)
- python-xlib
- python-setuptools (for installation)

## Installation

Install the dependencies first:

    $ sudo pacman -S python-setuptools python-xlib

clone this repo into your local storage:

    $ git clone https://github.com/yuune/Cornora.git
    $ cd Cornora
    $ chmod +x setup.py

then install via this command:

    $ sudo ./setup.py install


## Usage

| args            | conditions   |
| --------------- | ------------ |
| --tl "command"  | top-left     |
| --tr "command"  | top-right    |
| --bl "command"  | bottom-left  |

Example

```
      $ cornora --tl "skippy-xd"
      # or with multi conditions
      $ cornora --tl "skippy-xd" --tr "rofi -show run"      
```
      
## License

The code is available under the [MIT license](LICENSE).
