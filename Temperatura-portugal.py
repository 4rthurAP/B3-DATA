import requests
import bs4
res = requests.get('https://forecast.weather.gov/MapClick.php?lat=37.78762000000006&lon=-122.39600999999999#.XWQ8MOhKg2w')
objSoup = bs4.BeautifulSoup(res.text,features="html.parser")
html_obj=objSoup.select('.myforecast-current-lrg')
temp = html_obj[0].getText()

print(temp)