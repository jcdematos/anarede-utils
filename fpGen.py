"""
PROGRAM NAME - fpGen
PROGRAMMER - J. Matos, 06-2021
DATE - 21/06/2021
BUGS -
DESCRIPTION - Cria casos de fluxo de potência continuado com diferentes fatores
			  de crescimento.
"""
from functions import *
import random
import time
from random import seed

random.seed(time.time())

def findDINC(fLines):
	""" Recebe linhas do arquivo de interesse e retorna o index da linha onde
	define-se o crescimento da potência ativa e reativa. """
	for entrie in range(0, len(fLines)):
		line = fLines[entrie]
		if (line.startswith("DINC")):
			while True:
				entrie+=1
				line = fLines[entrie]
				if (line.startswith("(")):
					continue
				elif (line.startswith("99999")):
					break;
				return entrie

def genCPFLOW(fLines, nLinha):
	""" Generates a new growth factor and returns a new list of lines using that
	growth factor and the growth power factor"""
	# Make it possible to limit by an uppper and lower bound
	p = '{:<05}'.format(random.randrange(0,100)/1000)
	q = '{:<05}'.format(random.randrange(0,100)/1000)
	newGrowth = p + " " + q + "\n"
	fLines[nLinha] = fLines[nLinha][0:52]+newGrowth
	# potencia aparente
	s=(float(p)*2+float(q)**2)**(1/2)
	# fator de potencia
	if float(q) != 0:
		fp = '{0:.03}'.format(float(p)/s)
	else:
		fp = '{0:.03}'.format(1.0)
	print('p ' + p + " q " + q + " fp " + fp)
	return [fLines, fp.replace(".", "")]

def saveCPFLOWpwf(fLines, fp, workPath):
	""" Get the file and the new growth factor and save in the work path inside
	a new folder """
	fileFolder =workPath+"/cpflow_"+fp
	if Path(fileFolder).exists():
		return False
	Path(fileFolder).mkdir()
	filePath = fileFolder+"/cpflow_"+fp+".pwf"

	file = open(filePath, "w")
	file.writelines(fLines)
	file.close()
	return True

def runCPFLOW(folder):
	""" Runs cpflow, folder must be Path() """
	number = str(folder.name)[7:]
	file = str(folder)+"\\cpflow_"+number+".pwf"
	print(file)
	runAnarede(file)

def generateCPFLOW(file, pathWork, n):
	file = openFile(file)
	fLines = readFile(file)
	nLinha = findDINC(fLines)
	contador = 0
	while contador < n:
		[newfLines, newFP] = genCPFLOW(fLines, nLinha)
		if saveCPFLOWpwf(newfLines, newFP, pathWork):
			contador+=1
