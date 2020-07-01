import requests
from bs4 import BeautifulSoup
import re
URL = 'https://www.canadacomputers.com/product_info.php?cPath=26_1832_1833&item_id=167427&language=en'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find("span", class_="h2-big").get_text()
results = re.sub("[^\\d.]", "", results)
print(float(results.strip()))
