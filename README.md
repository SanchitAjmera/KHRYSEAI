# KHRYSEAI
An Instagram bot that automates commenting, liking and following on Instagram. Named after the Golden Maidens crafted by Hephaestus 

## Installation
### Windows
#### Mozilla Firefox
You must have Mozilla Firefox preinstalled. You can find out how here, https://support.mozilla.org/en-US/kb/how-download-and-install-firefox-windows

Set the path to the Firefox executable `firefox.exe` as a path variable on windows, which is explained here, https://www.computerhope.com/issues/ch000549.htm

Check if `PATH` command on CMD or `which firefox` command on bash contains the path of your `firefox.exe` executable

#### Dependancies
run `.\setup.sh` command on CMD in the `src` folder to install all neccesary dependencies

## Instapy Cookies
Instapy might have an issue with accessing instagram because of there being no cookies found. For this a simple fix is to add the line:

`browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]").click()`

in `login_util.py:269` in your `instapy` module: 

`C:\Users\<username>\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\instapy`

after the `if cookie_loaded:` statement

## Quickstart
1 - In `main.py` enter your instagram credentials in place of the `userName` and `passWord` variables.

2 - Configure the file and set the desired comments, delays and volume of posts targeted in `main.py`

3 - Run the program by entering `python main.py` plus your desired tags targeted, for example `python main.py vase minimalism` would target the hashtags "vase" and "minimalism"

## Contact
If you have any issues or have any questions, please raise an issue on Github 

