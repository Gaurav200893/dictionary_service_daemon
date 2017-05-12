#!/usr/bin/python

# set env vars for x lib
import os
# environnement vars
os.environ.setdefault('XAUTHORITY', '/home/webwerks/.Xauthority')
os.environ.setdefault('DISPLAY', ':0.0')

import time


import pyxhook
import tkinter_dict
#change this to your log file's path
log_file='/home/webwerks/dictionary_service_daemon/file.log'

#this function is called everytime a key is pressed.
def OnKeyPress(event):
  fob=open(log_file,'a')
  fob.write(event.Key)
  fob.write('\n')

  # print the button pressed
  #print(event.Ascii)
  # tkinter_dict.getSelectedMeanings()

  if event.Ascii==113: #113 for key 'q'
  	tkinter_dict.getSelectedMeanings()

  if event.Ascii==96: #96 is the ascii value of the grave key (`)
    fob.close()
    new_hook.cancel()
#instantiate HookManager class
new_hook=pyxhook.HookManager()
#listen to all keystrokes
new_hook.KeyDown=OnKeyPress
#hook the keyboard
new_hook.HookKeyboard()
#start the sessionfff
new_hook.start()