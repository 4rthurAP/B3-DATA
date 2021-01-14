# *- enconding utf-8 -*

# Bibliotecas
 
from yahooquery import Ticker
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

##.history(start='2005-05-01', end='2013-12-31')

ambv = Ticker("ABEV3.SA")
ambvhistory  = ambv.history(period = "7d", interval = "30m")
ambvhistory.head()
## print(petr.history(period="max"))

df = pd.DataFrame({'volume': [ambvhistory["volume"].head()]},)

# Criando um pandas writter no arquivo desejado.
writer = pd.ExcelWriter('Pasta1.xlsx')

# Converter o DataFrame em um arquivo xlsx.
df.to_excel(writer, sheet_name='Sheet1')

# Salvar no arquivo xlsx.
writer.save()

print(df)