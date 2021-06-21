import sys
import os
import subprocess
from pathlib import Path

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

def anaredePath(config="anaredePath.config"):
	""" Open config file and get anarede path """
	path = readFile(config)[0].strip("\n")
	if os.path.exists(path):
		return path
	print("Path doesnt exists")
	return False

def workPath(file):
	fileStart = file.rfind("/")
	return file[0:fileStart]

def cleanHeader():
	""" Function to clear the headers created by anarede """
	pass

def runAnarede(file):
	""" Runs anarede with the given file """
	return subprocess.run(["anarede", file], stdout=subprocess.PIPE, text=True)

def moveFiles(anaPath, workPath, filesList, mkdir=False, dirName="tempDir"):
	""" Move files from anarede work dir to the desired work dir """
	anaPath = anaPath
	workPath = workPath
	for file in filesList:
		scr = anaPath+"/"+file
		dst = workPath+"/"+file
		if os.path.exists(dst): # Delete file if already exists
			Path(dst).unlink(True)
		Path(scr).rename(dst)
