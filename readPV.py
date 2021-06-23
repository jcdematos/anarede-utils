"""
PROGRAM NAME - readPV
PROGRAMMER - J. Matos, 06-2021
DATE - Started 22/06/2021
DESCRIPTION - Funções para ler um pv.plot, retornar os plots organizados em
              barras, além de função para gerar a margem de carregamento e
              tensão critica do sistema.
"""
import sys
import re
import time
import matplotlib.pyplot as plt
from collections import namedtuple
from functions import *

class Plot:
    """ Class to hold the data for each plot """
    def __init__(self, barNumber, xdata, ydata):
        self.barNumber = barNumber
        self.xdata = xdata
        self.ydata = ydata

def typeByNumber(number, myBars):
	for bar in myBars:
		if bar.number == number:
			return bar.tipo

def barraPQ(number, myBars):
    if typeByNumber(number, myBars) == "":
        return True
    if typeByNumber(number, myBars) == "0":
        return True

def readPV(variable, myBars, file="none"):
    myPlots = []
    file = openFile(sys, file)
    fLines = readFile(file)

    endPlot = fLines[2]
    endFile = "   0\n"
    variable = "V"

    patternValores = r"\d+[.]\d{4}"
    barNumber = ""
    readingPlot = False
    for entrie in range(3, len(fLines)):
        line = fLines[entrie]
        if line.startswith(variable):
            barNumber = line[4:9].strip(" ")
            readingPlot = True
            x = []
            y = []
            #if bar is generator, do not read
        elif line.startswith(endPlot) or line.startswith(endFile):
            if readingPlot:
                # found end of plot
                myPlots.append(Plot(barNumber, x, y)) # add new plot
                readingPlot = False
        elif readingPlot:
            values = re.findall(patternValores, fLines[entrie])
            x.append(float(values[0]))
            y.append(float(values[1]))
    return myPlots

def loadMargin(plot, myBars):
    if not barraPQ(plot.barNumber, myBars):
        return False
    print("BARRA")
    print(plot.barNumber)
    print(plot.xdata)
    print(plot.ydata)
    x0 = plot.xdata[0]
    y0 = plot.ydata[0]
    yMax = min(plot.ydata)
    print(x0)
    print(y0)
    print(yMax)
