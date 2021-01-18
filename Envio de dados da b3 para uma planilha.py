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

ambvhistory  = ambv.history(period = "1d", interval = "1m")
embrhistory  = embr.history(period = "1d", interval = "1m")

# escrevendo os históricos
ambvhistory.to_excel('Pasta1.xlsx')
embrhistory.to_excel('Pasta1.xlsx')

# Criando um pandas writter no arquivo desejado.

writer = pd.ExcelWriter('Pasta1.xlsx')

# Converter o DataFrame em um arquivo xlsx.

ambvhistory.to_excel(writer, sheet_name='AMBV3')
embrhistory.to_excel(writer, sheet_name='EMBR3')

# Salvar no arquivo xlsx. 

writer.save()

