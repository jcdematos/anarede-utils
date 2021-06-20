
import sys
import os

import tkinter as tk
from tkinter import filedialog

def openFile(sys, file="none"):
	""" Abri arquivo a ser usado, dado por argumento ou dialog box """
	if file == "none":
		if len(sys.argv) > 1:
			for argument in (sys.argv):
				if argument == '-o':
					# open file from string passed
					pass
		else:
			root = tk.Tk()
			root.withdraw()
			file = filedialog.askopenfilename()
	return file

def readFile(file):
	""" Reads a file and returns a list of lines """
	with open(file, 'r') as dados:
		lines = dados.readlines();
	return lines
