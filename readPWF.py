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
import time
from functions import *
from readREL import *
from readPV import *

class Bar:
	""" Class to hold data for the bars """
	nBars = 0 # numbers of bars
	caseTitle = ""
	relPath = ""
	hisPath = ""
	loadMargin = ""
	criticalVoltage = ""
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

	def printBarMin(self):
		print(self.number +"|"+ self.estado +"|"+ self.tipo +"|"+ self.grupoBase +"|"+ self.nome +"|"+ self.area)
	def printBar(self):
		print(self.number +"|"+ self.estado +"|"+ self.tipo +"|"+ self.grupoBase +"|"+ self.nome +"|"+ self.area)
		print(self.PG+"|"+ self.QG +"|"+ self.PL +"|"+ self.QL)


def printBars():
	print(Bar.caseTitle)
	print(Bar.hisPath)
	print(Bar.relPath)

def readPWF(fLines, myBars):
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
	fLines = readFile(file)
	#------------------------------------------------------------------------------
	readPWF(fLines)

	#------------------------------------------------------------------------------
	result = runAnarede(file)
	files = [Bar.relPath, Bar.hisPath]
	moveFiles(pathAnarede, pathWork, files)


	filePV ="C:\\Users\\Julio Matos\\ownCloud\\tcc\\code\\anarede-utils\\pv.plt"
	readREL(myBars, pathWork+"/"+Bar.relPath)
	myPlots = readPV("V", myBars, filePV)

	voltages = []
	critical = 1
	for plot in myPlots:
		""" Gets the critical voltage and load margin of the system """
		if barraPQ(plot.barNumber, myBars):
			x, y = inflectionPoint(plot.xdata, plot.ydata)
			plot.addInflection(x, y)
			voltage = criticalVoltage(plot,myBars)
			if (voltage < critical):
				critical = voltage
				margin = loadMargin(plot, myBars)
			voltages.append(criticalVoltage(plot,myBars))
#			printPlot(plot, [plot.xi, plot.yi])

	Bar.criticalVoltage = critical
	Bar.loadMargin = margin
	print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
	main()
