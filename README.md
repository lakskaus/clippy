# clippy
Tool for taking screenshots of partial area of screen on linux. Similar to Windows clipping tool.
Works for Ubuntu(Hopefully).

# Requirements.txt
Use 

``` pip install -r requirements.txt```

# Tkinter
Tkinter is usually installed with python on other platforms, but on some linux distributions it isn't always included and so you might run into an error when running it.

The following command should fix the issue:
```sudo apt-get install python3-tk```

# Adding it as a keyboard shortcut
On Ubuntu you can go to Settings > Keyboard > View and Customize Shortcuts > Custom Shortcuts > +

From there you add a name to your shortcut and then something like "python3 /path/to/the/pythn/script.py" into the command section. For example for someone named Rasputin it might be "python3 /home/rasputin/Desktop/PythonFiles/clip/clip.py".

Then insert which shortcut key combination you want to use. I use "shift + cmd(windows key) + s" because that is what Windows uses for its native clipping tool.
