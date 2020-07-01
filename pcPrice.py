import requests
from bs4 import BeautifulSoup
import re
from twilio.rest import Client
import time
from creds import account_sid, auth_token, cell, twillio_num
class pcPrice:
    def __init__(self):
        self.final_price = 0
        self.mother_board = 249.0
        self.cpu = 300.00
        self.RAM = 104.99
        self.m2SSD = 99.99
        self.HDD =  74.99
        self.case = 79.99
        self.psu = 69.99
        self.gpu = 239.00
        self.fans = 54.99
        self.pc_part_list = {"Motherboard": "No Sale", "CPU": "No Sale", "RAM": "No Sale", "SSD": "No Sale", "HDD": "No Sale", "Case": "No Sale", "PSU": "No Sale",
        "GPU": "No Sale", "Fans": "No Sale"}
    def check_prices(self):
        for i in range(8):
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
            if i == 0:
                if(float(results) < self.mother_board):
                    self.pc_part_list["Motherboard"] = "Sale"

            elif i == 1:
                if(float(results) < self.cpu):
                    self.pc_part_list["CPU"] = "Sale"
            elif i == 2:
                if(float(results) < self.RAM):
                    self.pc_part_list["RAM"] = "Sale"
            elif i == 3:
                if(float(results) < self.m2SSD):
                    self.pc_part_list["SSD"] = "Sale"
            elif i == 4:
               if(float(results) < self.HDD):
                    self.pc_part_list["HDD"] = "Sale"
            elif i == 5:
                if(float(results) < self.case):
                    self.pc_part_list["Case"] = "Sale"
            elif i == 6:
                if(float(results) < self.psu):
                    self.pc_part_list["PSU"] = "Sale"
            elif i == 7:
                if(float(results) < self.gpu):
                    self.pc_part_list["GPU"] = "Sale"
            self.final_price += float(results)
            # print(final_price)
        headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
        }
        URL = 'https://www.amazon.ca/Corsair-CO-9050084-WW-Af120-Cooling-Triple/dp/B07KGZ42XL/ref=pd_lpo_147_t_2/143-1327161-9681242?_encoding=UTF8&pd_rd_i=B07KGZ89V5&pd_rd_r=b4fc5e26-03cd-442f-83cd-bbde9b824117&pd_rd_w=Ub3F8&pd_rd_wg=EwjLV&pf_rd_p=256a14b6-93bc-4bcd-9f68-aea60d2878b9&pf_rd_r=1M0MFRMRB79FC5JYTXQ3&refRID=1M0MFRMRB79FC5JYTXQ3&th=1'
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'lxml')   
        results = soup.find("span", class_="a-size-medium a-color-price priceBlockBuyingPriceString").get_text().strip()
        results = re.sub("[^\\d.]", "", results)
        if(float(results) < self.fans):
                    self.pc_part_list["Fans"] = "Sale"
        # print(results)
        self.final_price += float(results)
        # print(self.pc_part_list)
        return self.final_price

pcp = pcPrice()

while True:
    final_price = pcp.check_prices()
    final_price*= 1.13
    
    client = Client(account_sid, auth_token)
    full_message = "the final price of your build is: " + str("{:.2f}".format(final_price)) +"\n" + str(pcp.pc_part_list)
    # print(full_message)
    message = client.messages.create(body=full_message,from_=twillio_num,to=cell)
    time.sleep(86400)