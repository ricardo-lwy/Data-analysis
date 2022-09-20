
from cmath import inf
#from socket import TIPC_CLUSTER_SCOPE
from bs4 import BeautifulSoup  # this module helps in web scrapping.
import requests  # this module helps us to download a web page
import urllib.request
import pandas as pd
from pandas.core.frame import DataFrame
from openpyxl.writer.excel import ExcelWriter
from lxml import etree
import requests  # 模拟浏览器请求的库
from cgitb import html
from ast import Break
from http.client import NOT_FOUND
import re
from time import sleep
import skudata
# 读取
# 读取需求的excel文件的数据

df = pd.read_excel('.xlsx', sheet_name='Feuille1')



# 一共有多少行
sumline = len(df)

# print(data)
print(sumline+1)

# 后面需要生成的列表
# SKU,infinitus站上的值，爬取得出的结果
# dfpm1


# 0
HANDLES = []
# 1
TITLES = []
# 2
OPTION1NAME = []
# 3
OPTION1VALUE = []
# 4
OPTION2NAME = []
# 5
OPTION2VALUE = []
# 6
OPTION3NAME = []
# 7
OPTION3VALUE = []
# 8
SKUS = []
# 9
HSCODES = []
# 10
COO = []
# 11
INFVAL = []
# 我们将后面自己添加的差异状态以及实际网站数据加在后面
# 12
LINKS = []
# 13
LINKVAL = []
# 14
ETAT = []


# 第二种情况，无链接或者被墙放在另一个文件里面
# dfpm2
HANDLES2 = []
TITLES2 = []
OPTION1NAME2 = []
OPTION1VALUE2 = []
OPTION2NAME2 = []
OPTION2VALUE2 = []
OPTION3NAME2 = []
OPTION3VALUE2 = []
SKUS2 = []
HSCODES2 = []
COO2 = []
INFVAL2 = []
# 我们将后面自己添加的差异状态以及实际网站数据加在后面
LINKS2 = []
LINKVAL2 = []
ETAT2 = []


# 休眠时判定
grabcount = 1
for i in range(0, sumline):
    # 读取二维数组中的数据。
    # sku
    grabcount += 1
    # 200的整数倍
    if (grabcount%200 == 0):
        print("休息一下")
        sleep(120)
    rowsku = df.values[i][8]
    rowinfval = df.values[i][11]
    # python 的for循环有点问题，加个count计数
    count = -1
    indexnum = -1
    for j in range(0, len(skudata.all_sku)):
        count = count+1
        # 查找索引
        if (skudata.all_sku[j] == rowsku):
            print(count)
            indexnum = count
            break
    if (indexnum == -1):
        print("警报！,未找到", rowsku, "对应的SKU!")
# 没找到这个Sku，因此我们要将他添加到错误日志中
        HANDLES2.append(df.values[i][0])
        TITLES2.append(df.values[i][1])
        OPTION1NAME2.append(df.values[i][2])
        OPTION1VALUE2.append(df.values[i][3])
        OPTION2NAME2.append(df.values[i][4])
        OPTION2VALUE2.append(df.values[i][5])
        OPTION3NAME2.append(df.values[i][6])
        OPTION3VALUE2.append(df.values[i][7])
        SKUS2.append(rowsku)
        HSCODES2.append(df.values[i][9])
        COO2.append(df.values[i][10])
        INFVAL2.append(rowinfval)
        # 自定义数据
        LINKS2.append("sku在库中不存在因此没有对应链接！")
        LINKVAL2.append(0)
        ETAT2.append("错误原因：sku在库中不存在！！！！！！！！！")

    else:
        requrl = skudata.all_url[indexnum]
        print("成功找到", rowsku, "名字为：",
              skudata.all_sku[indexnum], "对应的url为：", requrl)
        # 找到索引，开始爬虫任务；
        #########20/09/2022更新：需要找到解释器
        try:
            soup = BeautifulSoup(requests.get(requrl).text, "html.parser")
# 无货<button type="submit" data-use-primary-button="true" class="ProductForm__AddToCart Button Button--secondary Button--full" disabled="disabled">Rupture</button>
    # 有货<button type="submit" data-use-primary-button="true" class="ProductForm__AddToCart Button Button--primary Button--full" data-action="add-to-cart"><span>Ajouter au panier</span></button>
    # 有货警报<button type="submit" data-use-primary-button="true" class="ProductForm__AddToCart Button Button--primary Button--full" data-action="add-to-cart"><span>Ajouter au panier</span></button>
         # 网站特性，可以通过第一个submit值来判断
         # 语法规则find('tag域'，{tag中的参数})
            buttontest = soup.find('button', {"type": "submit"})
            etat = [x.get_text() for x in buttontest]
            etatstr = etat[0]
            if (etatstr == "Rupture"):  # 无货的情况
                print("网站无货")
                if (rowinfval > 0):  # 情况一供应商无货但是我们网站显示有货
                    # 原始数据插入
                    HANDLES.append(df.values[i][0])
                    TITLES.append(df.values[i][1])
                    OPTION1NAME.append(df.values[i][2])
                    OPTION1VALUE.append(df.values[i][3])
                    OPTION2NAME.append(df.values[i][4])
                    OPTION2VALUE.append(df.values[i][5])
                    OPTION3NAME.append(df.values[i][6])
                    OPTION3VALUE.append(df.values[i][7])
                    SKUS.append(rowsku)
                    HSCODES.append(df.values[i][9])
                    COO.append(df.values[i][10])
                    INFVAL.append(rowinfval)

                    # 我们自己加的数据
                    LINKS.append(requrl)
                    LINKVAL.append(0)
                    ETAT.append("供应商无货但是我们网站显示有货")
                    print("出现情况1.供应商无货但是我们网站显示有货")
            else:
                # 有货，未正确显示
                try:
                    ptest = soup.find(
                        'p', {"class": "ProductForm__Inventory Text--subdued", "style": "display: none"})

                    p_str = [x.get_text() for x in ptest]  # 执行不了就跳出进入except阶段
                    # 货源充足
                    print("货源充足")
                    # 情况2，货源充足但是我们网站显示无货。
                    if (rowinfval < 1):
                        HANDLES.append(df.values[i][0])
                        TITLES.append(df.values[i][1])
                        OPTION1NAME.append(df.values[i][2])
                        OPTION1VALUE.append(df.values[i][3])
                        OPTION2NAME.append(df.values[i][4])
                        OPTION2VALUE.append(df.values[i][5])
                        OPTION3NAME.append(df.values[i][6])
                        OPTION3VALUE.append(df.values[i][7])
                        SKUS.append(rowsku)
                        HSCODES.append(df.values[i][9])
                        COO.append(df.values[i][10])
                        INFVAL.append(rowinfval)

                        # 我们自己加的数据
                        LINKS.append(requrl)
                        LINKVAL.append(3)
                        ETAT.append("货源充足但是我们网站显示无货")
                        print("出现情况2.货源充足但是我们网站显示无货")

                    # 有货，马上没货
                except:

                    ptest = soup.find(
                        'p', {"class": "ProductForm__Inventory Text--subdued"})
                    p_str = [x.get_text() for x in ptest]
                    # 匹配数字
                    p_num = int(re.findall(r"\d+", p_str[0])[0])

                    if (p_num < 2 and rowinfval > 0):  # 小于2的情况，视为无货，但是我们网站显示有货
                        # 情况三，货源为1但是我们网站显示充足
                        HANDLES.append(df.values[i][0])
                        TITLES.append(df.values[i][1])
                        OPTION1NAME.append(df.values[i][2])
                        OPTION1VALUE.append(df.values[i][3])
                        OPTION2NAME.append(df.values[i][4])
                        OPTION2VALUE.append(df.values[i][5])
                        OPTION3NAME.append(df.values[i][6])
                        OPTION3VALUE.append(df.values[i][7])
                        SKUS.append(rowsku)
                        HSCODES.append(df.values[i][9])
                        COO.append(df.values[i][10])
                        INFVAL.append(rowinfval)

                        # 我们自己加的数据
                        LINKS.append(requrl)
                        LINKVAL.append(0)
                        ETAT.append("供应商货只剩一个但是我们网站显示有货")
                        print("情况三，货源为1但是我们网站显示充足")

                    elif (p_num >= 2 and rowinfval < 1):
                        # 情况4，网站虽然警报但是有货，我们显示无货
                        HANDLES.append(df.values[i][0])
                        TITLES.append(df.values[i][1])
                        OPTION1NAME.append(df.values[i][2])
                        OPTION1VALUE.append(df.values[i][3])
                        OPTION2NAME.append(df.values[i][4])
                        OPTION2VALUE.append(df.values[i][5])
                        OPTION3NAME.append(df.values[i][6])
                        OPTION3VALUE.append(df.values[i][7])
                        SKUS.append(rowsku)
                        HSCODES.append(df.values[i][9])
                        COO.append(df.values[i][10])
                        INFVAL.append(rowinfval)

                        # 我们自己加的数据
                        LINKS.append(requrl)
                        LINKVAL.append(3)
                        ETAT.append("货源数大于1但是我们网站显示无货")
                        print("出现情况4.货源数大于1但是我们网站显示无货")

        except:
            HANDLES2.append(df.values[i][0])
            TITLES2.append(df.values[i][1])
            OPTION1NAME2.append(df.values[i][2])
            OPTION1VALUE2.append(df.values[i][3])
            OPTION2NAME2.append(df.values[i][4])
            OPTION2VALUE2.append(df.values[i][5])
            OPTION3NAME2.append(df.values[i][6])
            OPTION3VALUE2.append(df.values[i][7])
            SKUS2.append(rowsku)
            HSCODES2.append(df.values[i][9])
            COO2.append(df.values[i][10])
            INFVAL2.append(rowinfval)
            LINKVAL2.append(0)
            LINKS2.append(requrl)
            ETAT2.append("出现情况5，对应链接为空或者网站被墙")
            print("出现情况5，链接无效或者网站被墙")


# 生成结果界面和错误日志
########################################################################
#########################################################################
###########################################################################

df_pm1 = DataFrame({'Handle':HANDLES,'Title':TITLES,'Option1 Name':OPTION1NAME,'Option1 Value':OPTION1VALUE,'Option2 Name':OPTION2NAME,'Option2 Value':OPTION2VALUE,'Option3 Name':OPTION3NAME,'Option3 Value':OPTION3VALUE,'SKU':SKUS,'HS Code':HSCODES,'COO':COO,'INFINITUS CIFA':INFVAL,'SKU_URL':LINKS,'实际存货':LINKVAL,'状态':ETAT})
df_pm2 = DataFrame({'Handle':HANDLES2,'Title':TITLES2,'Option1 Name':OPTION1NAME2,'Option1 Value':OPTION1VALUE2,'Option2 Name':OPTION2NAME2,'Option2 Value':OPTION2VALUE2,'Option3 Name':OPTION3NAME2,'Option3 Value':OPTION3VALUE2,'SKU':SKUS2,'HS Code':HSCODES2,'COO':COO2,'INFINITUS CIFA':INFVAL2,'SKU_URL':LINKS2,'存货情况':LINKVAL2,'状态':ETAT2})
print(df_pm1)
print(df_pm2)


#######################################
# 写入代码暂时没有写，在控制台中进行控制会更加方便
# 写入结果到excel，询问具体需求。
# 19/09/2022 by Weiyi LIU
