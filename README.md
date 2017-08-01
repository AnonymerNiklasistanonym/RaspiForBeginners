# RaspiForBeginners
I document in this repository everything I do with my new Raspberry Pi 3. Have fun with your Rapspberry Pi 3 :D

# 1. Order/Get the hardware
* First, I've ordered a new Raspberry Pi 3 at [Amazon - 36€](https://www.amazon.de/Raspberry-Pi-Prozessor-Quad-Core-cortex-a53/dp/B01CD5VC92/ref=sr_1_4?s=computers&ie=UTF8&qid=1501606913&sr=1-4&keywords=raspberry+pi+3) (but there are also other sources where you can buy it from ;)
* At least an 8GB MicroSD Card (I've ordered a 32GB MicroSD Card at [Amazon - 16€](https://www.amazon.de/gp/product/B013UDL5RU/ref=oh_aui_detailpage_o00_s01?ie=UTF8&psc=1) (but there are also other sources where you can buy it from ;)

I already had the following things we also need:
* MicroUSB cable
* USB Charger (5V 2A)
* HDMI cable
* Display with HDMI Port
* Keyboard (USB)
* Mouse (USB)
* A computer (Windows 10 Desktop)

# 2. Setup an OS (a distribution) on the Raspberry Pi
Your Raspberry Pi is in front of you and you want to play with it :) ... But therefore you need an OS.<br>
To install one you have many possibilities: [See here](https://www.raspberrypi.org/learning/software-guide/quickstart/)
I chose to download the current Raspbian distribution "Jessie with desktop" directly from [raspberry.org](https://www.raspberrypi.org/downloads/raspbian/).<br>
Then I extracted the ZIP file to get the image of the LINUX distribution.<br>
To get the image onto the MicroSD card I used the open source program [etcher](https://etcher.io/). Simply install it, open it, choose the .img file, choose the correct drive and press flash.<br>
After the program has finished, you can now insert the MircoSD card into the Raspberry Pi.

# 3. First start
Now we are ready to go to start it.<br>
We only need to connect the HDMI cable with our monitor, connect a mouse and keyboard via USB (insert the MicroSD card) and plug in the USB charger and connect it with the MicroUSB to USB cable with the Pi.<br>
Because of the Pi start automatically and without login you will go straight to the desktop of Raspbian. YAY

# 4. Security and Network
## Security
Because of the default password is **raspberry** change it to something special (like *IwouldLike666RaspberryPies:D* ;)<br>
Simply go to menu in the upper left and click raspberry config (elaborate later a better way and add the console way).
## Network
Because we want to get online or into a home network, we simlply just click the upper left WLAN symbol (near the Bluetooth symbol) and click the right network (plus enter the hopefully not default credentials - if you connected a LAN cable you can skip this).
This was fast. Now we have a small but cool computer that can do everything that your current computer can :) (everything but Being fast in Gaming, Web, Video ... ;)

# 5. Connect it
## Remote desktop connection
I wanted to access the device everywhere from my Windows Desktop and my Windows Laptop so I though a remote desktop connection would be a perfect start (I have also only one monitor so.... yeah).<br>
I had some problems while establishing a simple connection, but thanks to this [stackexchange thread and Shreyas Murali](https://raspberrypi.stackexchange.com/questions/56413/error-problem-connecting-to-raspberry-pi-3-with-xrdp/56415#56415) i could establish a remote desktop connection like [Adam Riley described in his blog](http://www.raspberrypiblog.com/2012/10/how-to-setup-remote-desktop-from.html):
* First input this to remove the problem creating vncserver things `sudo apt-get remove xrdp vnc4server tightvncserver`
* Second install tightvncserver `sudo apt-get install tightvncserver`
* and last but not least install xrdp `sudo apt-get install xrdp`

XRDP will automatically run after the installation. Now we can start on any Windows computer (over the program search) a *remote desktop connection*. If you start this you need to know the IP Adress of your Raspberry Pi on your home network (elaborate later with the console way). If there are no problems (hopefully :) you now have a login i front of you in which you insert **pi** as username and **your secure password** as password. Viola, there you have your Raspberry Pi desktop.<br>
Because I wanted to acssess the PI without connecting it to anything than the power cable you need to open a config screen in the console (elaborate later) so that the Raspberry Pi will always start with a graphical user interface also when nothing (no HDMI cable) is connected.
