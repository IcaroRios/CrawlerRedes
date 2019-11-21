import numpy as np
import tabula
import pandas as pd

# UTIL Functions
def is_nan(x):
    return (x is np.nan or x != x)
# ======================================================================

dataArray = []

dataArray.append('============================================================================================================================')

df = tabula.read_pdf("televisores.pdf", multiple_tables=True, lattice=False, stream=True, pages='2')
# DEVERÁ TER OUTRO TRATAMENTO
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

dataArray.append('============================================================================================================================')

df = tabula.read_pdf("congeladores.pdf", multiple_tables=True, lattice=False, stream=True, pages='all')
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

dataArray.append('============================================================================================================================')




for x in dataArray:
    print(x)
