import requests
res = requests.get('https://forecast.weather.gov/MapClick.php?lat=37.78762000000006&lon=-122.39600999999999#.XWQ8MOhKg2w')
res.raise_for_status() #verificar se existem erros
###3) Parse data

import bs4
objSoup = bs4.BeautifulSoup(res.text,features="html.parser")
html_obj=objSoup.select('.myforecast-current-lrg')
temp = html_obj[0].getText()
##
print(temp)