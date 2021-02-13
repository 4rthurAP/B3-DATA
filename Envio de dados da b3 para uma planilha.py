# *- enconding utf-8 -*

# Bibliotecas
 
from yahooquery import Ticker
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Listas das açoes utilizadas
ambv = Ticker("ABEV3.SA")
embr = Ticker("EMBR3.SA")

# Históricos
# AMBV
def ambev():
    ambvhistory = ambv.history(period = "1d", interval = "1m")
    return ambvhistory
#EMBR
def embraer(): 
    embrhistory  = embr.history(period = "1d", interval = "1m")
    return embrhistory

# escrevendo os históricos
ambev().to_excel('Pasta1.xlsx')
embraer().to_excel('Pasta1.xlsx')

# Criando um pandas writter no arquivo desejado.

writer = pd.ExcelWriter('D:/finance/B3-DATA/Ativos.xlsx')

# Converter o DataFrame em um arquivo xlsx.

ambev().to_excel(writer, sheet_name='AMBV3')
embraer().to_excel(writer, sheet_name='EMBR3')

# Salvar no arquivo xlsx. 

writer.save()

