# RaspiForBeginners

In this repository I'll wanted to document (now also with other cool people :raised_hands:) everything I do with my *new* Raspberry Pi 3 just for fun and education.

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
B1 Console              (boot OS in console only without GUI)
B2 Console Autologin    (boot OS in console and automatically be logged in)
B3 Desktop              (boot OS with a GUI)
B4 Desktop Autologin    (boot OS with a GUI and automatically be logged in)
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

### XRDP (Works fine with Windows)

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

Voilà, there you have your Raspberry Pi desktop on your Windows computer.

### XRDP method for Android

You can even remotely control your Pi via your ANDROID device:

It's a bit messy, but here are the things you need to do:

1. Install a virtual keyboard, because the android app can't handle essential inputs like `-`.
   * `sudo apt-get update` - update the repositories
   * `sudo apt-get upgrade` - upgrade the whole system (optional)
   * `sudo apt-get install matchbox-keyboard` - install the virtual  matchbox-keyboard keyboard
   * `sudo reboot` - a reboot isn't really necessary but just do it quickly
2. You can now start it over the terminal with the command `matchbox-keyboard`
3. Download and install the android app [RDP Remote Desktop aFreeRDP](https://play.google.com/store/apps/details?id=com.freerdp.afreerdp&hl=en) 
4. Set everything up
   * start the app and click the plus symbol in the top bar (*add*)
   * now enter under `Label` how you want to name the connection
   * for `Host` the IP address of the Pi
   * for `Credentials` click it and enter your username and password
   * now go to times back (press two times the back button) and save your changes
5. Enjoy your ANDROID remote control
   * click the new created connection and go straight to the desktop of your Pi on your ANDROID device
   * if you know want to execute commands just type in `match` + `Tab` and `enter` and you can input symbol's like `-` over the virtual console



Also because we set as automatic start of the Pi a GUI-start we now always login to the GUI of the Pi when we log ourselves in over a remote desktop connection without needing the raspberry connect to any cables but the power chord (and eventually your network cable if you do not have WLAN).

## SSH connection (SFTP with Windows)

Because of the Secure Shell protocol you can do even more cool things.

One of them is to remotely control the whole file system of your Raspberry Pi from for example your WINDOWS computer over a program named FileZilla.

What do you need to do that you can do this?

First you need to activate SSH on your Raspberry Pi.

* over the GUI: `Preferences` >> `Raspberry Pi Configuration`
* or the CLI: `sudo raspi-config` >> `5 Interfacing Options` >> `P2 SSH` >> `Enable`

Now you can switch to your WINDOWS computer and download/install FileZilla from [filezilla-project.org](https://filezilla-project.org/).

When you installed it launch it. 

* Then click in the upper left `File` >> `Site manager`
* Now create a new site with clicking the button `New Site`
* On the right click the tab `General`
* Now enter in the `Host:` text field the IP address of your Pi (`hostname -I`).
* Choose as `protocol` the Secure File Transfer Protocol (`SFTP`)
* The `Logon Type:` is `Normal`
* Now enter your Pi username (`pi`)
* and your **long, secure & unique password**

And you are ready to go. Just click `Connect` at the bottom left and you can see in the main window of FileZilla in the right file hierarchy the file system of your pi. Also you can copy, move, edit files from there.

[source](https://www.raspberrypi.org/documentation/remote-access/ssh/sftp.md)


# 6. Welcome to the console :)

## Introduction

The CLI (command line interface) is in contrast to the GUI (graphical user interface) solely text based.

This brings the advantage of printing out with very few commands small things like "Hello world!" to controlling and monitoring with some other commands a big server.

In addition, support is simpler due to the uniqueness of the commands.

If this is all Greek to you ("oder du verstehst bisher nur Banhof") just keep reading - it's really simple:

## Start the console

If you booted in the CLI environment without starting the GUI (see 4.) you obviously are already in the console. And if you booted into the desktop GUI environment you can click the terminal icon on the top bar to start the console.

But there is a third way (if you booted with a GUI):
You can press `Ctrl` + `Alt` + `t` to start the console everywhere without even touching the mouse.

If you now also want to go full screen just press `Alt` + `Space` and then `x`.

And if you want to close the terminal again just press `Ctrl` + `Shift` + `q`.

## Shortcuts

Typing is is easy for you and with the arrow keys you already know how to get back and forth in the current command. So what can you possibly do better or faster you ask?... The answer is... a lot:

---

* `Ctrl` + `a` brings you in no-time to **the begin** of your current command
* `Ctrl` + `e` brings you in no-time to **the end** of your current command
* `Ctrl` + `x` + `x` moves your cursor between the begin and the end of your current command

---

- `Ctrl` + `b` move backward one character (same as `←`)
- `Ctrl` + `f` move forward one character (same as `→`)

---

* `Alt` + `b` move backward one word (or go to the start of the currently cursor pointed word)
* `Alt` + `f` move forward one word (or go to the end of the currently cursor pointed word)

---

* `Ctrl` + `k` *kills* or better deletes everything of the current command from the begin to the current cursor position
* `Ctrl` + `w` *kills* everything of the current command from the current cursor position to the end
* `Ctrl` + `u` *kills* everything of the current command after the position where your cursor is
* But all those shortcuts don't really kill or delete the text parts - they rather save them to a clipboard so that you can paste with the shortcut `Ctrl` + `y` these parts in your current command at your current cursor position

---

- `Ctrl` + `p` replaces your current command with your *previous* entered command (in entered history)
- `Ctrl` + `n` replaces your current command with your *next* entered command (in entered history)

---

- `Ctrl` + `c` stops/aborts the current running program in the console/terminal
- `Ctrl` + `d` stops every currently running program (closes the console in this case)
- `Ctrl` + `l` cleans the whole terminal

------

Also there is the holy grail the `Tab` key. It completes commands, filenames, etcetera...
If you press the `Tab` key again it will autocomplete to the next logical command, filename, etcetera...

## Commands

Here some simple but commands you should now or are helpful to know:

### Text output command ("Hello world")

---

#### `echo`

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

```
pi@raspberrypi:~ $ echo hello "world! now press enter
> hello world! in a new line :o and now \"enter again\"
> wow again a new line... now we want to end by typing a " and pressing enter
hello world! now press enter
hello world! in a new line :o and now "enter again"
wow again a new line... now we want to end by typing a  and pressing enter
pi@raspberrypi:~ $ ▮
```

### File system commands

---

#### `ls`

stands for *List directory contents* and lists the current content of the folder you are in.

Wait a second - we are in a folder?

That's right. The console is always in a specific directory which enables many possibilities you will later learn about. With this command you can list the contents of the current directory your console *is*.

Folders are in the case of the default Pi terminal blue and files white.

```
pi@raspberrypi:~ $ ls
Desktop Documents Downloads Music Pictures Public python_games Templates Videos
pi@raspberrypi:~ $ ▮
```

But there are more things like only commands on LINUX:
There are also command options.

In the case of a directory listener you probably also want to know the size, date, and more:

`-l` → long listing - get a list with size and date of creation and ...

```
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

Explanation: ([used source](https://linuxconfig.org/understanding-of-ls-command-with-a-long-listing-format-output-with-permission-bits))

* `d` stands for directory - `l` for a link - `c` for a character file
* `rwxr-xr-x` are the permissions applied to this *file* also called octets

  * the firs octet defines the permission for the file owner `rwx`
  * the second octet defines the permissions defined for the group `r-x`
  * the third and last part defines the permissions for everyone else `r-x`

    * The permissions are the following

       | `r`  | `w`   | `x`     |
       | ---- | ----- | ------- |
       | read | write | execute |

* `2` number of linked hard-links (links to that file/directory)
* `pi` the owner of the file/directory
* `pi` the group which this file/directory belongs to
* `4096` size of the file/directory
* `Aug  1 14:59` modification/creation date and time
* `Desktop` the file/directory name

`-a` → shows not only the *normal* files, but also the *hidden* ones that start with a `.`
(because in LINUX everything (file,folder,device,command) is a file, a file that starts with `a` is a hidden file)

```
pi@raspberrypi:~ $ ls -a
.             .cache  Documents       .idlerc    .pki         .themes     .WolframEngine
..            .config Downloads       .local     .profile     .thumbnails .Xauthority
.bash_history .dbus   .gconf          .minecraft Public       Videos      .xsession-errors
.bash_logout  Desktop .gstreamer-0.10 Music      python_games .vnc        .xsession-errors.old
.bashrc       .dmrc   .gtkrc-2.0      Pictures   Templates    .Wofram
pi@raspberrypi:~ $ ▮
```

the cool thing with the command options are that you can just combine them in one simple command like:

```
pi@raspberrypi:~ $ ls -la
total 144
drwxr-xr-x 25 pi   pi   4096 Aug  4 14:46 .
drwxr-xr-x  3 root root 4096 Jul  5 12:41 ..
-rw-------  1 pi   pi   2162 Aug  4 01:26 .bashhistory
[too much unimportants code - I stop here]
pi@raspberrypi:~ $ ▮
```

---

Okay. So now we can find files in our current directory but can we probably also go into other directories?

Not a problem my friend:

---

#### `cd`

stands for *change directory* and will do the magic

You just type in `cd` and after that your path - the directory you wanna go. In this case we want straight to the documents folder:

```
pi@raspberrypi:~ $ cd Documents
pi@raspberrypi:~/Documents $ ▮
```

WOW. Did you just see that?
Wait a second, one more tip:

```
pi@raspberrypi:~/Documents $ cd ~
pi@raspberrypi:~ $ ▮
```

The thing after `username@hostname:` is the path where your console/terminal currently *is*. :open_mouth:

The odd `~` is the sign for your home directory. If you changed your directory so much, that you lost yourself just enter `cd ~` and you are back home.

But there are more tricks:

With `cd ..` you go one folder upwards

```
pi@raspberrypi:~ $ cd Desktop
pi@raspberrypi:~/Desktop $ cs ..
pi@raspberrypi:~ $ ▮
```

### Create/Edit/Delete/View files

Next we probably want to create files (that means folders and files):

------

#### `mkdir`

stands for *Make directory* and creates a directory with the name you write after it

```
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
3. If you come from a WINDOWS computer you probably wondered why there was no error prompt after I created first the folder `cool folder` and then `Cool folder` without any kind of error prompt. That is because of LINUX. The file system is in contrast to WINDOWS - if you put it simply - not case sensitive. You can create files and folders with the same name as long as there is a difference in large or lower case. On WINDOWS computers you can't do this. Every file in a directory there can only have a unique name.
4. Wait a second, I want also to create files :disappointed:...

------

#### `touch`

creates a file with the name you write after it :smiley:

```
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

```
pi@raspberrypi:~ $ mkdir Desktop/another_cool_directory
pi@raspberrypi:~ $ touch Desktop/another_cool_directory/hi
pi@raspberrypi:~ $ cd Desktop/another_cool_directory/
pi@raspberrypi:~Desktop/another_cool_directory $ ls
hi
pi@raspberrypi:~Desktop/another_cool_directory $ ▮
```

Another additional tip:
If you - although the path is already in the console - want the whole path of the directory your currently at just enter `pwd`:

```
pi@raspberrypi:~Desktop/another_cool_directory $ pwd
/home/pi/Desktop/another_cool_directory
pi@raspberrypi:~Desktop/another_cool_directory $ ▮
```

---

Two things to go: Deleting files and viewing/editing them

Of course you could install programs that can do these things so much better (for example an advanced text editor like Vim), but for now we'll use the `nano` terminal editor, because it is already installed.

---

#### `nano`

is a simple text editor

```
pi@raspberrypi:~ $ nano
```

If you enter this command in the terminal will start a new CLI where you can write text like in a normal text editor.. just you are still in the terminal.

When you are finished just use the shortcut `Ctrl` + `x`. Now (if you wrote something) the editor asks if it should save the things you wrote. If you press `y` you now just need to type in a name for your file.

The cool thing is you can not only do much more with `nano` and creating files, you can also really simple edit existing files:

```
pi@raspberrypi:~ $ nano existing_file
```

This will open the existing file named existing_file and you can edit the content of it. Saving is the same just quit `nano` with `Ctrl` + `x` and press `y` now just don't change the name of the file and you edited successfully a file.

---

#### `cat`

enables you to quickly view the content of a text file directly in the editor

For example did I just edit the existing_file in my home directory like in the command before and wrote `Hello world!` . When you now input `cat existing_file` you will see the content directly in the console:

```
pi@raspberrypi:~ $ cat exisiting_file
Hello world!
pi@raspberrypi:~ $ ▮
```

But how can you delete all these very unimportant files you created in the last 10 minutes?

---

#### `rm`

like *remove*

Doesn't sound so difficult, doesn't it? Let's clean my desktop:

```
pi@raspberrypi:~/Desktop $ ls
another_cool_directory exisiting_file hi tut tut.txt
pi@raspberrypi:~/Desktop $ rm hi
pi@raspberrypi:~/Desktop $ rm tut.txt
pi@raspberrypi:~/Desktop $ ls
another_cool_directory exisiting_file tut
pi@raspberrypi:~/Desktop $ ▮
```

But if we try to remove a directory there is an error prompt... let's learn a new command:

---

#### `rmdir`

like *remove directory*

```
pi@raspberrypi:~/Desktop $ ls
another_cool_directory exisiting_file tut
pi@raspberrypi:~/Desktop $ rm another_cool_directory
rm: cannot remove 'another_cool_directory': Is a directory
pi@raspberrypi:~/Desktop $ rmdir another_cool_directory
rmdir: cannot remove 'another_cool_directory': Directory is not empty
pi@raspberrypi:~/Desktop $ ▮
```

Okay. It seems like you only can delete empty directories. But of course we have a command for deleting also a not empty directory:

```
pi@raspberrypi:~/Desktop $ rm -rf another_cool_directory
pi@raspberrypi:~/Desktop $ ls
exisiting_file tut
pi@raspberrypi:~/Desktop $ mkdir new_empty_directory
pi@raspberrypi:~/Desktop $ ls
exisiting_file new_empty_directory tut
pi@raspberrypi:~/Desktop $ rmdir new_empty_directory
pi@raspberrypi:~/Desktop $ ls
exisiting_file tut
pi@raspberrypi:~/Desktop $ ▮
```

Damn. You're really fast. Some cool and helpful things before we go on with next steps:

### Find out more about commands

Another essential command is

------

#### `man`

like *manual*

Type this command and after it the command you want to know more about (be it what does it, what are the command options, etcetera...).

For example I want to know more about the command `ls`:

```
pi@raspberrypi:~ $ man ls
```

Then in the console/terminal a manual which you can scroll through opens that contains all the information about the command `ls`. With pressing `q` you can leave the manual and are right back in the console/terminal. This works with every command.

### Command history tricks

---

#### `history`

shows all the executed commands (very long! - my example is small)

```
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

#### `!!`

runs the last executed command

```
pi@raspberrypi:~ $ echo hello world!
hello world!
pi@raspberrypi:~ $ !!
echo hello world!
hello world!
pi@raspberrypi:~ $ ▮
```

### Learn more commands and shortcuts

If you want to learn more shortcuts and commands (and believe us, there are so many) just search on the web. There are many sites (like our sources) that list cool commands and in the comments you will find more and more. The learning curve is very steep.

---

*Source of many shortcuts and many that we didn't told about: [skorks](https://www.skorks.com/2009/09/bash-shortcuts-for-maximum-productivity/)*
*Source of many commands and many that we didn't told about: [tecmint](https://www.tecmint.com/useful-linux-commands-for-newbies/)*


# 7. Install additional software/programs

Installing programs is on LINUX or rather on Raspbian quite different if you come from OSX or WINDOWS.

Therefore here a quick and dirty explanation of operating systems and especially LINUX:

## The operating system

### The kernel

The kernel is the core computer program. It has the full control over everything of the system and is the first thing that gets started on a computer start-up.

It handles all connected peripherals, input, output and thus controlling on what other programs having access to.

Systems like WINDOWS and LINUX have an underlying kernel.

Nevertheless there are big differences between especially these two besides that LINUX is an open source developed and public viewable kernel and the WINDOWS kernel is a cooperation secret.

### LINUX distributions and WINDOWS

Probably you know LINUX distributions better under the names Arch Linux, Debian, Fedora, Gentoo, Manjaro, Mint, Ubuntu, Raspbian, etcetera.

These so named *distributions* don't have specific kernels. They all have the same kernel, the LINUX kernel. \*

But only the kernel won't bring you far. Every system is only so useful as the programs that are installed on it. Like.. what would WINDOWS be if you wouldn't have a GUI.

And because there are so many possible GUI's and file managers, file editors and network programs and even more programs that some people created distributions. They all consist of the LINUX kernel and many chosen programs/packages.

You can think of WINDOWS like the only distribution of the WINDOWS kernel.

The cool thing about this on LINUX distributions is that you can theoretically install every LINUX program on every LINUX distribution, this means also every GUI and so on.

\* there are ways to strip a kernel down in size but they are nevertheless all based on one LINUX kernel

## How to install these... packages?!

It's quite simple how to install packages onto your Raspberry Pi running Raspbian:

Just type into the console `apt-get install` and enter to install the software:

```
pi@raspberrypi:~ $ sudo apt-get install <name of the software>
```

Why does this work?
Every distribution has it's own repository where they all saved these packages that work well with their systems. By typing this you can download it and get the newest for your distribution available package of the software you want.

### Example: Lets install Firefox

Normally on WINDOWS you go to the Mozilla Firefox website go to the download page. Download the executable and run it. Then you wait till it's finished installing.

How's that on our Raspbian?

Funny thing I just found out: Firefox isn't listed in the console under it's real name (because it still supports flash which requires an *x86* processor but the raspberry pi has an 64 bit *ARM* processor) but under the name **Iceweasel**. So let's cut to the chase:

```
pi@raspberrypi:~ $ sudo apt-get install iceweasel
.... text
pi@raspberrypi:~ $ ▮
```

Okay.... did we install it now or what did we do?

If it only was easy to start Firefox now... Let's try something:

```
pi@raspberrypi:~ $ iceweasel
pi@raspberrypi:~ $ ▮
```

Probably Firefox just launched and now you know it's installed.

### Example: Lets install cowsay

To install this very important package just type in:

```
pi@raspberrypi:~ $ sudo apt-get install cowsay
```

After the installation you can now use this command:

```
pi@raspberrypi:~ $ cowsay Hi, I\'m a cow.
```

​And enjoy the result. :smiley: :cow:

## What can I do when a new version of my installed software gets released?

That is also quite cool. Remember when I wrote that every distribution has it's own repository with all the  latest packages of every program you install over the package manager `apt`?

That's very handy because there is an command that compares all the versions and the kernel on your Raspberry Pi with the ones in the repository and updates the things that aren't latest on your Pi.

You therefore need to know two commands:

1. Update/Compare the local repositories with the latest repositories online

   ```
   pi@raspberrypi:~ $ sudo apt-get update
   ```

2. Download the new packages (if there are any new ones)

   ```
   pi@raspberrypi:~ $ sudo apt-get upgrade
   ```

When the command terminates all of your system software (kernel and over packages) should be the latest of your current distribution.

# 8. Program on it

## Batch

First let's create a bash script file:

```
pi@raspberrypi:~ $ nano
```

Then we just write a simple bash script in `nano`:

```
#!/bin/bash
# A example Bash script file comment
echo WOW You just executed a Bash script :o
```

Then we save this by clicking `Ctrl` + `x` and `y` and entering the name `bash_test_script.sh` .

Now we can execute it:

```
pi@raspberrypi:~ $ bash bash_test_script.sh
WOW You just executed a Bash script :o
pi@raspberrypi:~ $ ▮
```

## Python

First let's create a python script file:

```
pi@raspberrypi:~ $ nano
```

Then we just write a simple python script in `nano`:

```python
print("WOW You just executed a Python script :o")
```

Then we save this by clicking `Ctrl` + `x` and `y` and entering the name `python_test_script.py` .

Now we can execute it:

```
pi@raspberrypi:~ $ python_test_script.py
WOW You just executed a Python script :o
pi@raspberrypi:~ $ ▮
```

---

But when we speak about python we have even more possibilities on the Pi.

If you enter `python` in the console you enter a live python editor where you can program live:

```
pi@raspberrypi:~ $ python
Python 2.7.9 (default, Sep 17 2016, 20:26:04)
[GCC 4.9.2] on linux2
Type "help", "copyright", "credits" or "license" for more inforamtion.
>>> ▮
```

Now we can do fun stuff in the terminal (everything we want to do):

```
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

You even have one more option - to program on the preinstalled python 3 console IDE.

To start it you can search and click the IDE icon **or**...

...we use the glorious mighty console:

````
pi@raspberrypi:~ $ idle3
````

Of course you can also open with this command directly any preexisting file like the one we just created:

```
pi@raspberrypi:~ $ idle3 python_test_script.py
```


# 9. Set up a local webserver

## A *normal* webserver (Apache)

First we install Apache:

```
pi@raspberrypi:~ $ sudo apt-get install apache2 -y
```

By default there will be an instant *normal* web server created (on your local network).

You can get it anywhere on your local network by typing in your current IP address (`hostname -I`) or local also under `localhost` into the browser search bar.

If you probably also want to change the content of your local server just got to the directory `/var/www/html/` and edit for example the file `index.html` which will be displayed if someone enters the IP address of your Pi.

[source](https://www.raspberrypi.org/documentation/remote-access/web-server/apache.md)

For example:

```
pi@raspberrypi:~ $ sudo rm /var/www/html/index.html
pi@raspberrypi:~ $ sudo touch /var/www/html/index.html
pi@raspberrypi:~ $ sudo nano /var/www/html/index.html
```

Then edit in `nano` the file `index.html` to the content `Hello world!<br>This is HTML`.

After saving this you should instantly by searching for the IP address of the Pi see these words on the website.

### Enable SFTP in html directory (`chmod`)

If you use SFTP you probably noticed that FileZilla blocks uploads. With the following commands...

```
pi@raspberrypi:~ $ cd /var/www/
pi@raspberrypi:~/var/www $ chmod a+w html
pi@raspberrypi:~/var/www $ chmod a+w html/index.html
pi@raspberrypi:~/var/www $ ▮
```

...you give everyone writing rights in this folder and now everything should work with FileZilla.

If you want to know more about `chmod ` look here: [source](http://www.dummies.com/computers/raspberry-pi/working-with-file-permissions-on-your-raspberry-pi/)

## PHP server

When we want to use PHP there isn't much more we need to do.

Let's start by installing PHP5 and the Apache PHP5 module via the package manager:

```
pi@raspberrypi:~ $ sudo apt-get install php5
pi@raspberrypi:~ $ sudo apt-get install libapache2-mod-php5 -y
```

Because we used the Apache module the same directory as before will be used. But now also `.php` files can be shared via local network.

[source](https://www.raspberrypi.org/documentation/remote-access/web-server/apache.md)

For example:

```
pi@raspberrypi:~ $ sudo rm /var/www/html/index.html
pi@raspberrypi:~ $ sudo touch /var/www/html/index.php
pi@raspberrypi:~ $ sudo nano /var/www/html/index.php
```

Then edit in `nano` the file to the content `<?php echo "hello world"; echo date('Y-m-d H:i:s'); ?>`.

...

***Didn't work - I probably need to set up the Pi again.***

...

## SQL server

...

***Didn't work - I probably need to set up the Pi again.***

...

## SFTP server

... native windows implementation


# 10. Automated tasks scheduler (`cron `)

https://www.raspberrypi.org/documentation/linux/usage/cron.md

...


# 11. Speech recognition interaction

...


# 12. Work with the GPIO pins

...

## Example with a LED

...

## Example with an LCD display

...