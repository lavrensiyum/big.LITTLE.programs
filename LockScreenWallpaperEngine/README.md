
# LockScreenWallpaperEngine

<img src="lockscreenwallpaperengine.gif"/>

Bored of the default Windows Lock Screen? Well, with this script, you will be able to run Wallpaper Engine on the Lock Screen.

## Update Time!!
Now, the script working with Threads. No need to wait "listener.join()" to finish. Better then ever.

## How does is work

After enabling Windows Screen Saver, this script is checks the Lock Screen (WIN + L) and detect LogonUI.exe

```
62.      if(proc.name() == "LogonUI.exe"):
```

then, the script will call the "SC_SCREENSAVE" command.

```
21.      ctypes.windll.user32.PostMessageW(HWND_BROADCAST, WM_SYSCOMMAND, SC_SCREENSAVE, 0)
```

after that, the script adjust the screen brightness to 0 and if user break the screensaver, 

```
70.      with Listener(on_press=on_press) as listener:
71.         listener.join()
```

the script set the default screen brightness back.

```
72.      brightness_control(main_brightness)
```

## Setup and Run

First of all, open the WallpaperEngine, drag the mouse cursor to the "Installed" box at the top left and click on "Configure Screensaver".

Select what you want and click on "Settings and Preview" at the top left. Select the screensaver as "Wallpaper Engine" and the timeout as you want. Click Apply and close the window.

Now we come to script part.

I recommend to install requirements libs in the default python. To this, open cmd and install this libraries:

```
$ pip install psutil, pyuac, ctypes, screen_brightness_control, pynput
```

after that, check the link bellow

```
https://www.jcchouinard.com/python-automation-using-task-scheduler/
```

and create a task like this,

```
Triggers: 
    trigger: When logged in
Action:
    action: Start a program
    program/script: C:\where\program\is\run.pyw
General:
    security options: Run with highest privileges (check label)
                      Run only when user is logged on
```

and thats it. After that, when you log into your Windows account, Windows Task Scheduler will run the script. You don't even need to start the script every time.

For the test, lock your Windows account (WIN + L) and wait 5 second. The script will run WallpaperEngine and adjust brightness to 0. After that, press something on the keyboard or shake the mouse and exit screensaver. Now the script will set brightness back to default.

To disable the script, simply open Windows Task Scheduler and set disable the task what you named. To stop temporary the task, open Task Manager and terminate "Python", "Python (32 bit).