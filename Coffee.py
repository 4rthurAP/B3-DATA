# *- enconding utf-8 -*

# Bibliotecas
 
from yahooquery import Ticker
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ambv = Ticker("ABEV3.SA")

# print(petr.history(period="max"))
ambvhistory  = ambv.history(period = "30d", interval = "15m")

# print(ambvhistory)
df = pd.DataFrame(ambvhistory)
print(ambvhistory)
# print(df["volume"].value_counts())
# print(df["open"].value_counts())
# print(df["close"].value_counts())
