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
import re
import time
import subprocess
from pathlib import Path
from functions import *
from readREL import *

def anaredePath(config="anaredePath.config"):
	""" Open config file and get anarede path """
	path = readFile(config)[0]
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

class Bar:
	""" Class to hold data for the bars """
	nBars = 0 # numbers of bars
	caseTitle = ""
	relPath = ""
	hisPath = ""
	files = [relPath, hisPath]
	def __init__(self, number, estado, tipo, grupoBase, nome, area):
		self.number = number.strip(" ")
		self.estado = estado.strip(" ")
		self.tipo = tipo.strip(" ")
		self.grupoBase = grupoBase.strip(" ")
		self.nome = nome.strip(" ")
		self.area = area.strip(" ")


	def addFluxPot(self, pg, qg, pl, ql):
		self.PG = pg.strip(" ")
		self.QG = qg.strip(" ")
		self.PL = pl.strip(" ")
		self.QL = ql.strip(" ")

	def printBar(self):
		print(self.number + self.estado + self.tipo + self.grupoBase + self.nome + self.area)
		print(self.PG + self.QG + self.PL + self.QL)

def printBars():
	print(Bar.caseTitle, end="")
	print(Bar.hisPath, end="")
	print(Bar.relPath, end="")

def readPWF():
	pass


myBars = []

def main():
	# Make directory structure
	file = openFile(sys)
	print("Reading file : %s" % file)
	pathAnarede = anaredePath()
	print("Anarede path is " + pathAnarede)
	pathWork = workPath(file)
	print("Working Directory path is " + pathWork)

	start_time = time.time()
	#------------------------------------------------------------------------------

	fLines = readFile(file)
	#------------------------------------------------------------------------------
	for entrie in range(0, len(fLines)):
		line = fLines[entrie]
		if (line.startswith("TITU")):
			# Salva nome do título do caso
			Bar.caseTitle = fLines[entrie+1].rstrip("\n")
			# Later use rstrip to remove new line and spaces
			continue
		if (line.startswith("DBAR")):
			# Get basic information from bars
			while True:
				entrie += 1
				line = fLines[entrie]
				if (line.startswith("99999")):
					break
				if (line.startswith("(")):
					continue
				else:
					Bar.nBars += 1
					number = line[0:5]
					estado = line[6]
					tipo = line[7]
					grupoBase = line[8:10]
					nome = line[10:22]
					area = line[73:76]
					myBars.append(Bar(number,estado,tipo,grupoBase,nome,area))
		if (line.startswith("ULOG")):
			if (fLines[entrie+2].rfind("rel") != -1):
				Bar.relPath = fLines[entrie+2].rstrip("\n")
			if (fLines[entrie+2].rfind("his") != -1):
				Bar.hisPath = fLines[entrie+2].rstrip("\n")

	#------------------------------------------------------------------------------
	#result = runAnarede(file)
	#files = [Bar.relPath, Bar.hisPath]
	#moveFiles(pathAnarede, pathWork, files)


	readREL(myBars, pathWork+"/"+Bar.relPath)

	print("Barras lidas")
	for bar in myBars:
		Bar.printBar(bar)
	print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
	main()
