"""
PROGRAM NAME - readREL
PROGRAMMER - J. Matos, 06-2021
USAGE - Run the program after running readPWF in a PFLOW simulation file.
DATE - 19/06/2021
BUGS -
DESCRIPTION - Le um relatório gerado pelo anarede e salva o módulo de tensão,
              angulo da barra e dados de geração e dados de carga em cada barra.
"""
import re
import time
import subprocess
from pathlib import Path
from functions import *

def readREL(myBars, file="none"):
    print(file)
    file = openFile(sys, file)
    fLines = readFile(file)

    for entrie in range(0, len(fLines)):
        line = fLines[entrie]
        if (line.find("RELATORIO DE BARRAS CA") > -1):
            entrie+=8 # Pula cabeçalho
            while True:
                line = fLines[entrie]
                entrie+=1
                if (line.find("CEPEL") > -1):
                    break
                else:
                    number = line[3:8].strip(" ")
                    for bar in myBars:
                        if (bar.number == number):
                            pg = line[37:44]
                            qg = line[45:52]
                            pl = line[69:76]
                            ql = line[77:84]
                            bar.addFluxPot(pg, qg, pl, ql)
