# dictionary_service_daemon
This is dictionary service which runs in the background and shows the meaning on press of key 'q'.

[![loader](https://github.com/Gaurav200893/dictionary_service_daemon/blob/master/tkinter_dictionary.png)](#features)

## Requirements
> pip3 install pydictionary

> pyxhook (already included)

## Configuration
#### you need to use upstart in Ubuntu to make it work

> go to etc/init

> create a configuration file tkinter_dict.conf (which is already included in this project). Make sure this line: exec python3 /home/youruser/dictionary_service_daemon/get_meanings.py>> /var/log/tkinter_dict.log 2>&1 is correct.

> make sure the folder path in tkinter_dict.conf for python file correct. Keep this project folder in home/youruser/this project

> make changes in get_meanings.py os.environ.setdefault('XAUTHORITY', '/home/youruser/.Xauthority') set this correctly.

> change this line log_file='/home/webwerks/dictionary_service_daemon/file.log' to log_file='/home/youruser/dictionary_service_daemon/file.log'

## How to run

> To run this service type in terminal: sudo service tkinter_dict start

> To stop type this: sudo service tkinter_dict stop

## How to get meanings

> Copy the word 

> Now press the button "Q". You will see the window in few seconds.

#### Remember this service will restart automatically if you start your system again.

### The Pressing of "Q" is really annoying ;)
