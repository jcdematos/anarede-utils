from functions import *
from fpGen import *
from readPWF import *
from readREL import *

# Classes
myBars = []
myPlots = []

# Define files and paths
configFile = openFile()
pathAnarede, casoBase, baseCPFLOW, pathWork = readConfig(configFile)

genCPFLOW = True

print("Caminho ANAREDE: %s" % pathAnarede)
print("Caso Base: %s" % casoBase)
print("Template CPFLOW: %s" % baseCPFLOW)
print("Caminho pasta de trabalho: %s" % pathWork)

# Ler pwf caso base
pwfFile = openFile(pathWork+"/"+casoBase)
pwfLines = readFile(pwfFile)
readPWF(pwfLines, myBars)
# Executar caso base
print("Running ANAREDE with %s" % pathWork+"/"+casoBase)
runAnarede(pathWork+"/"+casoBase)
filesList = [Bar.relPath, Bar.hisPath]
print("Moving file to %s" % pathWork)
moveFiles(pathAnarede, pathWork, filesList)
# Ler REL do caso base
print("Reading report file %s" % pathWork+"/"+Bar.relPath)
relFile = openFile(pathWork+"/"+Bar.relPath)
relLines = readFile(relFile)
readREL(myBars, relLines)

# If true, generate the cpflows
if genCPFLOW:
    print("Generating CPFLOWs with %s" % pathWork+"/"+baseCPFLOW)
    generateCPFLOW(pathWork+"/"+baseCPFLOW, pathWork, 3)

# Get generated folders
folders = getFolders(pathWork)
for folder in folders:
    # Run cpflows in each folders
    runCPFLOW(folder)
    
# 5 ler pv de cada cpflow
#   1 salvar em csv
#for folder in folderList:
#    runCPFLOW(folder)
#    filesList = createMoveFilesList(anaPath)
#    #moveFiles(anaPath, folder, filesList)
#print(filesList)
