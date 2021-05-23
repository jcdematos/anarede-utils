import sys
import re
import time
import matplotlib.pyplot as plt
from collections import namedtuple

start_time = time.time()

# to implement
# be able to pass no argument, will get pv.plt this ways
# be able to pass the argument of the file as restricting
#   use -o for open
# be able to open a dialog to choose the file
#   use -d for open dialog
#print('Numbers of arguments: {}'.format(len(sys.argv)))
#print('Arguments(s) passed{}'.format(str(sys.argv)))


# how to parse the file?
# file structure:
# two first lines seems to be headers
# CURVAPXV - since this template seems to be used in other files from cepel, use this as title
# Carregamento (MW) - use as X axis title and unit
# This section is standard for every entrie
# x axis is given in second line
# y axis in given here
# number of lines
# y axis
# unit for y axis, number of the bar, name of the bar
# data for x and y, respectivly
# for numbers, anarede seems to use 4 decimals, this may be of use on regex
#Entrie = namedtuple('Entrie', 'title, xtitle, xunit, ytitle, yunit, barra, xdata, ydata')
Barra = namedtuple('Barra', 'title, xtitle, ytitle, barra, xdata, ydata')
#barra.append(Entrie('Titulo - Barra', 'xtitle', 'MW', 'ytitle', 'Tensoa V', 'barra', [1], [2]))
barra = []

if 1:
    # read file into lines
    with open('pv.plt', 'r') as dados:
        lines = dados.readlines();

    # get global title and x axis
    # as they are the same during the file
    title = lines[0].replace('\n', '')
    lines.pop(0)
    xtitle = lines[0].replace('\n', '')
    ytitle = "Tensao"
    lines.pop(0)
    #print(title, end="")
    #print(xtitle, end="")


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
#                print("barra = " + nome_barra, end="")
                listStart = i
            elif re.search(patternIndice, lines[i]):
                indices = re.findall(patternIndice, lines[i])
                indices = int(indices[0])
#                print("indices = ", end="")
#                print(indices)
        else:
            values = re.findall(patternValores, lines[i])
            xvalues.append(float(values[0]))
            yvalues.append(float(values[1]))
#            print(listStart)
            if (i == listStart + indices):
#                print(xvalues)
#                print(yvalues)
                barra.append(Barra(title, xtitle, ytitle, nome_barra, xvalues, yvalues))
#            print(lines[i], end="")
#    print("N entries = " + str(numberEntries))

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
