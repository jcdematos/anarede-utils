"""
PROGRAM NAME - fpGen
PROGRAMMER - J. Matos, 06-2021
USAGE - Escolha um caso base e gera cpflows como diferentes fatores de potência.
		Dar uma entrada de quantos gerar, limite superior e inferior do fator

DATE - 21/06/2021
BUGS -
DESCRIPTION - Cria casos de fluxo de potência continuado com diferentes fatores
			  de crescimento.
"""
import time
from pathlib import Path
from functions import *
from random import seed
from random import random

seed(time.time())

def findDINC(fLines):
	""" Recebe linhas do arquivo de interesse e retorna o index da linha onde
	define-se o crescimento da potência ativa e reativa.
	"""

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

file = openFile(sys)
fLines = readFile(file)

linha = findDINC(fLines)

f = open("teste.pwf", "w")
f.writelines(fLines[linha])
f.close()
