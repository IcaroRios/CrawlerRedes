from utils import generate_random_start, generate_from_seed
from keras.models import load_model
import tensorflow as tf
from flask import Flask, render_template, request
from wtforms import Form, TextField, validators, SubmitField, DecimalField, IntegerField
import numpy as np
import tabula
import pandas as pd
import json

# UTIL Functions
def is_nan(x):
    return (x is np.nan or x != x)

app = Flask(__name__)

@app.route("/")
def hello():
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
    return dataArray


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)