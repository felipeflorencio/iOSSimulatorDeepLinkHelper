# iOS Simulator Deep Link Helper
A small script that helps you get all your running simulator's, pick one and pass the deep link that you want that simulator to start

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![Python 3.0](https://img.shields.io/badge/python-3.0-blue.svg)](https://www.python.org/downloads/release/python-300/)
[![made-with-Markdown](https://img.shields.io/badge/Made%20with-Markdown-1f425f.svg)](http://commonmark.org)

Python interface to you load all running simulator, pick one and pass a deep link that you want to test and will be open on simulator that you chose.

### Requirements
- Python 3

## About

This tool was built to make easy select a simulator and open a deep link.  
You need to have one simulator running, if not the tool will say that there's no simulator running and ask you to start.  
If you have just 1 simulator running we will select that one by default and only ask for the deeplink you want to try.  
But if you have more than one simulator running we will show a list with a number, it's just type the number that will pick that to use the deep link.

## Usage

```shell
python3 deeplink_helper.py

// Will show your list of running devices
This are the devices that are running, please pick one:
0 - Device XPT
1 - Device NVB
2 - Device PDJ

// After pick one you need to put the deep link that you want to try
Which deep link do you want to try:
Deep link: <my deep link that I want to try>

```

#### * Python tip

If you don't want to always type 'python3' you can just run this command on terminal: 

```shell
chmod +x deeplink_helper.py
```

And after you can run just typing: 

```shell
./deeplink_helper.py
```

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![saythanks](https://img.shields.io/badge/say-thanks-ff69b4.svg)](https://saythanks.io/to/kennethreitz)

### Improvements  
	- Possibility to start a simulator if no one is running.
	- Cache the last running deep link and just ask if want to use the same again. 


## Author

Felipe Garcia, felipeflorencio@me.com  
Twitter: @dr_nerd   

<a href="https://twitter.com/intent/follow?screen_name=dr_nerd"><img alt="Follow on Twitter" src="https://img.shields.io/twitter/follow/dr_nerd.svg?style=social"></a>

## License (MIT)

Copyright (C) 2016 Johannes Plunien

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
