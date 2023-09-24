## VibeYak

VibeYak adds buttplug compatibility for YikYak made possible by [buttplug.io](https://buttplug.io/) and the [buttplug-py](https://github.com/Siege-Wizard/buttplug-py) library. 


## Why?
Why would I spend the time to do such a thing? Well you see I thought it would be funny and then I spent hours learning these libraries to try and do such thing because I thought it would be funny. It really was not that funny, I just was too far in. I think I need help.
## Installation

Make sure you have [git](https://git-scm.com/downloads) installed, as well as [python version 3.11](https://www.python.org/downloads/release/python-3110/).

Also make sure you have [Interface Central](https://intiface.com/central/) installed, this will be used to connect to your buttplug of choice.

Clone this repository by running in terminal:
```bash
   git clone https://github.com/onyxcatto/VibeYak
```

Change directory in to the cloned repository by running:
```bash
   cd VibeYak
```
Make sure you have pip (python's package manager) installed by running the following command depending on your OS:

If you are on Windows:
```bash
   py -m ensurepip --upgrade
```
If you are on MacOS or Linux:
```bash
   python -m ensurepip --upgrade
```
Install dependencies by running (You might have to type "pip3" instead of "pip" depending on your OS):
```bash
   pip install -r requirements.txt
```

Install playwright by running:
```bash
   playwright install
```

Now open Interface Central and hit the play button in the top left corner to start receiving input.

Check if your buttplug device in recognized in the devices tab, and hit the start scanning button if the device is not picked up. 

Make sure to stop scanning once the device is found. More information of how to work [Interface Central is here on their Github](https://github.com/intiface/intiface-central).

Now run the program (You may have to type "python3" instead of "python", depending on your OS):
```bash
   python VibeYak.py
```
The program will ask you to login to your YikYak account (actually it's your Sidechat account because Sidechat owns YikYak) by asking for your phone number. 

Upon entering your phone number, it will text you a verification code (it will say it's from SideChat, SideChat owns YikYak, it's the same thing), which when entered will grant access to your account. Make sure you enter the code exactly right or the program will not work.

I know this may seem suspicious to give out your phone number like that, but read the source code if you don't trust me. This program works by running the [unoffical web version](https://web.yikyak.pro/) of YikYak in a stripped down browser known as [Playwright](https://playwright.dev/) order to get the Karma from the user. 

Now it should be all connected and now start vibrating in response to your Karma increasing.
