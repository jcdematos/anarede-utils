"""
PROGRAM NAME - readPV
PROGRAMMER - J. Matos, 06-2021
DATE - Started 22/06/2021
DESCRIPTION - Funções para ler um pv.plot, retornar os plots organizados em
			  barras, além de função para gerar a margem de carregamento e
			  tensão critica do sistema.
"""
import re
import matplotlib.pyplot as plt
import numpy as np
from functions import *

class Plot:
	""" Class to hold the data for each plot """
	def __init__(self, barNumber, xdata, ydata):
		self.barNumber = barNumber
		self.xdata = xdata
		self.ydata = ydata

	def addInflection(self, xi, yi):
		self.xi = xi
		self.yi = yi

def typeByNumber(number, myBars):
	""" type of the bar by its number """
	for bar in myBars:
		if bar.number == number:
			return bar.tipo

def barraPQ(number, myBars):
	""" Finds if a bar is PQ or not """
	if typeByNumber(number, myBars) == "":
		return True
	if typeByNumber(number, myBars) == "0":
		return True
	return False

def readPV(variable, myBars, file="none"):
	""" Le um arquivo pv.plot and returns as a list, variavel pode ser "P", "V"
	ou "Q", sendo a variável de interesse no pv.plt. """
	myPlots = []
	file = openFile(file)
	fLines = readFile(file)

	endFile = "   0\n"

	patternValores = r"\d+[.]\d{4}" # regex para valores do gráfico
	patternIndice = r"(\d+)" # regex para numero de linhas do gráfico

	barNumber = ""
	readingPlot = False
	for entrie in range(3, len(fLines)):
		line = fLines[entrie]
		if line.startswith(variable):
			barNumber = line[4:9].strip(" ")
			readingPlot = True
			x = []
			y = []
		elif len(re.findall(patternIndice, line)) == 1:
			# Se encontrou numero de linhas, gráfico acabou
			if readingPlot:
				myPlots.append(Plot(barNumber, x, y)) # add new plot
				readingPlot = False
		elif readingPlot:
			# Adiciona linhas as vetor x e y
			values = re.findall(patternValores, fLines[entrie])
			x.append(float(values[0]))
			y.append(float(values[1]))
	return myPlots

def printPlot(plot, path, inflectionPoint=False, show=False):
	""" Either show or save the plot of a bar in the given path """
	plt.plot(plot.xdata, plot.ydata)
	if inflectionPoint:
		# Inclui o ponto de tensão critíca no gráfico, se ele existe
		plt.plot(inflectionPoint[0], inflectionPoint[1], color='red', marker="o")
	if show:
		plt.show()
	else:
		if Path(str(path)+"/figures").exists() == False:
			Path(str(path)+"/figures").mkdir()
		plt.savefig(str(path)+"/figures/"+str(plot.barNumber)+".png")
	plt.close()

def criticalVoltage(plot):
	""" Returns the critical voltage """
	return plot.yi

def inflectionPoint(x, y):
	""" Finds critical voltage point """
	dx = np.gradient(x) # Deriva eixo x
	desPoints = []
	for point in dx:
		if point > -1 and point < 1:
			# Encontra pontos próximo de 0
			desPoints.append(point)
	point = min(desPoints, key=abs) # Ponto mais proximo do zero
	indice = np.where(dx == point)[0][0] # Indice do ponto
	return x[indice], y[indice]

def loadMargin(plot):
	""" Load margin of a bar """
	margin = plot.xi - plot.xdata[0]
	return margin
