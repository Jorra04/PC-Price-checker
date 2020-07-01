import requests
from bs4 import BeautifulSoup
import re
final_price = 0

for i in range(8):
    # print(i)
    if i == 0:
        URL = 'https://www.canadacomputers.com/product_info.php?cPath=26_1832_1833&item_id=167427&language=en'
    elif i == 1:
        URL = 'https://www.canadacomputers.com/product_info.php?cPath=4_64&item_id=138215&language=en'
    elif i == 2:
        URL = 'https://www.canadacomputers.com/product_info.php?cPath=24_311_1326&item_id=096846'
    elif i == 3:
        URL = 'https://www.canadacomputers.com/product_info.php?cPath=179_1927_1928&item_id=114574'
    elif i == 4:
        URL = 'https://www.canadacomputers.com/product_info.php?cPath=15_1086_210&item_id=132494'
    elif i == 5:
        URL = 'https://www.canadacomputers.com/product_info.php?cPath=6_1937&item_id=151357'
    elif i == 6:
        URL = 'https://www.canadacomputers.com/product_info.php?cPath=33_1938&item_id=094360'
    elif i == 7:
        URL = 'https://www.canadacomputers.com/product_info.php?cPath=43_557_558&item_id=107533'
    
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    
    results = soup.find("span", class_="h2-big").get_text().strip()
    results = re.sub("[^\\d.]", "", results)

    final_price += float(results)
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}
URL = 'https://www.amazon.ca/Corsair-CO-9050084-WW-Af120-Cooling-Triple/dp/B07KGZ42XL/ref=pd_lpo_147_t_2/143-1327161-9681242?_encoding=UTF8&pd_rd_i=B07KGZ89V5&pd_rd_r=b4fc5e26-03cd-442f-83cd-bbde9b824117&pd_rd_w=Ub3F8&pd_rd_wg=EwjLV&pf_rd_p=256a14b6-93bc-4bcd-9f68-aea60d2878b9&pf_rd_r=1M0MFRMRB79FC5JYTXQ3&refRID=1M0MFRMRB79FC5JYTXQ3&th=1'
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'lxml')   
results = soup.find("span", class_="a-size-medium a-color-price priceBlockBuyingPriceString").get_text().strip()
results = re.sub("[^\\d.]", "", results)
# print(results)
final_price += float(results)

final_price *= 1.13

print("the final price of your build is: " + str("{:.2f}".format(final_price)))
