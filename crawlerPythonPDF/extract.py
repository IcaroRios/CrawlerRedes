import math
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

print(dataArray)

