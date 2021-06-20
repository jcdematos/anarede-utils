"""
PROGRAM NAME - readPWF
PROGRAMMER - J. Matos, 06-2021
USAGE - Run the program and pick a PWF file using, give no argument to open a
		file dialog, or -o to give a string with the file path.
DATE - Started 14/06/2021
BUGS -
DESCRIPTION - Programa que le o pwf de um caso base do ANAREDE e remove dados
			  relevantes para analisar a estabilidade de tensão.
"""
import sys
import os
import re
import time
import subprocess
import pexpect

import tkinter as tk
from tkinter import filedialog

def anaredePath(config="anaredePath.config"):
	""" Open config file and get anarede path """
	path = readFile(config)[0]
	if os.path.exists(path):
		return path
	return False

def workPath(file):
	fileStart = file.rfind("/")
	return file[0:fileStart]

def openFile(sys, file):
	""" Abri arquivo a ser usado, dado por argumento ou dialog box """
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

def cleanHeads():
	""" Function to clear the headers created by anarede """
	pass

def readFile(file):
	contador = 0
	with open(file, 'r') as dados:
		lines = dados.readlines();
	print("Linhas lidas %s" % len(lines))
	return lines

def runAnarede(file):
	run = "start anarede -o \"" + file + "\""
	print(run)
	return os.system(run)

class Bar:
	""" Class to hold data for the bars """
	nBars = 0 # numbers of bars
	caseTitle = ""
	relPath = ""
	def __init__(type):
		self.type = type;

	def defineTitle(title):
		caseTitle = title

myBars = []
file = openFile(sys, "case.pwf")
print("Readin file : %s" % file)
#here get path of file as to create directory strutcture

start_time = time.time()
#------------------------------------------------------------------------------
fLines = readFile(file)
print("fLines has %s lines" % len(fLines))
#------------------------------------------------------------------------------
#for line in fLines:
stripElements = [" ", "\n"]
for entrie in range(0, len(fLines)):
	line = fLines[entrie]
	if (line.startswith("(")):
		continue # Ignore comment lines
	if (line.startswith("TITU")):
		Bar.caseTitle = fLines[entrie+1]
		# Later use rstrip to remove new line and spaces
		continue
	# First reading only DBAR and ULOG commands
	if (line.startswith("DBAR")):
		pass
	if (line.startswith("ULOG")):
		# Find rel and his file names
		if (fLines[entrie+2].rfind("rel") != -1):
			Bar.relPath = fLines[entrie+2]
			print(Bar.relPath)
		if (fLines[entrie+2].rfind("his") != -1):
			Bar.relPath = fLines[entrie+2]
			print(Bar.relPath)

print(Bar.caseTitle)
#    print(line, end="")
#------------------------------------------------------------------------------
print("--- %s seconds ---" % (time.time() - start_time))
#result = runAnarede(file)
result = subprocess.run(["anarede", file], stdout=subprocess.PIPE, text=True, input="Hello from the other side")
# the files created are being saved in anarede folder
if (result == 0):
	print(result)
