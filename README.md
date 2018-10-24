<div align="center">
	<h1>Cornora</h1>
	<p>Simple Hotcorner Launcher for X</p>
</div>

## Dependencies

- `bash`
- `xdotool`

## Installation

1. Make sure you're already have those dependencies installed
2. clone this repo into your local storage:

    $ git clone https://github.com/yuune/Cornora.git
    
    $ cd Cornora

3. install it :

    $ sudo make install


## Usage

| args           | conditions   |
| -------------- | ------------ |
| -tl "command"  | top-left     |
| -tr "command"  | top-right    |
| -bl "command"  | bottom-left  |
| -br "command"  | bottom-right |

Example

      $ cornora -tl "skippy-xd"
      # or with multi conditions
      $ cornora -tl "skippy-xd" -tr "rofi -show run"      

      
## License

The code is available under the [MIT license](LICENSE).
