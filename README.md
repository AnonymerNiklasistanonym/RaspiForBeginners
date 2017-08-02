# RaspiForBeginners
In this repository I'ill wanted to document (now also with other cool people :raised_hands:) everything I do with my *new* Raspberry Pi 3 just for fun and education.

You can use this repository as a beginners tutorial for your own Raspberry Pi or probably learn something new and cool about it (or help us to make this tutorial/repository better :).

Have fun with your Raspberry Pi 3 :smiley:

# 1. Get the hardware
**But first what do we need to have fun with our Raspberry Pi 3?**

* Obviously order a new Raspberry Pi 3 (I bought one from [Amazon for 36€](https://www.amazon.de/Raspberry-Pi-Prozessor-Quad-Core-cortex-a53/dp/B01CD5VC92/ref=sr_1_4?s=computers&ie=UTF8&qid=1501606913&sr=1-4&keywords=raspberry+pi+3))
* An at least an 8GB Micro SD Card (I've ordered a 32GB big one from [Amazon for 16€](https://www.amazon.de/gp/product/B013UDL5RU/ref=oh_aui_detailpage_o00_s01?ie=UTF8&psc=1))

**The following things you probably already have:**
*(you don't need them all for having fun but if you want to follow this tutorial)*

* USB Charger (5V 2A) with an Micro USB cable (or you can buy a specific power supply)
* HDMI cable
* Display with a HDMI port
* Keyboard (USB)
* Mouse (USB)
* A computer (I have a Windows 10 Desktop - other desktop OSs' should be fine too)

# 2. Setup an OS
Your Raspberry Pi is in front of you and you want to play with it... but therefore you need an operating system.
To install one you have many possibilities regarding the OS or rather LINUX distribution ([See here the official guide](https://www.raspberrypi.org/learning/software-guide/quickstart/)).

**We installed Raspbian onto the Raspberry Pi:**

1. Therefore you need to download the current Raspbian distribution ("Jessie with desktop" did we download) directly from [raspberry.org](https://www.raspberrypi.org/downloads/raspbian/).
2. Then you extracted the ZIP file to get the image of the LINUX distribution.
3. Because you can't just put an `.img` file on the Micro SD card you need to install a program like the open source program [etcher](https://etcher.io/). 
   Simply install it, open it, choose the `.img` file, choose the correct drive and press flash.
4. Great, now you only need to safely eject the card and put it into your Raspberry Pi. :thumbsup:

# 3. First start
​Now we are ready to go and can finally start the Pi. :muscle: 

Because we (or better I) am not the best with the console I want to start in the graphical user interface of the OS. Therefore you need to follow these steps:

1. Connect the HDMI cable with your monitor.
2. If you want to use the system probably connect a mouse and keyboard via USB.
3. Now you can plugin the power supply or USB charger and connect it with the Micro USB port on the Raspberry to start it.
4. Enjoy the fresh desktop of Raspbian because you get automatically logged in and so straight to the desktop.

# 4. Security and network and more
## Security
You get automatically logged in as the user **pi** with the default password **raspberry**.

But because everyone knows that a default password isn't such a great idea you might wanna consider doing the following things:

### Change the default password

To change the fault password there are two ways:

#### Graphical User Interface

+ Click the raspberry icon at the top left
+ Click `Preferences`
+ Click `Raspberry Pi Configuration`
+ In the new window you are now in the tab `System` 
+ There you click the top button `Change Password...`
+ Now you input the current password **raspberry** and below two times a new, *secure* and *long* password (like **IwouldLike666RaspberryPies:D**)

#### Console

The console is the most powerful tool - it's so mighty that we will do every step also in the console. It's in the beginning a bit strange, but thanks to a steep learning curve you will also soon like to work with it. :wink:

- Click the console icon at the top left (icon looks a bit like this: `>_`)
- Tada, you opened the mightiest tool and should be seeing something like this:

```
pi@raspberrypi:~ $ ▮
```

This means you are the user **pi** and logged in at the computer with the name **raspberrypi**.

- now you can interact/talk with the OS/LINUX distribution through typing in commands with your keyboard and pressing enter if your command stands there completely
- the first command we gonna use is the command `passwd` and press enter:

```
pi@raspberrypi:~ $ passwd
Changing password for pi.
(current) UNIX password: ▮
```

Now you input your old (or right now default) password (**raspberry**)
*(don't get frightened because you can see nothing - it's normal that if you input passwords the console only listens and not prints stars (*`*` *) or other things)*

- After you typed in the correct password you need to type in a new, *secure* and *long* password

```
pi@raspberrypi:~ $ passwd
Changing password for pi.
(current) UNIX password:
Enter new UNIX password: ▮
```

- And after that type in this new password again

```
pi@raspberrypi:~ $ passwd
Changing password for pi.
(current) UNIX password:
Enter new UNIX password:
Retype new UNIX password: ▮
```

- Nice job, you changed successfully the password of your Raspberry Pi over the console :smiley::thumbsup:

### Deactivate the auto login at boot

Normally every time you start the Pi you get logged in immediately without typing in your password which is .... cool I guess, but we (or at least me) want to be a bit more secure.

Because of that we want to change this so that every time you start the Pi you need to type in your credentials (through this way the possibility to forget your password is also minimized).

To change this we stay in the console or open it if it's closed and type in `sudo raspi-config`
*(`sudo` is an abbreviation of “**super user do**” and allows LINUX users to execute administrative programs that not every user should be able to run. Only the **root user** should be able to run them - for example not the guest user should be able to change these kind of things.)*

```
pi@raspberrypi:~ $ sudo raspi-config▮
```

After you pressed enter you will find yourself in the middle of the **Raspberry Pi Software Configuration Tool (raspi-config is the console name)**.

You now pilot the red selection with the arrow keys to 
`3 Boot Options		Configure options for startup`.

Then you press enter and select 
`B1 Desktop / CLI		Choose whether to boot into a des...`.

Then after you pressed enter you can choose what you want to boot in every time:

```
B1 Console				(boot OS in console only without GUI)
B2 Console Autologin		(boot OS in console and automatically be logged in)
B3 Desktop				(boot OS with a GUI)
B4 Desktop Autologin		(boot OS with a GUI and automatically be logged in)
```

We choose to always start with a GUI and without automatically be logged in.
So we select `B3` and press enter.

## Network
Because we also want to talk with the Raspberry Pi in our home network or even want to get access to the world wide web we not even need to connect a lame old LAN cable (😜 - but we can do this nonetheless if we want to or have no WLAN router).

Since the Raspberry Pi 3 has a cool WLAN chip, [and more if you want to know all the hardware parts](https://www.raspberrypi.org/learning/software-guide/components/raspberry-pi/), we can access the home network simply by clicking the WLAN symbol right next to the Bluetooth symbol at the top right. Then select the right network, click it, hopefully input a *long* and *safe* password and hurray! we  are connected to the home network and have internet (if you have internet in your home network ;).

## Resolution

Probably some of you have noticed that the desktop isn't full screen on some monitors like my 1920x1080 monitor. Let's change this so that we can fully enjoy the Raspberry Pi.

#### Graphical User Interface

- Click the raspberry icon at the top left
- Click `Preferences`
- Click `Raspberry Pi Configuration`
- In the new window you are now in the tab `System` 
- There you click the button `Set Resolution...` and select your desired resolution
- Than you also disable Underscan and after one fast reboot you are fully prepared *"Es krachen zu lassen!"* (German idiom - literally translated to *"To let it crash!"* - right translated to *"To party hard!"*)

#### Console

The cool thing is - you can do the whole thing also in the console and you already know how! You don't believe me?

* Just open your console and start again the **Raspberry Pi Software Configuration Tool**  with the command `raspi-config`
* Then select `7 Advanced Options`
* Then select `A2 Overscan`
* Then select `No`

Same thing if you want to change the resolution:

- Select again `7 Advanced Options`
- Then select `A5 Resolution`
- Then select `Your desired resolution`



WOW. This was fast!
Now you have a small but cool computer that can do everything that your current computer can :) 

(everything but being fast in Gaming, Web, Video ... ;) 
(Note: It can even play 1080p and can be used for normal browsing)

# 5. Connect it
## Remote desktop connection
I wanted to access the device everywhere from my Windows Desktop and my Windows Laptop so I though a remote desktop connection would be a perfect start (I have also only one monitor so.... yeah).

This means that you can mirror the whole Raspberry Pi GUI on your Windows Device (or also LINUX) and using it while the Raspberry only needs to be connected to the power and the same network like your Computer (LAN or WLAN - also the router needs to be allowing this and not isolate every device on the network).

I had some problems while establishing the connection with the tutorial from [Adam Riley on his blog](http://www.raspberrypiblog.com/2012/10/how-to-setup-remote-desktop-from.html), but thanks to this [stack exchange thread and Shreyas Murali](https://raspberrypi.stackexchange.com/questions/56413/error-problem-connecting-to-raspberry-pi-3-with-xrdp/56415#56415) I could establish a remote desktop connection in... less than one minute:

* First input this to remove the somehow problem creating vncserver things
  `sudo apt-get remove xrdp vnc4server tightvncserver`
* Second install tightvncserver
  `sudo apt-get install tightvncserver`
* and last but not least install xrdp
  `sudo apt-get install xrdp`
* XRDP will automatically run after the installation.

One thing before we can start:
You need to know the IP address of your Raspberry Pi on your home network. 

If you do not know the address we can use our mighty console by using the command `hostname -I`.
If you press enter you will see the IP address and mac address of your Raspberry Pi like `192.168.0.23 33ac:6589:a374:...`
just copy everything before the blank and you have the IP address or rather house number of your Pi in your network.

Now we can start on any Windows computer (over the program search) a *remote desktop connection*.

* You input in the opened window the IP address of your Raspberry Pi and click `connect`
* Than a strange window should open itself that asks for a username and password 
* You type in as your username **pi** and as password your **your secure password** 

Viola, there you have your Raspberry Pi desktop on your Windows computer.



Also because we set as automatic start of the Pi a GUI start we now always login to the GUI of the Pi when we log ourselves in over a remote desktop connection without needing the raspberry connect to any cables but the power chord (and eventually your network cable if you do not have WLAN).