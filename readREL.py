"""
PROGRAM NAME - readREL
PROGRAMMER - J. Matos, 06-2021
DATE - 19/06/2021
BUGS -
DESCRIPTION - Function to read a .REL file.
"""
from functions import *

def readREL(myBars, file="none"):
    """ Read a .REL file and add data to a Bar object """
    file = openFile(sys, file)
    fLines = readFile(file)

    for entrie in range(0, len(fLines)):
        line = fLines[entrie]
        if (line.find("RELATORIO DE BARRAS CA") > -1):
            # Inicia leitura de pagina
            entrie+=8 # Pula cabeçalho
            while True:
                line = fLines[entrie]
                entrie+=1
                if (line.find("CEPEL") > -1):
                    # Para leitura no fim da página
                    break
                else:
                    # Le dados de geração da barra
                    number = line[3:8].strip(" ")
                    for bar in myBars:
                        if (bar.number == number):
                            pg = line[37:44]
                            qg = line[45:52]
                            pl = line[69:76]
                            ql = line[77:84]
                            bar.addFluxPot(pg, qg, pl, ql)
