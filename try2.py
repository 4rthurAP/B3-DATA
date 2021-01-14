import pandas as pd
from pandas import DataFrame
from yahooquery import Ticker
from openpyxl import Workbook
from openpyxl import worksheet
import xlsxwriter

ambv = Ticker("ABEV3.SA")
ambvhistory  = ambv.history(period = "7d", interval = "30m")
ambvhistory.head()

df = pd.DataFrame({'open': [ambvhistory["open"].head()],
                  'close': [ambvhistory["close"].head()],
})

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter("Pasta1.xlsx")

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')

# Get the xlsxwriter workbook and worksheet objects.
Workbook  = writer.book
worksheet = writer.sheets['Sheet1']

# Add some cell formats.
format1 = Workbook.addformat({'num_format': '#,##0.00'})
format2 = Workbook.addformat({'num_format': '0%'})

# Note: It isn't possible to format any cells that already have a format such
# as the index or headers or any cells that contain dates or datetimes.

# Set the column width and format.
worksheet.set_column('B:B', 18, format1)

# Set the format but not the column width.
worksheet.set_column('C:C', None, format2)

# Close the Pandas Excel writer and output the Excel file.
writer.save()

## apenas mais uma tentativa falha... ##