import numpy as np
import tabula
import pandas as pd
import json
# UTIL Functions
def is_nan(x):
    return (x is np.nan or x != x)
# ======================================================================
dataArray = []
df = tabula.read_pdf("http://www.inmetro.gov.br/consumidor/pbe/congeladores.pdf", multiple_tables=True, lattice=False, stream=True, pages='all')
for table in df:
    data = pd.DataFrame(table) #convertendo pagina em Panda DataFrame
    for row, value in data.iterrows():
        rowData = []
        hasNaN = False
        for collumn in list(data):
            if is_nan(data[collumn][row]) :
                hasNaN = True
            else:
                rowData.append(data[collumn][row])
        if not hasNaN:
            dataArray.append(rowData)

# print(dataArray)
del dataArray[:5]
# print (dataArray)

#CASO TUDO DER ERRADO, COLOCAR ESSE CÓDIGO AQUI PARA GERAR O ARQUIVO E SER LIDO PELO DATATABLES.

fileOUT = open('teste.txt','w+')
fileOUT.write('{\n\t"demo": [\n')
for num,congelador in enumerate(dataArray,start=1):
    fileOUT.write('\t\t[\n')
    for num2,data in enumerate(congelador,start=1):
        fileOUT.write('\t\t\t')
        fileOUT.write('\"')
        fileOUT.write(data)
        if num2 == len(congelador):
            fileOUT.write('\"\n')
        else:
            fileOUT.write('\",\n')
    if num == len(dataArray):
        fileOUT.write('\t\t]\n')
    else:
        fileOUT.write('\t\t],\n')
fileOUT.write('\t]\n}')
fileOUT.close()
