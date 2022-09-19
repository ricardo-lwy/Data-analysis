from bs4 import BeautifulSoup  # this module helps in web scrapping.
import requests  # this module helps us to download a web page
import urllib.request
import re
import pandas as pd
from pandas.core.frame import DataFrame
from openpyxl.writer.excel import ExcelWriter
from lxml import etree
import requests  # 模拟浏览器请求的库
import re  # 正则库aaa@qq.com
from ast import Break
from http.client import NOT_FOUND
import re
header = {
    'user-agent': 'Mozilla/5.0(Macinatosh;Intel Mac OS X 10_13_6)Applewebkit/537.36(KHTML,like Gecko)Chrome/81.0.4044.138 Safari/537.36',
}



all_url = [


    "https://bohm-paris.com/collections/colliers/products/collier-bohm-paris-carlo?variant=40518289031350",
    #"https://bohm-paris.com/products/bague-bohm-paris-lotta?_pos=9&_sid=e2f364b77&_ss=r%20https://www.satine.paris/fr/bague-fine/5444-14294-bague-acier-inoxydable.html#/45-couleur-dor%C3%A9",
    #"https://bohm-paris.com/collections/colliers/products/collier-bohm-paris-carlo?variant=40518289096886",


]




# 15/09/2022 爬取bohm测试

from cgitb import html


result1 = []
linksname = []
link = DataFrame(all_url)
print(len(all_url))
for url in all_url:
    linksname.append(url)
    try:
        soup = BeautifulSoup(requests.get(url).text, "html.parser")

        # 通过查看字段发现它在第12项

    # 无货<button type="submit" data-use-primary-button="true" class="ProductForm__AddToCart Button Button--secondary Button--full" disabled="disabled">Rupture</button>
    # 有货<button type="submit" data-use-primary-button="true" class="ProductForm__AddToCart Button Button--primary Button--full" data-action="add-to-cart"><span>Ajouter au panier</span></button>
    # 有货警报<button type="submit" data-use-primary-button="true" class="ProductForm__AddToCart Button Button--primary Button--full" data-action="add-to-cart"><span>Ajouter au panier</span></button>
       # 网站特性，可以通过第一个submit值来判断
        buttontest = soup.find('button', {"type": "submit"})
        etat = [x.get_text() for x in buttontest]
        etatstr = etat[0]
        # 无货的情况
        if (etatstr == "Rupture"):
            result1.append("无货")
            print("OKOK")

        else:
            # 有货，未正确显示
            ptest = soup.find(
                    'p', {"class": "ProductForm__Inventory Text--subdued", "style": "display: none"})

            try:
                p_str = [x.get_text() for x in ptest]
                result1.append("货源充足")
                print("OKOK")
               

             # 有货，马上没货
           
            except:
                 # 没有显示马上无货，说明货源充足
                result1.append(p_str)
                print(p_str)
                print("OKOK")

    except:
        result1.append("notfound")
        print("notOKOK")


df_pm = DataFrame({'linksname': linksname, '剩余数量': result1})

df_pm

