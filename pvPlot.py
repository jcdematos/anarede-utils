import sys
import re
import time
import matplotlib.pyplot as plt
from collections import namedtuple
import tkinter as tk
from tkinter import filedialog
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

Barra = namedtuple('Barra', 'title, xtitle, ytitle, barra, xdata, ydata')
#barra.append(Entrie('Titulo - Barra', 'xtitle', 'MW', 'ytitle', 'Tensoa V', 'barra', [1], [2]))
barra = []
file = "pv.plt"

if len(sys.argv) > 1:
    for argument in (sys.argv):
        if argument == '-d':
            logging.info("Command line argument -d")
            root = tk.Tk()
            root.withdraw()
            file = filedialog.askopenfilename()
        if argument == '-o':
            # open file from string passed
            pass

start_time = time.time()
if 1:
    with open(file, 'r') as dados:
        lines = dados.readlines();

    # Get title and x axis title
    title = lines[0].replace('\n', '')
    lines.pop(0)
    xtitle = lines[0].replace('\n', '')
    ytitle = "Tensao"
    lines.pop(0)

    # Regex para os valores, quantidade pontos e linha de barra
    patternValores = r"\d+[.]\d{4}"
    patternIndice = r"\d+"
    patternBarra = r"^[V]"

    numberEntries = 0
    for i in range(0,len(lines)):
        if not re.search(patternValores, lines[i]):
            if lines[i] == "Tensao\n":
                numberEntries += 1
                xvalues = [] # clear xvalues for tupple
                yvalues = []
                pass
            elif re.search(patternBarra, lines[i]):
                nome_barra = lines[i]
                listStart = i
            elif re.search(patternIndice, lines[i]):
                indices = re.findall(patternIndice, lines[i])
                indices = int(indices[0])
        else:
            values = re.findall(patternValores, lines[i])
            xvalues.append(float(values[0]))
            yvalues.append(float(values[1]))
            if (i == listStart + indices):
                barra.append(Barra(title, xtitle, ytitle, nome_barra, xvalues, yvalues))

    # Plotagem das curvas
    k = 0
    for b in barra:
        plt.figure(b.barra)
        plt.ylabel(b.ytitle)
        plt.xlabel(b.xtitle)
        plt.title(b.title + " " + b.barra)

        plt.plot(xvalues, yvalues)
        plt.savefig("figures/"+str(k)+"png")
        plt.close()
        k+=1

print("--- %s seconds ---" % (time.time() - start_time))
