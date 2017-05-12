#!/usr/bin/python

import __future__
import sys
import getch

from PyDictionary import PyDictionary

try:
	# for Python2
	from Tkinter import *   
except ImportError:
	# for Python3
	from tkinter import *

try:
	# python 2
	from tkFont import Font
except ImportError:
	# python 3
	from tkinter.font import Font


''' Code to get the user input (This might be redundent code for input)''' 

# detect python version at runtime
if sys.version_info.major<3:
	import thread as _thread
else:
	import _thread

import time


def appendAllMeanings(text_list):
	''' Append all meanings together '''

	appended_text = '';
	for values in text_list:
		if(appended_text!=''):
			appended_text += ";"
		appended_text = appended_text + values

	return appended_text

def getMeanings(text):
	''' Get the meanings from PyDictionary Library '''

	dictionary = PyDictionary(text)
	meanings = dictionary.getMeanings()
	return meanings

def main():
	'''
		Display with tkinter
	'''

	master = Tk()
	master.withdraw()


	clipboard_text = master.clipboard_get()
	meaning_text = getMeanings(clipboard_text)

	if meaning_text is not None or meaning_text!='':
		word_heading = ''
		word_meaning = ''
		i=1
		for words,elements in meaning_text.items():
			word_heading = str(words) + ":" +"\n"
			if elements is None:
				word_meaning = "No meaning(s) available."
				break
			for parts_of_speech, meaning in elements.items():
				meaning_text = appendAllMeanings(meaning)
				word_meaning +=  str(i)+". "+parts_of_speech +": \n"+ meaning_text + "\n\n"
				i+=1
	  
	# create frame for window
	dict_frame = Frame(master, relief=GROOVE, width=50, height=100, bd=1)
	dict_frame.place(x=10,y=10)

	# create scrollbar
	scrollbar = Scrollbar(master)
	scrollbar.pack(side=RIGHT, fill=Y)

	# create text box
	txt = Text(master, wrap=WORD,background="#e6ffff")
	txt.pack(expand=1, fill=BOTH)

	# create fonts
	myFont = Font(family="Times New Roman", size=12)
	txt.tag_configure("bold", font="wieght:bold")
	txt.configure(font=myFont)

	# insert text
	txt.insert(END, "\n")
	txt.insert(END, word_heading + "\n","bold")
	txt.insert(END, word_meaning + "\n")

	# configure text widget
	txt.configure(state=DISABLED)
	txt.config(yscrollcommand=scrollbar.set)

	# assign scrollbar
	scrollbar.config(command=txt.yview)

	# show the tkinter window
	master.deiconify()
	mainloop()





def getSelectedMeanings():
	''' begin main execution '''
	# print("Press Ctrl+H to get the meaning")
	# while True:
	# 	char = getch.getch()
	# 	key_char = ord(char)
	# 	# print(key_char)
	# 	if key_char==8:
	main()
