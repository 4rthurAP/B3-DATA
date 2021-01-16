# *- enconding utf-8 -*

# Bibliotecas
 
from yahooquery import Ticker
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

##.history(start='2005-05-01', end='2013-12-31')

ambv = Ticker("ABEV3.SA")
ambvhistory  = ambv.history(period = "1d", interval = "60m")
ambvhistory.head()
print(ambvhistory['date'])
## print(petr.history(period="max"))

df = pd.DataFrame({'volume': [ambvhistory["volume"].head()],
                  'open': [ambvhistory["open"].head()],
                  'close': [ambvhistory["close"].head()],
                  'high': [ambvhistory["high"].head()],
                  'low': [ambvhistory["low"].head()]
                  })

# Criando um pandas writter no arquivo desejado.
writer = pd.ExcelWriter('Pasta1.xlsx')

# Converter o DataFrame em um arquivo xlsx.
df.to_excel(writer, sheet_name='planilha1')

# Salvar no arquivo xlsx.
writer.save()

##print(ambvhistory)