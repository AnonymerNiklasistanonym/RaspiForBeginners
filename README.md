# RaspiForBeginners

In this repository I'll document (now also with other cool people :raised_hands:) everything I do with my *new* Raspberry Pi 3 just for fun and education.

You can use this repository as a beginners tutorial for your own Raspberry Pi [3] or probably learn something new and cool about it (or even help us to make this tutorial/repository better :).

Have fun with your Raspberry Pi 3! :smiley:

## 0. Other cool things

Outside of this tutorial you can find in this repository also:

- A funny and short introduction into Linux and Bash (only in German for now) from [denniskeller](https://github.com/denniskeller)
  → find it in the [directory `linuxdemo`](linuxdemo) (download the repository and open`index.html`)
- Some simple scripts in different languages if you want to get in touch with some programming languages
- Other things if you have something cool and contribute it :D
  (links to cool websites and repositories are also allowed)

### 0.1 [How to connect and use a camera with Python](CAMERA.md)

(Advanced) Tutorial of how to make/use pictures/videos with your raspberry pi and python3.

### 0.2 [How to connect and use GPIO pins](GPIO.md)

(Advanced) Tutorial of how to use the GPIO pins to turn LED's on, use external displays and such things with your raspberry pi and python3.

## 1. Get the hardware

**But first what do we need to have fun with our Raspberry Pi 3?**

- Obviously order a Raspberry Pi 3 (I bought one from [Amazon for 36€](https://www.amazon.de/Raspberry-Pi-Prozessor-Quad-Core-cortex-a53/dp/B01CD5VC92/ref=sr_1_4?s=computers&ie=UTF8&qid=1501606913&sr=1-4&keywords=raspberry+pi+3))
- An at least an 8GB Micro SD Card (I've ordered a 32GB big one from [Amazon for 16€](https://www.amazon.de/gp/product/B013UDL5RU/ref=oh_aui_detailpage_o00_s01?ie=UTF8&psc=1))

**The following things you probably already have:**
*(you don't need them all for having fun but if you want to follow this tutorial)*

- USB Charger (5V 2A) with an Micro USB cable (or you can buy a specific power supply)
- HDMI cable
- Display with a HDMI port
- Keyboard (USB)
- Mouse (USB)
- A computer (I have a Windows 10 Desktop - other desktop OSs' should be fine too)

## 2. Setup an OS

Your Raspberry Pi is in front of you and you want to play with it... but therefore you need an operating system.
To install one you have many possibilities regarding the OS or rather Linux distribution ([See here the official guide](https://www.raspberrypi.org/learning/software-guide/quickstart/)).

**Let's install the default Raspbian OS onto the Raspberry Pi:**

1. Therefore you need to download the current Raspbian distribution ("Jessie with desktop" did we download) directly from [raspberry.org](https://www.raspberrypi.org/downloads/raspbian/).
2. Then extract the ``.zip` file to get the image of the Linux distribution.
3. Because you can't just put an `.img` file on the Micro SD card you need to install a program that *burns it onto the Micro SD Card* like the open source program [etcher](https://etcher.io/).
   Install it, open it, choose the `.img` file, choose the correct drive and press flash.
4. Great, now you only need to safely eject the card and put it into your Raspberry Pi Micro SD Card slot. :thumbsup:

## 3. First start

​Now we are ready to go and can finally start the Pi. :muscle:

Because you (or probably I) am not the best with the console let's start the Pi in the graphical user interface of the OS. Then it will behave the same like every other OS with a desktop.

To start it in GUI mode you need to at least once the following steps:

1. Connect the HDMI cable with your monitor.
2. If you want to interact with the Pi probably connect a mouse and keyboard via USB.
3. Now you can plugin the power supply or USB charger and connect it with the Micro USB port on the Raspberry to start it. (*Power not until after everything is connected!*)
4. Enjoy the fresh desktop of Raspbian because you automatically are logged in and so get straight to the desktop.

## 4. Security and network and more

### Security

You get automatically logged in as the user **pi** with the default password **raspberry**.

But because everyone knows that a default password isn't such a great idea you might wanna consider doing this:

#### Change the default password (*!!!*)

To change the fault password there are two ways:

##### Graphical User Interface

- Click the raspberry icon at the top left
- Click `Preferences`
- Click `Raspberry Pi Configuration`
- In the new window you are now in the tab `System`
- There you click the top button `Change Password...`
- Now you input the current password **raspberry** and below two times a new, *secure* and *long* password (like **IwouldLike666RaspberryPies:D**)

##### Console

The console is the most powerful tool - it's so mighty that we will do (almost) every step also in the console. At first it's a bit strange, but thanks to a steep learning curve you will also soon like to work with it (seriously, it's totally worth it!). :wink:

- Click the console icon at the top left (icon looks a bit like this: `>_`)
- Tada, you opened the mightiest tool and should be seeing something like this:

```text
pi@raspberrypi:~ $ ▮
```

This means you are the user **pi** and logged in at the computer with the name **raspberrypi**.

- now you can interact/talk with the OS/Linux distribution through typing in commands with your keyboard and pressing enter if your command stands there completely
- the first command we gonna use is the command `passwd` and press enter:

```text
pi@raspberrypi:~ $ passwd
Changing password for pi.
(current) UNIX password: ▮
```

Now you input your old (or right now default) password (**raspberry**)
*(don't get frightened because you can see nothing - it's normal that if you input passwords the console only listens and not prints stars (*`*` *) or other things)*

- After you typed in the correct password you need to type in a new, *secure* and *long* password

```text
pi@raspberrypi:~ $ passwd
Changing password for pi.
(current) UNIX password:
Enter new UNIX password: ▮
```

- And after that type in this new password again

```text
pi@raspberrypi:~ $ passwd
Changing password for pi.
(current) UNIX password:
Enter new UNIX password:
Retype new UNIX password: ▮
```

- Nice job, you changed successfully the password of your Raspberry Pi over the console :smiley::thumbsup:

#### Deactivate the auto login at boot

Normally every time you start the Pi you get logged in immediately without typing in your password which is .... cool I guess, but we (or at least I) want to live a little bit more secure.

Because of that we want to change this so that every time you start the Pi you need to type in your credentials (through this way the possibility to forget your password is also minimized).

To change this we stay in the console or open it if it's closed and type in `sudo raspi-config`.
*(`sudo` is an abbreviation of "**super user do**" and allows Linux users to execute administrative programs that not every user should be able to run. Only the **root user** should be able to run them - for example not the guest user should be able to change these kind of things.)*

```text
pi@raspberrypi:~ $ sudo raspi-config▮
```

After you pressed enter you will find yourself in the middle of the **Raspberry Pi Software Configuration Tool (raspi-config is the console name)**.

You now pilot the red selection with the arrow keys to
`3 Boot Options        Configure options for startup`.

Then you press enter and select
`B1 Desktop / CLI        Choose whether to boot into a des...`.

Then after you pressed enter you can choose what you want to boot in every time:

```text
B1 Console              (boot OS in console only without GUI)
B2 Console Autologin    (boot OS in console and automatically be logged in)
B3 Desktop              (boot OS with a GUI)
B4 Desktop Autologin    (boot OS with a GUI and automatically be logged in)
```

We choose to always start with a GUI and without automatically be logged in.
So we select `B3` and press enter.

### Network

Because we also want to talk with the Raspberry Pi in our home network or even want to get access to the world wide web we not even need to connect a lame old LAN cable (😜 - but we can do this nonetheless if we want to or have no WLAN router).

Since the Raspberry Pi 3 has a cool WLAN chip, [and more if you want to know all the hardware parts](https://www.raspberrypi.org/learning/software-guide/components/raspberry-pi/), we can access the home network simply by clicking the WLAN symbol right next to the Bluetooth symbol at the top right. Then select the right network, click it, hopefully input a *long* and *safe* password and hurray! we  are connected to the home network and have internet (if you have internet in your home network ;).

### Resolution

Probably some of you have noticed that the desktop isn't full screen on some monitors like my 1920x1080 monitor. Let's change this so that we can fully enjoy the Raspberry Pi.

#### Resolution - Graphical User Interface

- Click the raspberry icon at the top left
- Click `Preferences`
- Click `Raspberry Pi Configuration`
- In the new window you are now in the tab `System`
- There you click the button `Set Resolution...` and select your desired resolution
- Than you also disable Underscan and after one fast reboot you are fully prepared *"Es krachen zu lassen!"* (German idiom - literally translated to *"To let it crash!"* - right translated to *"To party hard!"*)

#### Resolution - Console

The cool thing is - you can do the whole thing also in the console and you already know how! You don't believe me?

- Just open your console and start again the **Raspberry Pi Software Configuration Tool**  with the command `raspi-config`
- Then select `7 Advanced Options`
- Then select `A2 Overscan`
- Then select `No`

Same thing if you want to change the resolution:

- Select again `7 Advanced Options`
- Then select `A5 Resolution`
- Then select `Your desired resolution`

WOW. This was fast!
Now you have a small but cool computer that can do everything that your current computer can :)

(everything but being fast in Gaming, Web, Video ... ;)
(Note: It can even play 1080p and can be used for normal browsing)

## 5. Connect it

### Remote desktop connection

---

#### Update 18. August 2017

I just reset my Raspberry Pi 3 and followed my instructions.
But when I tried to login via `XRDP` suddenly a different window popped up.

It worked fine as before but now it also supports the Microsoft Remote Desktop apps for [Windows 10](https://www.microsoft.com/en-us/store/p/microsoft-remote-desktop/9wzdncrfj3ps) and [Android](https://play.google.com/store/apps/details?id=com.microsoft.rdc.android&hl=en)!

That means you now can use your Windows 10 clipboard on the remote desktop and more cool features if you want to!

(I don't know if you even need the following instructions - try without them and if it doesn't work follow them)

---

#### XRDP (Works fine with Windows)

I wanted to access the device everywhere from my Windows Desktop and my Windows Laptop so I though a remote desktop connection would be a perfect start (I have also only one monitor so.... yeah).

This means that you can mirror the whole Raspberry Pi GUI on your Windows Device (or also Linux) and using it while the Raspberry only needs to be connected to the power and the same network like your Computer (LAN or WLAN - also the router needs to be allowing this and not isolate every device on the network).

I had some problems while establishing the connection with the tutorial from [Adam Riley on his blog](http://www.raspberrypiblog.com/2012/10/how-to-setup-remote-desktop-from.html), but thanks to this [stack exchange thread and Shreyas Murali](https://raspberrypi.stackexchange.com/questions/56413/error-problem-connecting-to-raspberry-pi-3-with-xrdp/56415#56415) I could establish a remote desktop connection in... less than one minute:

- First input this to remove the somehow problem creating vncserver things
  `sudo apt-get remove xrdp vnc4server tightvncserver`
- Second install tightvncserver
  `sudo apt-get install tightvncserver`
- and last but not least install xrdp
  `sudo apt-get install xrdp`
- XRDP will automatically run after the installation.

One thing before we can start:
You need to know the IP address of your Raspberry Pi on your home network.

If you do not know the address we can use our mighty console by using the command `hostname -I`.
If you press enter you will see the IP address and mac address of your Raspberry Pi like `192.168.0.23 33ac:6589:a374:...`
just copy everything before the blank and you have the IP address or rather house number of your Pi in your network.

Now we can start on any Windows computer (over the program search) a *remote desktop connection*.

- You input in the opened window the IP address of your Raspberry Pi and click `connect`
- Than a strange window should open itself that asks for a username and password
- You type in as your username **pi** and as password your **your secure password**

Voilà, there you have your Raspberry Pi desktop on your Windows computer.

#### XRDP method for Android

You can even remotely control your Pi via your ANDROID device:

It's a bit messy, but here are the things you need to do:

1. Install a virtual keyboard, because the android app can't handle essential inputs like `-`.
   - `sudo apt-get update` - update the repositories
   - `sudo apt-get upgrade` - upgrade the whole system (optional)
   - `sudo apt-get install matchbox-keyboard` - install the virtual  matchbox-keyboard keyboard
   - `sudo reboot` - a reboot isn't really necessary but just do it quickly
2. You can now start it over the terminal with the command `matchbox-keyboard`
3. Download and install the android app [RDP Remote Desktop aFreeRDP](https://play.google.com/store/apps/details?id=com.freerdp.afreerdp&hl=en)
4. Set everything up
   - start the app and click the plus symbol in the top bar (*add*)
   - now enter under `Label` how you want to name the connection
   - for `Host` the IP address of the Pi
   - for `Credentials` click it and enter your username and password
   - now go to times back (press two times the back button) and save your changes
5. Enjoy your ANDROID remote control
   - click the new created connection and go straight to the desktop of your Pi on your ANDROID device
   - if you know want to execute commands just type in `match` + `Tab` and `enter` and you can input symbol's like `-` over the virtual console

Also because we set as automatic start of the Pi a GUI-start we now always login to the GUI of the Pi when we log ourselves in over a remote desktop connection without needing the raspberry connect to any cables but the power chord (and eventually your network cable if you do not have WLAN).

### SSH (terminal) connection

But what if we don't want a GUI. A simple CLI is enough isn't it?

Because of this here are some services, that let you connect to your Pi  so that you can interact with it via command line:

#### ConnectBot (Android, [Open Source](https://github.com/connectbot/connectbot))

Here a simple and Open Source solution with which you can control your Pi over the terminal on your Android device:

1. Install the app via Play Store: [ConnectBot](https://play.google.com/store/apps/details?id=org.connectbot)
2. Open it and click the plus at the bottom right (`+`)
3. Click and expand the input filed `username@hostname:port`
   - Now input your username in the filed `username`
   - And input the IP address of your Pi
   - Enter a nickname in the field `Nickname`
   - Now conform your input by clicking the `+` at the top right
4. Click now the new entry in the list
5. A terminal will open itself and then a popup that asks if yo really want to connect - confirm
6. Then the terminal will say

   ````text
   Attempting 'password' authentication
   ````

   and an input filed will popup right above your keyboard which will say `Password:`

7. Input the password for your username and click ENTER
8. Again wait roughly one or two seconds and *Wooooosh* you have full CLI control over your Pi over your Android device :launch:

But this is not the only way to do this. There are many clients that can do this for many OS's. For example here you have another SSH CLI client for Windows:

#### PuTTY (Windows, [Open Source](https://www.chiark.greenend.org.uk/~sgtatham/putty/))

Also a very small but cool service for your Windows computer.

1. Install it over at [their website](http://www.putty.org/) (first link)
2. Open it and enter directly the IP address of your Pi
   (you are already in this but the input field is located under `Session > Host Name (or IP address)`)
3. If you not always want to retype the IP address enter in the input filed `Saved Sessions` a name for the connection and click `Save` after you are ready
4. Now click `Open` at the bottom of the window
5. Type in the terminal that opened itself your username:

   ```text
   Login as: ▯
   ```

6. Input ENTER and now input the password of your account:

   ```text
   Login as: pi
   pi@192.168.0.42's password: ▯
   ```

7. When you are ready press again ENTER and you are ready to rumble!

   ```text
   Login as: pi
   pi@192.168.0.42's password: ▯

   Text

   More Text
   Last login: Tue Aug 15 00:24:18 2017 fro 192.168.0.21
   pi@raspberrypi:~ $ ▯
   ```

Tipp: You can enter full screen mode by clicking `Ctrl` + `Right mouse key` and exiting it like this any time (looks way more professional :stuck_out_tongue_winking_eye:)

### File manager connection (SFTP over SSH)

The following services can you enable access to the file system of your Pi over the Secure Shell protocol:

#### Filezilla (Windows, [Open Source](https://filezilla-project.org/download.php?show_all=1))

Because of the Secure Shell protocol you can do even more cool things.

One of them is to remotely control the whole file system of your Raspberry Pi from for example your Windows computer over a program named FileZilla.

What do you need to do that you can do this?

First you need to activate SSH on your Raspberry Pi.

- over the GUI: `Preferences` >> `Raspberry Pi Configuration`
- or the CLI: `sudo raspi-config` >> `5 Interfacing Options` >> `P2 SSH` >> `Enable`

Now you can switch to your Windows computer and download/install FileZilla from [filezilla-project.org](https://filezilla-project.org/).

When you installed it launch it.

- Then click in the upper left `File` >> `Site manager`
- Now create a new site with clicking the button `New Site`
- On the right click the tab `General`
- Now enter in the `Host:` text field the IP address of your Pi (`hostname -I`).
- Choose as `protocol` the Secure File Transfer Protocol (`SFTP`)
- The `Logon Type:` is `Normal`
- Now enter your Pi username (`pi`)
- and your **long, secure & unique password**

And you are ready to go. Just click `Connect` at the bottom left and you can see in the main window of FileZilla in the right file hierarchy the file system of your pi. Also you can copy, move, edit files from there.

[source](https://www.raspberrypi.org/documentation/remote-access/ssh/sftp.md)

#### Swish (Windows, [Open Source](https://github.com/alamaison/swish))

If you want something more "native" under Windows you can use Swish, an native Windows SFTP client.

- Just download the client [here](http://www.swish-sftp.org/) and install it on your Windows computer. Nothing changed?
- Go to "my Device" in the Windows Explorer (there where you can see all your hard drives) and a new drive is there with the name "Swish"
- Now double click it and click at the top in the banner "Add SFTP Connection"
- Now input your desired name for the connection under `Lable:`
- Add under `Host:` your IP address and under `User:` your username and you are ready to create the connection
- Tipp: If you every time want to be directly in the home directory or in a specific directory enter your desired path under `Path:`
- Now after you created the connection double click the new icon and enter your password for the inputted user: Your file system of the pi natively in the Windows Explorer :raised_hands:

#### Solid Explorer File Manager (Android, [Trial free](https://neatbytes.com/solidexplorer/))

Because I used this feature way to often I want to add this although I think I paid something for the app (if you have working alternatives message me and I will add them :).

There are obviously countless SFTP Alternatives but here it is really simple:

- Start the app, click the plus (`+`) at the bottom right
- Click `New cloud connection`
- Choose `SFTP` and click `Next` at the bottom right
- Enter the IP address of your Pi under `Remote host name` and enter optional a specific path
- Enter a name for the connection under `Display name`
- Because I don't want to get into complicated things (I for myself couldn't do it) we only use the username and password for now (If you know how to do it more securely over a private key message me or add it yourself :)
- Click `Next` and add your username and password
- Click `Next` and again `Next` and check everything, then again `Next`
- And then finally click the big, fat `Connect` button
- If you now open the hamburger menu you can directly get into the file system of your Pi on any Android device :smiley:

## 6. Welcome to the console :)

### Introduction

The CLI (command line interface) is in contrast to the GUI (graphical user interface) solely text based.

This brings the advantage of printing out with very few commands small things like "Hello world!" to controlling and monitoring with some other commands a big server.

In addition, support is simpler due to the uniqueness of the commands.

If this is all Greek to you ("oder du verstehst bisher nur Banhof") just keep reading - it's really simple:

### Start the console

If you booted in the CLI environment without starting the GUI (see 4.) you obviously are already in the console. And if you booted into the desktop GUI environment you can click the terminal icon on the top bar to start the console.

But there is a third way (if you booted with a GUI):
You can press `Ctrl` + `Alt` + `t` to start the console everywhere without even touching the mouse.

If you now also want to go full screen just press `Alt` + `Space` and then `x`.

And if you want to close the terminal again just press `Ctrl` + `Shift` + `q`.

### Shortcuts

Typing is is easy for you and with the arrow keys you already know how to get back and forth in the current command. So what can you possibly do better or faster you ask?... The answer is... a lot:

---

- `Ctrl` + `a` brings you in no-time to **the begin** of your current command
- `Ctrl` + `e` brings you in no-time to **the end** of your current command
- `Ctrl` + `x` + `x` moves your cursor between the begin and the end of your current command

---

- `Ctrl` + `b` move backward one character (same as `←`)
- `Ctrl` + `f` move forward one character (same as `→`)

---

- `Alt` + `b` move backward one word (or go to the start of the currently cursor pointed word)
- `Alt` + `f` move forward one word (or go to the end of the currently cursor pointed word)

---

- `Ctrl` + `k` *kills* or better deletes everything of the current command from the begin to the current cursor position
- `Ctrl` + `w` *kills* everything of the current command from the current cursor position to the end
- `Ctrl` + `u` *kills* everything of the current command after the position where your cursor is
- But all those shortcuts don't really kill or delete the text parts - they rather save them to a clipboard so that you can paste with the shortcut `Ctrl` + `y` these parts in your current command at your current cursor position

---

- `Ctrl` + `p` replaces your current command with your *previous* entered command (in entered history)
- `Ctrl` + `n` replaces your current command with your *next* entered command (in entered history)

---

- `Ctrl` + `c` stops/aborts the current running program in the console/terminal
- `Ctrl` + `d` stops every currently running program (closes the console in this case)
- `Ctrl` + `l` cleans the whole terminal

---

Also there is the holy grail the `Tab` key. It completes commands, filenames, etcetera...
If you press the `Tab` key again it will autocomplete to the next logical command, filename, etcetera...

### Commands

Here are some simple commands you should know or are very helpful to know:

#### Text output command ("Hello world")

---

##### `echo`

`echo` + ... or "..." → output: ...

```tiki wiki
pi@raspberrypi:~ $ echo hello
hello
pi@raspberrypi:~ $ echo hello world!
hello world!
pi@raspberrypi:~ $ echo "hello world!"
hello world!
pi@raspberrypi:~ $ echo hello "world!" "what is happening?"
hello world! what is happening?hello "world!" "what is happening?"
pi@raspberrypi:~ $ ▮
```

You can even print a multiline text. Just let a simple `"` open and then enter line for line new text. If you are ready close it with typing a simple `"`. In between them you can just type enter and a new line will come up:

```text
pi@raspberrypi:~ $ echo hello "world! now press enter
> hello world! in a new line :o and now \"enter again\"
> wow again a new line... now we want to end by typing a " and pressing enter
hello world! now press enter
hello world! in a new line :o and now "enter again"
wow again a new line... now we want to end by typing a  and pressing enter
pi@raspberrypi:~ $ ▮
```

#### File system commands

---

##### `ls`

stands for *List directory contents* and lists the current content of the folder you are in.

Wait a second - we are in a folder?

That's right. The console is always in a specific directory which enables many possibilities you will later learn about. With this command you can list the contents of the current directory your console *is*.

Folders are in the case of the default Pi terminal blue and files white.

```text
pi@raspberrypi:~ $ ls
Desktop Documents Downloads Music Pictures Public python_games Templates Videos
pi@raspberrypi:~ $ ▮
```

But there are more things like only commands on Linux:
There are also command options.

In the case of a directory listener you probably also want to know the size, date, and more:

`-l` → long listing - get a list with size and date of creation and ...

```text
pi@raspberrypi:~ $ ls -l
total 36
drwxr-xr-x 2 pi pi 4096 Aug  1 14:59 Desktop
drwxr-xr-x 2 pi pi 4096 Aug  1 18:25 Documents
drwxr-xr-x 2 pi pi 4096 Aug  1 14:59 Downloads
drwxr-xr-x 2 pi pi 4096 Aug  1 14:59 Music
drwxr-xr-x 2 pi pi 4096 Aug  1 14:59 Pictures
drwxr-xr-x 2 pi pi 4096 Aug  1 14:59 Public
drwxr-xr-x 2 pi pi 4096 Jul  5 13:29 python_games
drwxr-xr-x 2 pi pi 4096 Aug  1 14:59 Templates
drwxr-xr-x 2 pi pi 4096 Aug  1 14:59 Videos
pi@raspberrypi:~ $ ▮
```

Explanation: ([used source](https://Linuxconfig.org/understanding-of-ls-command-with-a-long-listing-format-output-with-permission-bits))

- `d` stands for directory - `l` for a link - `c` for a character file
- `rwxr-xr-x` are the permissions applied to this *file* also called octets
  - the firs octet defines the permission for the file owner `rwx`
  - the second octet defines the permissions defined for the group `r-x`
  - the third and last part defines the permissions for everyone else `r-x`
    - The permissions are the following

       | `r`  | `w`   | `x`     |
       | ---- | ----- | ------- |
       | read | write | execute |

- `2` number of linked hard-links (links to that file/directory)
- `pi` the owner of the file/directory
- `pi` the group which this file/directory belongs to
- `4096` size of the file/directory
- `Aug  1 14:59` modification/creation date and time
- `Desktop` the file/directory name

`-a` → shows not only the *normal* files, but also the *hidden* ones that start with a `.`
(because in Linux everything (file,folder,device,command) is a file, a file that starts with `a` is a hidden file)

```text
pi@raspberrypi:~ $ ls -a
.             .cache  Documents       .idlerc    .pki         .themes     .WolframEngine
..            .config Downloads       .local     .profile     .thumbnails .Xauthority
.bash_history .dbus   .gconf          .minecraft Public       Videos      .xsession-errors
.bash_logout  Desktop .gstreamer-0.10 Music      python_games .vnc        .xsession-errors.old
.bashrc       .dmrc   .gtkrc-2.0      Pictures   Templates    .Wofram
pi@raspberrypi:~ $ ▮
```

the cool thing with the command options are that you can just combine them in one simple command like:

```text
pi@raspberrypi:~ $ ls -la
total 144
drwxr-xr-x 25 pi   pi   4096 Aug  4 14:46 .
drwxr-xr-x  3 root root 4096 Jul  5 12:41 ..
-rw-------  1 pi   pi   2162 Aug  4 01:26 .bashhistory
[too much unimportant code - I stop here]
pi@raspberrypi:~ $ ▮
```

---

Okay. So now we can find files in our current directory but can we probably also go into other directories?

Not a problem my friend:

---

##### `cd`

stands for *change directory* and will do the magic.

You just type in `cd` and after that your path - the directory you wanna go. In this case we want straight to the documents folder:

```text
pi@raspberrypi:~ $ cd Documents
pi@raspberrypi:~/Documents $ ▮
```

WOW. Did you just see that?
Wait a second, one more tip:

```text
pi@raspberrypi:~/Documents $ cd ~
pi@raspberrypi:~ $ ▮
```

The thing after `username@hostname:` is the path where your console/terminal currently *is*. :open_mouth:

The odd `~` is the sign for your home directory. If you changed your directory so much, that you lost yourself just enter `cd ~` and you are back home.

But there are more tricks:

With `cd ..` you go one folder upwards

```text
pi@raspberrypi:~ $ cd Desktop
pi@raspberrypi:~/Desktop $ cd ..
pi@raspberrypi:~ $ ▮
```

#### Create/Edit/Delete/View files

Next we probably want to create files (that means folders and files):

---

##### `mkdir`

stands for *Make directory* and creates a directory with the name you write after it.

```text
pi@raspberrypi:~ $ mkdir cool_folder
pi@raspberrypi:~ $ ls
cool_folder Desktop Documents Downloads Music Pictures Public python_games Templates Videos
pi@raspberrypi:~ $ mkdir cool_folder
mkdir: cannot create directory 'cool folder': File exists
pi@raspberrypi:~ $ mkdir Cool_folder
pi@raspberrypi:~ $ ls
cool_folder Desktop   Downloads Pictures python_games Videos
Cool_folder Documents Music     Public   Templates
pi@raspberrypi:~ $ ▮
```

Three things:

1. Creating a directory/folder is simple and you did it :raised_hands:
2. If the directory already exists you get an error prompt
   (`mkdir: cannot create directory 'cool folder': File exists`)
3. If you come from a Windows computer you probably wondered why there was no error prompt after I created first the folder `cool folder` and then `Cool folder` without any kind of error prompt. That is because of Linux. The file system is in contrast to Windows - if you put it simply - not case sensitive. You can create files and folders with the same name as long as there is a difference in large or lower case. On Windows computers you can't do this. Every file in a directory there can only have a unique name.
4. Wait a second, I want also to create files :disappointed:...

---

##### `touch`

creates a file with the name you write after it. :smiley:

```text
pi@raspberrypi:~ $ touch cool_file
pi@raspberrypi:~ $ ls
cool_file   Cool_folder Documents Music    Public       Templates
cool_folder Desktop     Downloads Pictures python_games Videos
pi@raspberrypi:~ $ touch Cool_file
pi@raspberrypi:~ $ ls
cool_file cool_folder Desktop   Downloads Pictures python_games Videos
Cool_file Cool_folder Documents Music     Public   Templates
pi@raspberrypi:~ $ ▮
```

---

**But attention:** If a file (this means a folder or a file) already is named `cool_file` and you enter `touch cool_file`. There will be no error prompt and there also won't be created anything. In such a case `touch` updates the timestamp of the file that is named `cool_file`.

---

After we now know how to create directories and files here an additional example for a longer path while using the command `cd`:

```text
pi@raspberrypi:~ $ mkdir Desktop/another_cool_directory
pi@raspberrypi:~ $ touch Desktop/another_cool_directory/hi
pi@raspberrypi:~ $ cd Desktop/another_cool_directory/
pi@raspberrypi:~Desktop/another_cool_directory $ ls
hi
pi@raspberrypi:~Desktop/another_cool_directory $ ▮
```

Another additional tip:
If you - although the path is already in the console - want the whole path of the directory your currently at just enter `pwd`:

```text
pi@raspberrypi:~Desktop/another_cool_directory $ pwd
/home/pi/Desktop/another_cool_directory
pi@raspberrypi:~Desktop/another_cool_directory $ ▮
```

---

Two things to go: Deleting files and viewing/editing them

Of course you could install programs that can do these things so much better (for example an advanced text editor like Vim), but for now we'll use the `nano` terminal editor, because it is already installed.

---

##### `nano`

is a simple text editor.

```text
pi@raspberrypi:~ $ nano
```

If you enter this command in the terminal will start a new CLI where you can write text like in a normal text editor.. just you are still in the terminal.

When you are finished just use the shortcut `Ctrl` + `x`. Now (if you wrote something) the editor asks if it should save the things you wrote. If you press `y` you now just need to type in a name for your file.

The cool thing is you can not only do much more with `nano` and creating files, you can also really simple edit existing files:

```text
pi@raspberrypi:~ $ nano existing_file
```

This will open the existing file named existing_file and you can edit the content of it. Saving is the same just quit `nano` with `Ctrl` + `x` and press `y` now just don't change the name of the file and you edited successfully a file.

---

##### `cat`

enables you to quickly view the content of a text file directly in the editor.

For example i just edit the existing_file in my home directory like in the command before and wrote `Hello world!` . When you now input `cat existing_file` you will see the content directly in the console:

```text
pi@raspberrypi:~ $ cat existing_file
Hello world!
pi@raspberrypi:~ $ ▮
```

---

##### Create short files with `cat` in the Terminal

`cat` originally was written to con**cat**enate 2 files, by writing the content from one File into another.

The command also can be used to write User input to a new File.

You only must use the `>` symbol, that instructs `cat` to write into the following file.

If the file not exist, it will be created. **!Warning!: If the file already exist, it will be overwritten**

```text
pi@raspberrypi:~/test $ cat > hello.txt
Hello World!
this is a text test file
pi@raspberrypi:~/test $ ▮
```

After writing all the text, we can exit the editor with typing `Ctrl + d`.

Now we created a new File `hello.txt`  and wrote some text in it.

We already know, how to display the content of a file with `cat`

```text
pi@raspberrypi:~/test $ cat hello.txt
Hello World!
this is a text test file
pi@raspberrypi:~/test $ ▮
```

[source](https://en.wikipedia.org/wiki/Cat_(Unix))

But how can you delete all these very unimportant files you created in the last 15 minutes?

---

##### `rm`

like *remove* [files].

Doesn't sound so difficult, doesn't it? Let's clean my desktop:

```text
pi@raspberrypi:~/Desktop $ ls
another_cool_directory existing_file hi tut tut.txt
pi@raspberrypi:~/Desktop $ rm hi
pi@raspberrypi:~/Desktop $ rm tut.txt
pi@raspberrypi:~/Desktop $ ls
another_cool_directory existing_file tut
pi@raspberrypi:~/Desktop $ ▮
```

But if we try to remove a directory there is an error prompt... let's learn a new command:

---

##### `rmdir`

like *remove directory*.

```text
pi@raspberrypi:~/Desktop $ ls
another_cool_directory existing_file tut
pi@raspberrypi:~/Desktop $ rm another_cool_directory
rm: cannot remove 'another_cool_directory': Is a directory
pi@raspberrypi:~/Desktop $ rmdir another_cool_directory
rmdir: cannot remove 'another_cool_directory': Directory is not empty
pi@raspberrypi:~/Desktop $ ▮
```

Okay. It seems like you only can delete empty directories. But of course we have a command for deleting also a not empty directory:

```text
pi@raspberrypi:~/Desktop $ rm -r another_cool_directory
pi@raspberrypi:~/Desktop $ ls
existing_file tut
pi@raspberrypi:~/Desktop $ mkdir new_empty_directory
pi@raspberrypi:~/Desktop $ ls
existing_file new_empty_directory tut
pi@raspberrypi:~/Desktop $ rmdir new_empty_directory
pi@raspberrypi:~/Desktop $ ls
existing_file tut
pi@raspberrypi:~/Desktop $ ▮
```

Damn. You're really fast. Some cool and helpful things before we go on with next steps:

#### Find out more about commands

Another essential command is

---

##### `man`

like *manual*

Type this command and after it the command you want to know more about (what does it, what are the command options, etcetera...).

For example I want to know more about the command `ls`:

```text
pi@raspberrypi:~ $ man ls
```

Then in the console/terminal a manual which you can scroll through opens, that contains all the information about the command `ls`. With pressing `q` you can leave the manual and are right back in the console/terminal. This works with every command.

#### Command history tricks

---

##### `history`

shows all the executed commands (very long! - my example is small)

```text
pi@raspberrypi:~ $ history
   1  echo hi
   2  echo hello world
   3  echo hello "world"
   4  ls
   5  ls -l
   6  ls -a
   7  ls -la
   8  history
pi@raspberrypi:~ $ ▮
```

(with the shortcut `Ctrl` + `r` you can search this history and when you think it's long enough type in `history -c` to clear it)

---

##### `!!`

runs the last executed command

```text
pi@raspberrypi:~ $ echo hello world!
hello world!
pi@raspberrypi:~ $ !!
echo hello world!
hello world!
pi@raspberrypi:~ $ ▮
```

#### Learn more commands and shortcuts

If you want to learn more shortcuts and commands (and believe us, there are so many) just search on the web. There are many sites (like our sources) that list cool commands and in the comments you will find more and more. The learning curve is very steep.

---

*Source of many shortcuts and many that we didn't told about: [skorks](https://www.skorks.com/2009/09/bash-shortcuts-for-maximum-productivity/)*
*Source of many commands and many that we didn't told about: [tecmint](https://www.tecmint.com/useful-Linux-commands-for-newbies/)*
*Even more commands: [raspberrypi.org](https://www.raspberrypi.org/documentation/Linux/usage/commands.md)*

### Commands advanced

But there is even more that you can do with commands:

#### Queue commands

If you don't get queue think of it like a command playlist. You could do for example this:

```text
pi@raspberrypi:~ $ cd Documents
pi@raspberrypi:~Documents $ mkdir Test
pi@raspberrypi:~Documents $ cd Test
pi@raspberrypi:~Documents/Test $ touch hi.txt
pi@raspberrypi:~Documents/Test $ cd ~
pi@raspberrypi:~ $ ▮
```

But this would require to input 4 commands and if you run programs you need to wait till one of the commands is ready and so on (like when you want to install many programs in a row).

Thanks to `&&` this is not a problem. Just put `&&` between the commands and exactly the same will happen without inputting each command after another, but with queuing them (or adding them to a playlist).

This will do the same as the last command line example:

```text
pi@raspberrypi:~ $ cd Documents && mkdir Test && cd Test && touch hi.txt && cd ~
pi@raspberrypi:~ $ ▮
```

You can do this with every command that exists. It's just a simple playlist/queue.

#### Search CLI output

If you for example have a directory with 42 files and you enter the `ls -l` command you probably are pretty sure which file you are searching (or know something of the filename or know the file type).

To optimize the "long" search in such a case there is the command `grep`.

It's like a really simple regular expression text search that only displays lines in the CLI or files that contain a keyword you write after it. Input `ls -l | grep 'keyword'`

For a better understanding how `grep` works look at another example:

##### Search a text file

You are in this example a system admin at a cyber security organization and Alice forgot her password and asks you to give it to her. Because you have a text file with all the passwords of everyone in the form you have now the job to say her her password as fast as  possible:

File: `Documents/SecureFiles/nothingToSeeGoAway.txt`

```text
Password for:
Jules: 123456
ObiLan: IhaveTheHighGround
Mona: securePassword
Nick: areyoufreakingkiddingme
Thomas: saveTheseDamnPasswordsAsHashesAdmins!!
Bernd: WhyAliceAlwaysForgetsHerPassword?
Alice: WhyDoIAlwaysForgetMyPassword????3897584
Bob: aliceIsCool
Jim: HiDwight
```

(Disclaimer: Never save passwords like this: THIS IS JUST A SIMPLE EXAMPLE FOR `grep`)

- You could now enter this:

  ```text
  pi@raspberrypi:~ $ cat Documents/SecureFiles/nothingToSeeGoAway.txt
  ```

  and would get every line of the document. This would mean you would have to read every line...

- But if you instantly only want the lines that contain "Alice" you obviously would use `grep` like this:

  ```text
  pi@raspberrypi:~ $ cat Documents/SecureFiles/nothingToSeeGoAway.txt | grep 'Alice'
  Bernd: WhyAliceAlwaysForgetsHerPassword?
  Alice: WhyDoIAlwaysForgetMyPassword????3897584
  pi@raspberrypi:~ $ ▮
  ```

  You see: You now only got the lines which contain the text "Alice".
  Plus: Per default the terminal highlights it for you (if not use the option `--color`)

There are also obviously many command options (read the `man grep` page therefore), but one cool option is the addition of `i`. The normal `grep` command searches case sensitive, with the command `grep -i` this isn't the case (BaDummTsss) and you now get every line that contains in some way `Alice`:

```text
pi@raspberrypi:~ $ cat Documents/SecureFiles/nothingToSeeGoAway.txt | grep 'Alice'
Bernd: WhyAliceAlwaysForgetsHerPassword?
Alice: WhyDoIAlwaysForgetMyPassword????3897584
Bob: aliceIsCool
pi@raspberrypi:~ $ ▮
```

##### But there is even more besides `cat file | grep 'word'`

 ([Source of even more](https://www.cyberciti.biz/faq/howto-use-grep-command-in-linux-unix/))

- Search for a word directly in a text file:

  ```text
  grep 'word' filename
  ```

- Search for a word directly in many text files:

  ```text
  grep 'word' file1 file2 file3
  ```

- Search the current output in the terminal of a command for a word:

  ```text
  commandThatCreatesATextOutput | grep 'word'
  ```

## 7. Install additional software/programs

Installing programs is on Linux or rather on Raspbian quite different if you come from OSX or Windows.

Therefore here a quick and dirty explanation of operating systems and especially Linux:

### The operating system

#### The kernel

The kernel is the core computer program. It has the full control over everything of the system and is the first thing that gets started on a computer start-up.

It handles all connected peripherals, input, output and thus controlling on what other programs having access to.

Systems like Windows and Linux have an underlying kernel.

Nevertheless there are big differences between especially these two besides that Linux is an open source developed and public viewable kernel and the Windows kernel is a cooperation secret.

#### Linux distributions and Windows

Probably you know Linux distributions better under the names Arch Linux, Debian, Fedora, Gentoo, Manjaro, Mint, Ubuntu, Raspbian, etcetera.

These so named *distributions* don't have specific kernels. They all have the same kernel, the Linux kernel. \*

But only the kernel won't bring you far. Every system is only so useful as the programs that are installed on it. Like.. what would Windows be if you wouldn't have a GUI.

And because there are so many possible GUI's and file managers, file editors and network programs and even more programs that some people created distributions. They all consist of the Linux kernel and many chosen programs/packages.

You can think of Windows like the only distribution of the Windows kernel.

The cool thing about this on Linux distributions is that you can theoretically install every Linux program on every Linux distribution, this means also every GUI and so on.

\* there are ways to strip a kernel down in size but they are nevertheless all based on one Linux kernel

### How to install these... packages

It's quite simple how to install packages onto your Raspberry Pi running Raspbian:

Just type into the console `apt-get install` and enter to install the software:

```text
pi@raspberrypi:~ $ sudo apt-get install <name of the software>
```

Why does this work?
Every distribution has it's own repository where they all saved these packages that work well with their systems. By typing this you can download it and get the newest for your distribution available package of the software you want.

#### Example: Lets install Firefox

Normally on Windows you go to the Mozilla Firefox website go to the download page. Download the executable and run it. Then you wait till it's finished installing.

How's that on our Raspbian?

Funny thing I just found out: Firefox isn't listed in the console under it's real name (because it still supports flash which requires an *x86* processor but the raspberry pi has an 64 bit *ARM* processor) but under the name **Iceweasel**. So let's cut to the chase:

```text
pi@raspberrypi:~ $ sudo apt-get install iceweasel
.... text
pi@raspberrypi:~ $ ▮
```

Okay.... did we install it now or what did we do?

If it only was easy to start Firefox now... Let's try something:

```text
pi@raspberrypi:~ $ iceweasel
pi@raspberrypi:~ $ ▮
```

Probably Firefox just launched and now you know it's installed.

#### Example: Lets install cowsay

To install this very important package just type in:

```text
pi@raspberrypi:~ $ sudo apt-get install cowsay
```

After the installation you can now use this command:

```text
pi@raspberrypi:~ $ cowsay Hi, I\'m a cow.
```

And enjoy the result. :smiley: :cow:

#### Example: Lets watch a movie

Before we can start and enjoy it, we must install `telnet` :

```text
pi@raspberry:~ $ sudo apt-get install telnet
```

After the installation you can use this command and get surprised :3

```text
pi@raspberry:~ $ telnet towel.blinkenlights.nl
```

*watching movie\*

If you now (after watching the complete movie) want back to the console, without restarting it, you must type in the exit signs.

In this case we must type in `Ctrl + ]` and then `quit` .

My Problem was, that (idk why) the Tastatur layout was different during this command.

So i must guess were the bracket was and on my (German) Tastatur it was on the `+` Plus sign.

Sooo just try some Symbols, while holding `Ctrl` and you will find a way out of telnet ^^ (:thinking: "No! Try not! *Do or do not*, there is not try.") (<- that wasn't a hint which movie you gonna watch xP)

[Thanks Simon Jansen. This is a Link to his created Java Applet of the Film](http://www.asciimation.co.nz/)

[Website of the human, who host it](http://blinkenlights.nl/services.html)

### What can I do when a new version of my installed software gets released

That is also quite cool. Remember when I wrote that every distribution has it's own repository with all the  latest packages of every program you install over the package manager `apt`?

That's very handy, because there is an command that compares all the versions and the kernel on your Raspberry Pi with the ones in the repository and updates the things that aren't latest on your Pi.

You therefore need to know two commands:

1. Update/Compare the local repositories with the latest repositories online

   ```text
   pi@raspberrypi:~ $ sudo apt-get update
   ```

2. Download the new packages (if there are any new ones)

   ```text
   pi@raspberrypi:~ $ sudo apt-get upgrade
   ```

When the command terminates all of your system software (kernel and over packages) should be the latest of your current distribution.

Remember, that `apt` is the paket-manager of Debian Derivates. If you're using arch/fedora/etc. you must search your own manager. Here a uncomplete List of some managers:

- `pacman`for Arch Linux and (i think so) all Derivates
- `dnf` on Fedora (since version 22) (older versions: `yum`, less powerfull)
- I never used others but on [this Wikipedia Site](https://en.wikipedia.org/wiki/Package_manager#Comparison_of_commands) are written some more :)

## 8. Program on it

### Scripting Languages

Scripts in the following languages *just run* with one command.

#### Bash

First let's create a bash script file:

```text
pi@raspberrypi:~ $ nano
```

Then we just write a simple bash script in `nano`:

```bash
##!/bin/bash

## A Comment
echo "WOW You just executed a Bash script :o"
```

Then we save this by clicking `Ctrl` + `x` and `y` and entering the name `bash_test_script.sh` .

Now we can execute it:

```text
pi@raspberrypi:~ $ bash bash_test_script.sh
WOW You just executed a Bash script :o
pi@raspberrypi:~ $ ▮
```

#### Python

First let's create a python script file:

```text
pi@raspberrypi:~ $ nano
```

Then we just write a simple python script in `nano`:

```python
"""Hello world script."""

## A comment
print("WOW You just executed a Python script :o")
```

Then we save this by clicking `Ctrl` + `x` and `y` and entering the name `python_test_script.py` .

Now we can execute it:

```text
pi@raspberrypi:~ $ python python_test_script.py
WOW You just executed a Python script :o
pi@raspberrypi:~ $ ▮
```

---

But when we speak about python we have even more possibilities on the Pi.

If you enter `python` in the console you enter a live python editor where you can program live:

```text
pi@raspberrypi:~ $ python
Python 2.7.9 (default, Sep 17 2016, 20:26:04)
[GCC 4.9.2] on linux2
Type "help", "copyright", "credits" or "license" for more inforamtion.
>>> ▮
```

Now we can do fun stuff in the terminal (everything we want to do):

```text
>>> 2 + 40
42
>>> a = 2 + 6 * 7
>>> b = -2
>>> a + b
42
>>> ▮
```

With typing `Ctrl` + `d` you can exit the python console in the terminal again.

---

You even have one more option - to program on the python 3 console IDE.

If the console isn't preinstalled: install it :D. You should already know that. (hint: `sudo apt-get install idle3`)

And if it doesn't work, because you are using a ssh connection, then follow the instructions on [this raspberrypi forum page](https://www.raspberrypi.org/forums/viewtopic.php?f=32&t=54312) (unfortunately i couldn't solve this Problem and i don't think that it's that important ) :see_no_evil:

To start it you can search and click the IDE icon **or**...

...we use the glorious mighty console:

```text
pi@raspberrypi:~ $ idle3
```

Of course you can also open with this command directly any preexisting file like the one we just created:

```text
pi@raspberrypi:~ $ idle3 python_test_script.py
```

---

##### Python 2 and 3

There are currently (2017) two versions of Python installed out of the box (on Raspbian). The language split itself a long time ago because of big differences (2008) and is right now only supported in version 2 for some years:

**That means Python 2 which is default on Raspbian is not the future and 'the best' Python.**

That means if you want to do more with Python (especially in the future) and don't want encoding problems and other things use Python 3!

You can very simple do this by using the following commands:

- instead of  `python script.py` use `python3 script.py`
- instead of `pip install module` use `pip3 install module`

#### PHP

PHP is mostly used in combination with websites/webservers. The cool thing is that PHP is a server-side scripting language - this means the `.php` script will be executed on the webserver and the result of the script will be send to a user after he wanted to see the PHP file.

You can use this and make dynamic websites like this:

Let's create a PHP script file:

```text
pi@raspberrypi:~ $ nano
```

Then we just write a simple PHP script in `nano`:

```php
<html>
    <head>
        <title>PHP Test</title>
    </head>
    <body>
        <?php echo '<p>Hello World</p>'; ?>
    </body>
</html>
```

Looks just like a normal website beside the tag `<?php ... ?>` (the tag can appear  everywhere in the document and also more than once). Everything that is between this tag will PHP convert to HTML content - the user isn't even able to see this code he just sees the following:

(Obviously first save this by clicking `Ctrl` + `x` and `y` and entering the name `php_test_script.php`)

```text
pi@raspberrypi:~ $ php php_test_script.php
<html>
    <head>
        <title>PHP Test</title>
    </head>
    <body>
        <p>Hello World</p>
    </body>
</html>
pi@raspberrypi:~ $ ▮
```

Therefore, when you run a PHP server the server automatically does this conversion every time a user wants to see a `.php` document and get's back only a normal `.html` website.

You can easily install it with the command: `sudo apt-get install php` (on debian/-derivates)

#### Ruby

Let's create a Ruby script file:

```text
pi@raspberrypi:~ $ nano
```

Then we just write a simple Ruby script in `nano`:

```ruby
## A Ruby script

puts 'WOW You just executed a Ruby script :o'
```

now let's save this by clicking `Ctrl` + `x` and `y` and entering the name `ruby_test_script.rb` .

Now we can execute it (if its not installed: `sudo apt-get install ruby` (on debian/-derivates)):

```text
pi@raspberrypi:~ $ ruby ruby_test_script.rb
WOW You just executed a Ruby script :o
pi@raspberrypi:~ $ ▮
```

#### Lua

Let's create a Lua script file:

```text
pi@raspberrypi:~ $ nano
```

Then we just write a simple Lua script in `nano`:

```lua
-- A Lua script

print ("WOW You just executed a Lua script :o")
```

now let's save this by clicking `Ctrl` + `x` and `y` and entering the name `lua_test_script.lua` .

Now we can execute it:

```text
pi@raspberrypi:~ $ lua lua_test_script.lua
WOW You just executed a Lua script :o
pi@raspberrypi:~ $ ▮
```

### Compiled Languages

These languages need to be compiled before you can execute your written code.

#### C

First let's create a C script file:

```text
pi@raspberrypi:~ $ nano
```

Then we just write a simple C script in `nano`:

```c
##include <stdio.h>

main()
{
    printf("Hello world!\n");
}
```

Then we save this by clicking `Ctrl` + `x` and `y` and entering the name `c_test_script.c` .

But now there is a problem. C isn't a script language.
It needs to be compiled before it can be executed.

So let's compile it to a executable file: ([very interesting stack overflow answer to this problem](https://raspberrypi.stackexchange.com/a/5600))

```text
pi@raspberrypi:~ $ gcc -Wall c_test_script.c -o executable_c_file
c_test_script.c:3:1: warning return type deafaults to ´int´ [Wreturn-type]
main()
 ^
c_test_script.c: In function ´main´:
c_test_script.c:6:1: warning: control reaches end of non-void function [Wreturn-type]
 }
 ^
pi@raspberrypi:~ $ ▮
```

We see all this (for now) not important comments/logs because through `-Wall` we enabled compiler warnings. This is really helpful for debugging a c program. `GCC` is the compiler that takes the code and converts it into an executable file. `-o` is needed to tell `GCC` to compile.

Now we can execute it:

```text
pi@raspberrypi:~ $ ./executable_c_file
Hello world!
pi@raspberrypi:~ $ ▮
```

#### Java

First let's create a Java file:

```text
pi@raspberrypi:~ $ nano
```

Then we just write a simple Java script in `nano`:

```java
/**
 * Hello World program
 */
public class java_test_script {

    /**
     * Main method
     */
    public static void main(String[] args) {
        // A wild comment
        System.out.println("Hello world!");
    }

}
```

Then we save this by clicking `Ctrl` + `x` and `y` and entering the name `java_test_script.java` .

Now we have the same *problem* like C.
We first need to compile our code before we can execute it:

```text
pi@raspberrypi:~ $ javac java_test_script.java
pi@raspberrypi:~ $ ▮
```

This creates a executable file with the same name that we can now execute:

```text
pi@raspberrypi:~ $ java java_test_script
Hello world!
pi@raspberrypi:~ $ ▮
```

---

If you are more interested to learn Java I can't recommend you more Eclipse.
A great IDE to develop Java in and export it:

```text
pi@raspberrypi:~ $ sudo apt-get update && sudo apt-get upgrade
pi@raspberrypi:~ $ sudo apt-get install eclipse
```

Then wait some minutes, eat something healthy, do some sport and then finally

```text
pi@raspberrypi:~ $ eclipse
```

Oh wait, wait again some minutes ... and then... you are in the eclipse IDE :smiley:

Now you can develop really cool Java code in a GUI that checks every action you take so the compile process will never print errors if you follow eclipse ;)

**Edit:** Probably you will notice very soon that it's very slow (at least the startup time - when it's running it's okay) - but you can use it on your Windows PC or Linux PC without these very long start times.

#### C\#

First let's create a C# file:

```text
pi@raspberrypi:~ $ nano
```

Then we just write a simple C# script in `nano`:

```c#
using System;

// wild comment
class HelloWorld
{
    static void Main(string[] args)
    {
      Console.WriteLine("Hello World!");
    }
}
```

Then we save this by clicking `Ctrl` + `x` and `y` and entering the name `cs_test_script.cs`.

Now we have again the same *problem* like C - but without further preinstalled options.

Because of that let's install one:

```text
pi@raspberrypi:~ $ sudo apt-get update
pi@raspberrypi:~ $ sudo apt-get install mono-complete▮
```

With `mono` you can compile and execute C# code.

After installing the complete `.Net` framework let's first compile our test code:

```text
pi@raspberrypi:~ $ gmcs cs_test_script.cs
pi@raspberrypi:~ $ ▮
```

We have now created an executable named `cs_test_script.exe`, let's run it:

```text
pi@raspberrypi:~ $ mono cs_test_script.exe
Hello World!
pi@raspberrypi:~ $ ▮
```

Tada, you just compiled and executed your probably first C# code!

#### C++

First let's create a C++ script file:

```text
pi@raspberrypi:~ $ nano
```

Then we just write a "simple" C++ script in `nano`:

```c++
##include <iostream>

//very wild comment
int main() {
  std::cout << "Hello World!" << std::endl;
  //don't ask me (undefinedCoding) what 'std::cout <<'... etc. mean :see_no_evil:
  return 0;
}
```

Then we save this by clicking `Ctrl` + `x` and `y` and entering the name `cpp_test_script.cpp` .

So let's compile it to a executable file (we already installed the gcc Compiler while programming C):

```text
pi@raspberrypi:~ $ g++ cpp_test_script.cpp -o executable_cpp_file
pi@raspberrypi:~ $ ▮
```

Now we can execute it:

```text
pi@raspberrypi:~ $ ./executable_cpp_file
Hello World!
pi@raspberrypi:~ $ ▮
```

:baby_chick:

## 9. Set up a local webserver

### A *normal* webserver (Apache)

First we install Apache:

```text
pi@raspberrypi:~ $ sudo apt-get install apache2 -y
```

By default there will be an instant *normal* web server created (on your local network).

You can get it anywhere on your local network by typing in your current IP address (`hostname -I`) or local also under `localhost` into the browser search bar.

If you probably also want to change the content of your local server just got to the directory `/var/www/html/` and edit for example the file `index.html` which will be displayed if someone enters the IP address of your Pi.

[source](https://www.raspberrypi.org/documentation/remote-access/web-server/apache.md)

For example:

```text
pi@raspberrypi:~ $ sudo rm /var/www/html/index.html
pi@raspberrypi:~ $ sudo touch /var/www/html/index.html
pi@raspberrypi:~ $ sudo nano /var/www/html/index.html
```

Then edit in `nano` the file `index.html` to the content `Hello world!<br>This is HTML`.

After saving this you should instantly by searching for the IP address of the Pi see these words on the website.

#### Enable SFTP in html directory (`chmod`)

If you use SFTP you probably noticed that FileZilla blocks uploads. With the following commands...

```text
pi@raspberrypi:~ $ cd /var/www/
pi@raspberrypi:~/var/www $ sudo chmod a+w html
pi@raspberrypi:~/var/www $ sudo chmod a+w html/index.html
pi@raspberrypi:~/var/www $ ▮
```

...you give everyone writing rights in this folder and now everything should work with FileZilla.

If you want to know more about `chmod` look here: [source](http://www.dummies.com/computers/raspberry-pi/working-with-file-permissions-on-your-raspberry-pi/)

### PHP server

When we want to use PHP there isn't much more we need to do.

Let's start by installing PHP5 and the Apache PHP5 module via the package manager:

```text
pi@raspberrypi:~ $ sudo apt-get install php5 libapache2-mod-php5 -y
```

Because we used Apache before when setting up and running the *normal webserver* the web files are in the same directory as before and the IP address will be the same.

If you now visit the website again there should be no change.

But you can now use the PHP server based preprocessor. What that means?
It means that you can compute things on the server - change text, load files, handle some things and etcetera - and then send a `.html` file back to the user that opened the website over the IP address.

This is really cool because the user not only doesn't know that the web page was preprocessed (has no access to important files or other) and you can develop simple dynamic pages with logins that are different for every user and so on. Just search the web if you are interested in PHP.

[cool website for learning php](https://nudelprogrammer.12hp.de/)

#### Small example

But here one small example.

1. Let's go back into the folder:

   ```text
   pi@raspberrypi:~ $ cd /var/www/html
   pi@raspberrypi:/var/www/html $ ▮
   ```

2. Then remove the `.html file`:

   ```text
   pi@raspberrypi:/var/www/html $ rm index.html
   pi@raspberrypi:/var/www/html $ ▮
   ```text
   You also can change the Name of the File from index.html to index.php and then edit it:

   ```text
   pi@raspberrypi:/var/www/html $ mv index.html index.php
   pi@raspberrypi:/var/www/html $ ▮
   ```

   (`mv` is the move command and in this case we "move" the old file into the new one)

3. And create a new php file with the following content with `nano` (or another text editor):

   ```text
   pi@raspberrypi:/var/www/html $ nano index.php
   ```

   Content:

   ```HTML
   <!DOCTYPE html>
   <html>
       <head>
           <title>Title: <?php echo "hello world"; ?></title>
       </head>
       <body>
           <h1>Heading</h1>
           <p>
               <?php
               $currentDateTime = date('Y-m-d H:i:s');
               echo "You've downloaded the webpage at ";
               echo $currentDateTime;
               echo ".";
               ?>
           </p>
       </body>
   </html>
   ```

4. Now save the file and visit the webpage again (over the Pi's IP address):

   You now should see (if you enter the IP address of the Pi in the browser) a webpage with the title "Title: hello world" and the webpage should have a heading named "Heading" and below it the current time when the webpage was loaded (like "You've downloaded the webpage at 2017-08-23 22:30:00.").

### SQL server

Couldn't setup MySQL. If somebody out there was more successful than me please make a pull request or say me in another way how you could do it. (or commit it directly?) :see_no_evil:

### SFTP server

Now something that is mostly only interesting for you at home but really great:

You can use your Raspberry Pi as a home network media center or also as an drive on Windows. All thanks to SFTP.

Secure File Transfer Protocol is not only way more secure (because it works over SSH), way more performant and more advanced than FTP ([read this article for more detailed information](https://southrivertech.com/whats-difference-ftp-sftp-ftps/)), it's also really simple to work with when you want to setup a home network media center.

#### Windows Drive

Sadly Windows itself doesn't natively SFTP - only FTP - but there is a really fast and simple workaround for that:

1. Download [Swish](http://www.swish-sftp.org/) and install it on your Windows computer.
2. Because nothing changed.. what the hell did you do?
3. Go to "This Pc" in Windows Explorer and see that there is a new Drive named Swish.
4. Click `Add SFTP Connection` and enter again your IP Address, Username, enter as path `/home/YOURUSERNAME` and give it a name/label
5. Now double click on the created connection icon and enter your password (for your YOUSERNAME)

Now you can delete files, add them, rename them and more natively over your Windows Explorer.

#### Home network media center distribution (with Kodi as receiver)

But like we now want everywhere in the home network access to pictures, music and videos on our Raspberry Pi.

Nothing simpler than that thanks to Kodi. Kodi is an Open Source Media Center application that we will use because it is fast, Open Source, supports seamless SFTP and exists for [Android](https://play.google.com/store/apps/details?id=org.xbmc.kodi&hl=en), [Windows (App store)](https://www.microsoft.com/de-de/store/p/kodi/9nblggh4t892), Linux distributions, [etcetera](https://kodi.tv/download).

1. Install it on the device of your choice and start Kodi. (I did install it on my Android phone (6.0) and on my Amazon Fire TV stick).
2. Then, because you probably don't have any sources at the begin you will get asked `Enter file section`.
3. Now you click `Add videos` or `Add Music` or something else depending on where you clicked.
   (If nowhere you can read this, but you read `Files` click this)
4. A popup window will open itself and ask if you want to add any sources (for example `Add video source`.
5. Click browse to get into another popup window. There you want to click the list entry `Add network location`.
6. Because you want to connect to the Pi with the fast, secure and reliable SFTP protocol we change the protocol to `Secure Shell (SSH / SFTP)`
7. Now do the same thing you did so far every SFTP Setup and enter your Pi's IP address (@`Server address`, you username (@`Username`), your password (@`Password`) and click `OK`.
8. You will now get back to the list where you can browse through connected sources (`Browse for new share`) and can now simply click the `sftp://YOURIPADDRESS:22` and browse to your folder that you want to add to this category (`home/YOURUSERNAME/Music` for example) and confirm the location.
9. Now Kodi will need some time to search through all your files, but when it's ready you can stream music, video, image, and more files seamless from your Pi to Kodi on every supported OS that is connected to your home network.

You can even add more things and do even more cool things with Kodi but this is not a Kodi tutorial - just how you can use this Open Source software to get a simple and secure, but also great home network media center.

DISCLAIMER:
To get this working  you first need a fast home network connection (at my place over old telephone lines and two routers and then over 5Ghz Wi-Fi to the Amazon Fire TV Stick I have around 80mbps). And because even the Pi has it's limits you need to accept that it cannot deliver many files to many users at the same time and also not big files to one person at a time.
For me music, video and picture streaming was no problem, but a 4K video file of the Blender demo video "Tears of Steel" @6,27 GB could not be streamed (which was the case because of a mix of the *bad* home network bandwidth - but the main reason was I think the rather *slow* Pi). As long as you are in my range of hardware 1080p videos shouldn't be a problem for you and music/picture streaming should work great too.

## 10. Automated tasks scheduler (`cron`)

[Link to the section about `cron` of the official Raspberry Pi documentation](https://www.raspberrypi.org/documentation/linux/usage/cron.md)

Cron jobs are a really cool thing that you can use as Linux user.

Over the cron scheduler you can program to run script at a time you want every week/year/minute/hour/etcetera. And it's so easy to use on Raspbian because there is even a GUI version of it preinstalled.

### Create a script for a `cron` job

You can at this point create whatever you want. Because this is a demo tutorial I will not setup a connection to a Mail API or something other, but the possibilities are endless.

We will just make a simple python script that creates a log entry every time the script runs - a simple demo of the mighty cron scheduler:

```python
## -*- coding: utf-8 -*-

"""Python script for a cron job function demo."""

import datetime
import os

## this get's us the path of the PI's home directory
## this is important, because every cron job script will be
## run from the home directory - even when it's not there
PATH_HOME_DIR = os.path.expanduser('~')

## Directory where we want to create the log
PATH_FILE_DIR = os.path.join(
    PATH_HOME_DIR, 'Documents/GitHubBeta/RaspiForBeginners/scripts')

## Path of the log file
PATH_FILE = os.path.join(PATH_FILE_DIR, 'log.txt')

## Check if the directory exists, if not create it
if not os.path.exists(PATH_FILE_DIR):
    os.makedirs(PATH_FILE_DIR)

## get the current time
DATE_TIME = datetime.datetime.now()
DATE = DATE_TIME.date()  # gives date
TIME = DATE_TIME.time()  # gives time
DATE_STRING = str(DATE.year) + "-" + \
    str(DATE.month).zfill(2) + "-" + str(DATE.day).zfill(2)
TIME_STRING = str(TIME.hour).zfill(2) + ":" + \
    str(TIME.minute).zfill(2) + ":" + str(TIME.second).zfill(2)

## create a file and add the current time or if it exists just add the current time
with open(PATH_FILE, "a+") as text_file:
    text_file.write("The script was executed at " +
                    TIME_STRING + " on " + DATE_STRING + "\n")

## read file to the console (https://stackoverflow.com/a/5214587/7827128)
with open(PATH_FILE) as file:
    COMPLETE_FILE = file.readlines()

## strip every entry and print it to the console (remove '\n')
for rows in COMPLETE_FILE:
    print(rows.strip())
```

Every time this python script runs it will add an entry of the current time to the text file `home/USERNAME/Documents/Documents/CronDemoLog/log.txt`.

With this you can check if the cron scheduler works or not.

So let's copy it somewhere on the Pi (I copied it to `home/USERNAME/script.py`) and run it with the console:

```text
pi@raspberrypi:~ $ python script.py
This script was executed at 14:7:0 on 2017-8-10
pi@raspberrypi:~ $ ▮
```

Your output should get one line more every time you enter this command:

```text
pi@raspberrypi:~ $ python script.py
This script was executed at 14:7:0 on 2017-8-10
This script was executed at 14:8:8 on 2017-8-10
pi@raspberrypi:~ $ ▮
```

You can also always read the file by using `cat`:

```text
pi@raspberrypi:~ $ cat Documents/CronDemoLog/log.txt
This script was executed at 14:7:0 on 2017-8-10
This script was executed at 14:8:8 on 2017-8-10
pi@raspberrypi:~ $ ▮
```

### Create a `cron` job

Now we are ready to create our first `cron` job.

#### GUI

Therefore we start the GUI with the command:

```text
pi@raspberrypi:~ $ gnome-schedule
```

If this doesn't work install the GUI with this command:

```text
pi@raspberrypi:~ $ sudo apt-get update && sudo apt-get install gnome-schedule
```

- Now that we opened the GUI click `New` at the top left
- and in the popup window `A task that launches recurrently`
- then enter a description and as command enter the command you used to run the script before (`python script.py`)
- If you do not want to check if it works every hour go to `Advanced` and
- click `Edit` at the same height as `Minute`
- then click `Every minute` and confirm everything

[to continue skip the Terminal paragraph and continue with "Output"]

#### Terminal

Let's create our first `cron` job with the mighty console. Therefore we enter the following command:

```text
pi@raspberrypi:~ $ crontab -e
```

*Eventually you now also enter your favorite text editor - just enter the number of it (for beginners I recommend nano).*

The document you see right now is a list of all cron jobs (should be empty if you never before created a cron job).

##### Example

This is how each line will look like - for example two lines from my current cron file:

```text
*/12 * * * * python3 Documents/SubstitutePlanNotifierAEG/script.py
01 04 1 1 1 python3 Documents/NewYearSurpriseBot/script.py
```

Each line/`cron` job consists of

- five time/date entries which are separated by a blank from another, then another blank
- followed by a command that should be executed
- followed by a newline character `\n`

| Minute + `' '`     | Hour + `' '`   | Day + `' '` | Month + `' '` | Weekday + `' '` | Command                                  | Newline (`\n`) |
| ---------------- | ------------ | --------- | ----------- | ------------- | ---------------------------------------- | -------------- |
| */12             | *            | *         | *           | *             | `python3[...]`                           | `\n`           |
| Every 12 minutes | At all hours | Every day | Every month | Every weekday | Execute this command in the home directory | Entry is over  |
| ...              | ...          | ...       | ...         | ...           | ...                                      |                |

##### Explanation of each entry

| Entry              | Content                                  |
| ------------------ | ---------------------------------------- |
| **Minute + `' '`**   | a number between 0 and 59 + a space      |
| **Hour + `' '`**     | a number between 0 and 23 (0 = midnight) + a space |
| **Day + `' '`**      | a number between 1 and 31 + a space      |
| **Month + `' '`**    | a number between 1 and 12 + a space      |
| **Weekday + `' '`**  | a number between 0 and 6 (0 = Sunday) + a space |
| **Command**        | the command that should be executed in the home directory |
| **Newline (`\n`)** | cron job is no over - now you can declare in a new line a new cron job |

##### Explanation of Operators

| Operator | Use                                      |
| -------- | ---------------------------------------- |
| **`*`**  | If you enter an asterisk this means you want to execute the command every possible time. (if you enter an asterisk for the minute, hour, day, month, weekday the command will be executed every minute all day ... all year: `* * * * * command`) |
| **`,`**  | If you for example want to run a command on Sunday and Saturday you can enter both numbers for the days and separating them with a comma: `* * * * 0,6 command` |
| **`-`**  | If you want to execute the command all week but not on the weekend you can use the period operator: `* * * * 1-5 command` |
| **`*/`** | But what if you want to run a command multiple times per time unit like for example every 10 minutes? You could enter `0,10,20,30,40,50 * * * * * command` but there is a better way if you use the asterisk slash operator: `*/10 * * * * * command` . `*/10` means that for all possible numbers modulo 10 == 0 (you divide every possible time/date unit number as long by 10 with rest till you only have a  rest that is smaller than 10 and then look if the rest is zero) this script will be executed. In this case this would mean 0%10=0, 10%10=0, 20%10=0, 30%10=0, 40%10=0, 50%10=0 so it is the same as writing down `0,10,20,30,40,50`. |

##### There is even more

`Cron` even supports special strings that can be used instead of the time/date units:

| String                | Meaning                                  |
| --------------------- | ---------------------------------------- |
| `@reboot`             | Execute command at startup               |
| `@yearly`/`@annually` | Execute command when a new year begins (the same as `0 0 1 1 *`) |
| `@monthly`            | Execute command when a new month begins (the same as `0 0 1 * *`) |
| `@weekly`             | Execute command when a new week begins (the same as `0 0 * * 0` = week starts at Sunday!) |
| `@daily`/`@midnight` | Execute command when a new day begins (the same as `0 0 * * *` ) |
| `@hourly`             | Execute command when a new hour begins (the same as `0 * * * *`) |

##### Add new cron job

Simply add a new line to the file you just have opened via `crontab -e`, enter either the five date/time entries separated by one space or a special string, then another space and the command you want to run at the just entered times. Now save the document and everything should work :smile:.

For demo purposes we want to run the script every minute - this means we need to execute *every minute* (`*`), *every hour* (`*`), *every day* (`*`), *every month* (`*`), *every weekday* (`*`) and our *command* is `python path/to/script.py` (or other if you named the script different - always consider that this command will be run from the home directory [`/home/username`]). That means all in all one line should look like this:

```text
* * * * * python path/to/script.py
```

---

If you want to run a script that needs root privileges (`sudo`) you need to access the cron document with:

```text
pi@raspberrypi:~ $ sudo crontab -e
```

---

If you want to know more about `cron` jobs or `crontab` visit the `man` page or look here: [https://help.ubuntu.com/community/CronHowto](https://help.ubuntu.com/community/CronHowto) which was also the source of the Terminal paragraph.

#### Output

(*But how can I be sure that this thing really works?*)

Now wait some minutes and drink some water or tea or eat some fruits and vegetables . It's healthy :)

When you come back just run the same `cat` command you run before (`cat Documents/CronDemoLog/log.txt`) to see if it worked. It should look like this:

```text
pi@raspberrypi:~ $ cat Documents/CronDemoLog/log.txt
This script was executed at 14:7:0 on 2017-8-10
This script was executed at 14:8:8 on 2017-8-10
This script was executed at 14:19:1 on 2017-8-10
This script was executed at 14:20:1 on 2017-8-10
This script was executed at 14:21:1 on 2017-8-10
pi@raspberrypi:~ $ ▮
```

That in mind I think you saw that the cron scheduler is really simple and mighty. You can run any script you want at specific times and dates. This gives you a whole lot of opportunities.

:raised_hands:

## 11. Speech recognition interaction

...

## 12. Work with the GPIO pins

...

### Example with a LED

...

### Example with an LCD display

...

## Bonus: Manage users/groups

If you want to add a new user, remove a user or great groups for user this is also fairly simple:

### Add a new user

To add a new user you really just need one command and to be the root user (`sudo`-rights):

```text
pi@raspberrypi:~ $ sudo adduser newusername
```

*Important note: The new user name can not contain caps like `newUserName`.*

```text
pi@raspberrypi:~ $ sudo adduser newusername
Adding user `newusername' ...
Adding new group `newusername' (1003) ...
Adding new user `newusername' (1002) with group `newusername' ...
Crating home directory `/home/newusername' ...
Copying files from `/etc/skel' ...
Enter new UNIX password: ▮
```

Now enter two times a new password for the new account:

```text
Retype new UNIX password: ▮
```

And now you can add specific information about the user or just press ENTER for the default value:

```text
passwd: password updated successfully
Changing the user information for the newusernam
Enter the new value, or press ENTER for the default
        Full Name []: New User Name▮
```

```text
        Room Number []: ▮
```

```text
        Work Phone []: ▮
```

```text
        Home Phone []: ▮
```

If you are ready and everything is correct confirm by pressing `y` or deny by pressing `n` (and ENTER):

```text
Is the information correct? [Y/n] ▮
```

### Change the password of a user as sudo user

Probably you are not like me and forget the password of the new user after like ten seconds but hey, here you go:

```text
pi@raspberrypi:~ $ sudo passwd newusername
Enter new UNIX password: ▮
```

```text
Retype new UNIX password: ▮
```

```text
passwd: password updated successfully
pi@raspberrypi:~ $ ▮
```

### Change permissions of users to files

With Linux groups you can simple manage many user at once.

For example you can set permissions for some folders for every guest account at the same time.

This works because of in Linux every user has a unique user ID (UID) and a group ID (GID).

Source: [yolinux](http://www.yolinux.com/TUTORIALS/LinuxTutorialManagingGroups.html)

Therefore, if you remember 6. > Commands > File system > `ls`,  the file system looks like this:

```text
pi@raspberrypi:~ $ ls -l
total 36
drwxr-xr-x 2 pi pi 4096 Aug  1 14:59 Desktop
drwxr-xr-x 2 pi pi 4096 Aug  1 18:25 Documents
...
```

In which the first `pi` is the owner and the second one is the `group` where this file belongs to (remember that files stand in this case for directories `d` and *normal* files `-`, ...).

More important are the three octets (`rwx`, `r-x`, `r-x`) at the begin of each file in this view:

- The first octet are the permissions of the file owner > the first `pi`
- The second octet are the permissions of the group where the file belongs to > the second `pi`
- The last octet are the permissions for everyone else

You can with this very easy manage permissions to files for many users.

**How easy is it in real life?**

```text
pi@raspberrypi:~ $ mkdir Documents/Example
pi@raspberrypi:~ $ cd Documents/Example
pi@raspberrypi:~/Documents/ExampleDir $ touch example_file
pi@raspberrypi:~/Documents/ExampleDir $ ls -l
total 0
-rw-r--r-- 1 pi pi 0 Aug 12 14:03 example_file
pi@raspberrypi:~/Documents/ExampleDir $ ▮
```

Now we can use the command `chmod` with `u` (user) or `g` (group) or `o` (other) (or a combination of them) `+` or `-` and a combination of `r`, `w` and `x` (only one of every character).

For example I as an owner want to have the right to `r` - read, `w` write and `x` execute this file (I know this doesn't make so much sense - if it was a directory this would have more sense).

To get the rights one command is all I need:

```text
pi@raspberrypi:~/Documents/ExampleDir $ chmod u+x example_file
pi@raspberrypi:~/Documents/ExampleDir $ ls -l
total 0
-rwxr--r-- 1 pi pi 0 Aug 12 14:03 example_file
pi@raspberrypi:~/Documents/ExampleDir $ ▮
```

And because this is a secret file nobody should be able to read it besides me:

```text
pi@raspberrypi:~/Documents/ExampleDir $ chmod go-r example_file
pi@raspberrypi:~/Documents/ExampleDir $ ls -l
total 0
-rwx------ 1 pi pi 0 Aug 12 14:03 example_file
pi@raspberrypi:~/Documents/ExampleDir $ ▮
```

Now I recognized that my file isn't that secret and that even others should be able to read and edit it:

```text
pi@raspberrypi:~/Documents/ExampleDir $ chmod go+rw example_file
pi@raspberrypi:~/Documents/ExampleDir $ ls -l
total 0
-rwxrw-rw- 1 pi pi 0 Aug 12 14:03 example_file
pi@raspberrypi:~/Documents/ExampleDir $ ▮
```

See - very simple, even over the console.

### Add groups and add user to groups

Now we just need to know how we can add users to groups and heck even create them in the first place

#### Add a group

Create a user group:

```text
sudo addgroup <groupname>
```

Yay. That was it. Ready. Go on.

Example:

```text
pi@raspberrypi:~ $ sudo addgroup newgroup
Adding group `newgroup' (GID 1004) ...
Done.
pi@raspberrypi:~ $ ▮
```

#### Add user to a group

To add an user to a group isn't such difficult as you think once you read the manual page of `usermod`:

Just add the command options `-a` for append and `-G` for group and you're set:

```text
sudo usermod -a -G <groupname> <username>
```

Example:

```text
pi@raspberrypi:~ $ sudo usermod -a -G newgroup newusername
pi@raspberrypi:~ $ ▮
```

#### View all the users in a group

Wit the following command you will get a list off all the users in a group:

```text
pi@raspberrypi:~ $ grep <groupname> /etc/group
```

That means for our example:

```text
pi@raspberrypi:~ $ grep newgroup /etc/group
newgroup:x:1004:newusername
pi@raspberrypi:~ $ ▮
```

---

Too view all groups on your system you can also use the command `getnet group`

With the command `grep` (**g**lobally search a **r**egular **e**xpression and **p**rint - [wikipedia](https://en.wikipedia.org/wiki/Grep)) you can search this list and output only the lines where the following string is contained.

Through this you can use also the command `getent group | grep <groupname>` to get all users of a group:

```text
pi@raspberrypi:~ $ getent group | grep newgroup
newgroup:x:1004:newusername
pi@raspberrypi:~ $ ▮
```

---

### Remove user and groups

Ok, now I have 20 users and 5 groups, but I think I can delete some of them:

#### Remove a user

(Source: [cyberciti](https://www.cyberciti.biz/faq/linux-remove-user-command/))

Very simple: `userdel` + `-r` +  `<username>`

This will not only remove the user but also delete it's local home directory (`-r`).

So let's delete our user `newusername`:

```text
pi@raspberrypi:~ $ sudo userdel -r newusername
userdel: newusername mail spool (/var/mail/newusername) not found
pi@raspberrypi:~ $ grep newgroup /etc/group
newgroup:x:1004:
pi@raspberrypi:~ $ ▮
```

##### Lock the account before you finally delete it

If you don't want to delete the account, only lock them (for some time or as a test if the account is still be used) use these commands.

```text
pi@raspberrypi:~ $ sudo passwd -l <username>
```

Instead of instantly locking the account you can set a specific time when the account will be locked:

```text
pi@raspberrypi:~ $ sudo usermod --expiredate 1 <username>
```

(Number in this format: `YYYY-MM-DD`)

If an account is locked the user will get a message at login that the account expired and he should search for the admin.

#### Remove a group

Probably this is no surprise but the command to remove groups is `delgroup`:

So now we have an empty example group.
Let's remove it too:

```text
pi@raspberrypi:~ $ sudo groupdel newgroup
pi@raspberrypi:~ $ grep newgroup /etc/group
pi@raspberrypi:~ $ ▮
```

So you now can also manage users on any Linux system via command line. Nice.

## Bonus: Get free/used storage

Probably you encountered the problem, that you don't know where storage is used and how much storage is used.

### General storage overview

```text
pi@raspberrypi:~ $ df
```

With this command you get the amount of available and used space on your Micro-SD card.

With the parameter: `-BM` or `-BG`, ... you can even change the block size (Megabyte, Gigabyte, ...):

```text
pi@raspberrypi:~ $ df -BG
```

### Current directory storage overview

#### All files on their own

You hopefully know that you get the data about all the files over the command:

```text
pi@raspberrypi:~ $ ls -al
```

#### All files together

To get the size of all files in your current directory use the command:

```text
pi@raspberrypi:~ $ du -sh
```

or if you want to know the size of another directory use this:

```text
pi@raspberrypi:~ $ du -sh Path/to/another/directory
```

## Bonus: Use Lazarus with IDE

Lazarus is a great programming language that I used some time back in school. It's somewhat like Delphi but just search the internet, if you are interested.

### Install IDE

Really easy. You just need this:

```text
pi@raspberrypi:~ $ sudo apt-get update && sudo apt-get upgrade
pi@raspberrypi:~ $ sudo apt-get install fpc
pi@raspberrypi:~ $ sudo apt-get install lazarus
```

After that start it over the start menu or over the command `startlazarus`.

## Bonus: Mount external drive (with the console)

This isn't exactly that simple like you're used to...

---

Attention: If you use the GUI and just want to copy data you don't need this!

Raspbian automatically detects new USB drives and mounts them if you follow the dialog.

If not or you want to use the console follow this tutorial:

---

Let's put in our USB-Drive and check if it blinks.

If it does blink:

### Find out if it is "mounted"

Therefore use this command:

```text
pi@raspberrypi:~ $ dmesg | tail -n 20
```

`dmesg` will print the kernel ring buffer... and with `tail` we take us the last 10 lines of this buffer. Or better with `-n 20` we take the last twenty lines of the buffer:

```text
...
[984210.277928] usb 1-1.2: new high-speed USB device number 4 using dwc_otg
[984210.408873] usb 1-1.2: New USB device found, idVendor=8644, idProduct=8003
[984210.408887] usb 1-1.2: New USB device strings: Mfr=1, Product=2, SerialNumber=3
[984210.408896] usb 1-1.2: Product: USB Flash Disk
[984210.408903] usb 1-1.2: Manufacturer: General
[984210.408911] usb 1-1.2: SerialNumber: 02303500000002D1
[984210.409908] usb-storage 1-1.2:1.0: USB Mass Storage device detected
[984210.410700] scsi host0: usb-storage 1-1.2:1.0
[984211.478865] scsi 0:0:0:0: Direct-Access     General  USB Flash Disk   1.00 PQ: 0 ANSI: 2
[984211.480459] sd 0:0:0:0: [sda] 3913728 512-byte logical blocks: (2.00 GB/1.87 GiB)
[984211.480809] sd 0:0:0:0: [sda] Write Protect is off
[984211.480823] sd 0:0:0:0: [sda] Mode Sense: 03 00 00 00
[984211.481140] sd 0:0:0:0: [sda] No Caching mode page found
[984211.481151] sd 0:0:0:0: [sda] Assuming drive cache: write through
[984211.484964]  sda: sda1
[984211.490303] sd 0:0:0:0: [sda] Attached SCSI removable disk
[984211.506485] sd 0:0:0:0: Attached scsi generic sg0 type 0
```

So we see it's there, but we want to know the name of it.
Let's try this command:

```text
pi@raspberrypi:~ $ sudo fdisk -l
...
Device         Boot Start      End  Sectors  Size Id Type
/dev/mmcblk0p1       8192    93596    85405 41.7M  c W95 FAT32 (LBA)
/dev/mmcblk0p2      94208 62333951 62239744 29.7G 83 Linux

Disk /dev/sda: 1.9 GiB, 2003828736 bytes, 3913728 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0xd8fca99d

Device     Boot Start     End Sectors  Size Id Type
/dev/sda1  *      128 3913727 3913600  1.9G  e W95 FAT16 (LBA)
```

Now I can see that my 2GB USB stick with the name `/dev/sda1` seems to be mounted, but how do I get access to it's file system?

### Mount the external drive to the file system

To get access we need to mount the drive to the file system.

To do this we first decide where we wanna mount it.
I thought I take the empty `media` directory:

```text
pi@raspberrypi:~ $ cd ../../../media
pi@raspberrypi:/media $ ▮
```

There we create a directory - named however we want.
I went with `usb`:

```text
pi@raspberrypi:/media $ sudo mkdir usb
pi@raspberrypi:/media $ ▮
```

Now the first step get's it part.
We need to know the name of the USB device on the system.
In my case (you can read the logs) this is `/dev/sda1`.

Now all we have to do is:

```text
pi@raspberrypi:/media $ sudo mount /dev/sda1 usb
```

And we mounted the drive with the name `/dev/sda1` in the directory `usb`.

Just try it out and hit:

```text
pi@raspberrypi:/media $ ls -la usb
```
