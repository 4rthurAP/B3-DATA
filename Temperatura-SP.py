# bibliotecas
import bs4
from bs4 import BeautifulSoup


htmlText = """<div class="_flex _justify-center _align-center">
<img width="60" height="60" src="/dist/images/v2/svg/2.svg">
<span class="-bold -gray-dark-2 -font-55 _margin-l-20 _center">
26º
</span>
</div>"""

soup = BeautifulSoup(htmlText, features="lxml")
spans = soup.findAll('span')
for span in spans:
    print(span.text)