##############计划对其进行扩展21/09/2022


########库文件
from bs4 import BeautifulSoup  # this module helps in web scrapping.
import requests  # this module helps us to download a web page 
from pandas.core.frame import DataFrame
import re



##################################
#数据列表部分
######################################
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


###################################################
###################################################
###################################################
#################        Fournisseur
class Fournisseur:
    def _init_():
        pass



###################################################
###################################################
###################################################
#################        ERROR
class typeError(Fournisseur):
    def soulution(self,df,i):
        HANDLES2.append(df.values[i][0])
        TITLES2.append(df.values[i][1])
        OPTION1NAME2.append(df.values[i][2])
        OPTION1VALUE2.append(df.values[i][3])
        OPTION2NAME2.append(df.values[i][4])
        OPTION2VALUE2.append(df.values[i][5])
        OPTION3NAME2.append(df.values[i][6])
        OPTION3VALUE2.append(df.values[i][7])
        SKUS2.append(df.values[i][8])
        HSCODES2.append(df.values[i][9])
        COO2.append(df.values[i][10])
        INFVAL2.append(df.values[i][11])
        # 自定义数据
        LINKS2.append("sku在库中不存在因此没有对应链接")
        LINKVAL2.append(0)
        ETAT2.append("错误原因:sku在库中不存在")
        




###################################################
###################################################
###################################################
#################         Satine
class SATINE(Fournisseur):

    def solution(self,df,i,requrl):
        header = {
        ########添加了一个用于记录登录数据的cookie在cookie刷新时记得要进行更换
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'Cookie': 'PHPSESSID=hc9d38hsqnbtj9c32cst5smev6; PrestaShop-adb724137fa62e51fd1ec2c1ff45bce3=def502003dcd341803ddc6e422a19da3f2d555b06eec511b726f2a7ebb0cfc6efea4233598f0b7562ea9782c9610263759e99130421088c814b7bf0ee328268e87e06194fe8f177f04369c4d80e49342dcf88e138c50879c8da25074a28606a4c823e0fa977fa5d5be3414aadb4e25430028723d52711df2abea87da1f0428d8eb09147ee244e777e995339bcfa6b249735080272c4d208aed359545b02657cde8d36cd55a86b92eb62daf0784a9d3b1a2b62396f5d5049ff6ec0fc16550b4d50293c3083f7438c7090ed6b52daa5a40cda3c76caf6b8ccc62f88ecc32295355bb2af3cc87e6f379e60e5d5e6e4aa3f630dbbdee62da058065ecc997146cf59d1229634f60760b521a9dfc738acd69fe2194b26762a4c7e6d4dad657206dec367ec77e3cca6421bed971bb35108e9f3d894a3aeefb683b14d6c7cd5f5c5ad3a13b8ef373df9a762a495fe498461f1d3b501c70b95d208d5750fe288b4fc15dab1eeba5a080244c3d3decba8df0653163200265640871212b892f46dd175e6c08eaf43007ecb204336cccde3ca3c6447c1b675e6082c7e4bb249ec80472c68e5b6d6b7aeff5f8f6b3e7062963efeb9904fb184781202bd4ea9b4a6c286c3fda7eb3a222'
    }

        try:
            soup = BeautifulSoup(requests.get(requrl,headers=header).text, "html.parser")

            alerteicon = soup.find('span', {"id": "product-availability"})
            try:
                alertelength=len(alerteicon)
        
                if (alertelength >1):  # 无货的情况#####alerte多个
                    print("网站无货")
                    if (df.values[i][11] > 0):  # 情况一供应商无货但是我们网站显示有货
                        # 原始数据插入
                        HANDLES.append(df.values[i][0])
                        TITLES.append(df.values[i][1])
                        OPTION1NAME.append(df.values[i][2])
                        OPTION1VALUE.append(df.values[i][3])
                        OPTION2NAME.append(df.values[i][4])
                        OPTION2VALUE.append(df.values[i][5])
                        OPTION3NAME.append(df.values[i][6])
                        OPTION3VALUE.append(df.values[i][7])
                        SKUS.append(df.values[i][8])
                        HSCODES.append(df.values[i][9])
                        COO.append(df.values[i][10])
                        INFVAL.append(df.values[i][11])

                        # 我们自己加的数据
                        LINKS.append(requrl)
                        LINKVAL.append(0)
                        ETAT.append("供应商无货但是我们网站显示有货")
                        print("出现情况1.供应商无货但是我们网站显示有货")
                else:
                    # 供应商有货且充足
                    print("货源充足")

                
                    # 情况2，货源充足但是我们网站显示无货。
                    if (df.values[i][11] < 1):
                        HANDLES.append(df.values[i][0])
                        TITLES.append(df.values[i][1])
                        OPTION1NAME.append(df.values[i][2])
                        OPTION1VALUE.append(df.values[i][3])
                        OPTION2NAME.append(df.values[i][4])
                        OPTION2VALUE.append(df.values[i][5])
                        OPTION3NAME.append(df.values[i][6])
                        OPTION3VALUE.append(df.values[i][7])
                        SKUS.append(df.values[i][8])
                        HSCODES.append(df.values[i][9])
                        COO.append(df.values[i][10])
                        INFVAL.append(df.values[i][11])

                        # 我们自己加的数据
                        LINKS.append(requrl)
                        LINKVAL.append(3)
                        ETAT.append("货源充足但是我们网站显示无货")
            
                        print("出现情况2.货源充足但是我们网站显示无货")
            except:##没有长度，说明连警报框都找不到，货量充足
                print("货源充足")
                # 情况2，货源充足但是我们网站显示无货。
                if (df.values[i][11] < 1):
                    HANDLES.append(df.values[i][0])
                    TITLES.append(df.values[i][1])
                    OPTION1NAME.append(df.values[i][2])
                    OPTION1VALUE.append(df.values[i][3])
                    OPTION2NAME.append(df.values[i][4])
                    OPTION2VALUE.append(df.values[i][5])
                    OPTION3NAME.append(df.values[i][6])
                    OPTION3VALUE.append(df.values[i][7])
                    SKUS.append(df.values[i][8])
                    HSCODES.append(df.values[i][9])
                    COO.append(df.values[i][10])
                    INFVAL.append(df.values[i][11])

                    # 我们自己加的数据
                    LINKS.append(requrl)
                    LINKVAL.append(3)
                    ETAT.append("货源充足但是我们网站显示无货")
        
                    print("出现情况2.货源充足但是我们网站显示无货")

        except:
            HANDLES2.append(df.values[i][0])
            TITLES2.append(df.values[i][1])
            OPTION1NAME2.append(df.values[i][2])
            OPTION1VALUE2.append(df.values[i][3])
            OPTION2NAME2.append(df.values[i][4])
            OPTION2VALUE2.append(df.values[i][5])
            OPTION3NAME2.append(df.values[i][6])
            OPTION3VALUE2.append(df.values[i][7])
            SKUS2.append(df.values[i][8])
            HSCODES2.append(df.values[i][9])
            COO2.append(df.values[i][10])
            INFVAL2.append(df.values[i][11])
            LINKVAL2.append(0)
            LINKS2.append(requrl)
            ETAT2.append("出现情况5.对应链接为空或者网站被墙")
            print("出现情况5.链接无效或者网站被墙")





###################################################
###################################################
###################################################
#################        BOHM
class BOHM(Fournisseur):
    def solution(self,df,i,requrl):

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
                    if (df.values[i][11] > 0):  # 情况一供应商无货但是我们网站显示有货
                        # 原始数据插入
                        HANDLES.append(df.values[i][0])
                        TITLES.append(df.values[i][1])
                        OPTION1NAME.append(df.values[i][2])
                        OPTION1VALUE.append(df.values[i][3])
                        OPTION2NAME.append(df.values[i][4])
                        OPTION2VALUE.append(df.values[i][5])
                        OPTION3NAME.append(df.values[i][6])
                        OPTION3VALUE.append(df.values[i][7])
                        SKUS.append(df.values[i][8])
                        HSCODES.append(df.values[i][9])
                        COO.append(df.values[i][10])
                        INFVAL.append(df.values[i][11])

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
                        if (df.values[i][11] < 1):
                            HANDLES.append(df.values[i][0])
                            TITLES.append(df.values[i][1])
                            OPTION1NAME.append(df.values[i][2])
                            OPTION1VALUE.append(df.values[i][3])
                            OPTION2NAME.append(df.values[i][4])
                            OPTION2VALUE.append(df.values[i][5])
                            OPTION3NAME.append(df.values[i][6])
                            OPTION3VALUE.append(df.values[i][7])
                            SKUS.append(df.values[i][8])
                            HSCODES.append(df.values[i][9])
                            COO.append(df.values[i][10])
                            INFVAL.append(df.values[i][11])

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

                        if (p_num < 2 and df.values[i][11] > 0):  # 小于2的情况，视为无货，但是我们网站显示有货
                            # 情况三，货源为1但是我们网站显示充足
                            HANDLES.append(df.values[i][0])
                            TITLES.append(df.values[i][1])
                            OPTION1NAME.append(df.values[i][2])
                            OPTION1VALUE.append(df.values[i][3])
                            OPTION2NAME.append(df.values[i][4])
                            OPTION2VALUE.append(df.values[i][5])
                            OPTION3NAME.append(df.values[i][6])
                            OPTION3VALUE.append(df.values[i][7])
                            SKUS.append(rowsku = df.values[i][8])
                            HSCODES.append(df.values[i][9])
                            COO.append(df.values[i][10])
                            INFVAL.append(df.values[i][11])

                            # 我们自己加的数据
                            LINKS.append(requrl)
                            LINKVAL.append(0)
                            ETAT.append("供应商货只剩一个但是我们网站显示有货")
                            print("情况三 货源为1但是我们网站显示充足")

                        elif (p_num >= 2 and df.values[i][11] < 1):
                            # 情况4，网站虽然警报但是有货，我们显示无货
                            HANDLES.append(df.values[i][0])
                            TITLES.append(df.values[i][1])
                            OPTION1NAME.append(df.values[i][2])
                            OPTION1VALUE.append(df.values[i][3])
                            OPTION2NAME.append(df.values[i][4])
                            OPTION2VALUE.append(df.values[i][5])
                            OPTION3NAME.append(df.values[i][6])
                            OPTION3VALUE.append(df.values[i][7])
                            SKUS.append(df.values[i][8])
                            HSCODES.append(df.values[i][9])
                            COO.append(df.values[i][10])
                            INFVAL.append(df.values[i][11])

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
            SKUS2.append(df.values[i][8])
            HSCODES2.append(df.values[i][9])
            COO2.append(df.values[i][10])
            INFVAL2.append(df.values[i][11])
            LINKVAL2.append(0)
            LINKS2.append(requrl)
            ETAT2.append("出现情况5,对应链接为空或者网站被墙")
            print("出现情况5,链接无效或者网站被墙")



 #############数据集合
def getres():
    dfresult = DataFrame({'Handle':HANDLES,'Title':TITLES,'Option1 Name':OPTION1NAME,'Option1 Value':OPTION1VALUE,'Option2 Name':OPTION2NAME,'Option2 Value':OPTION2VALUE,'Option3 Name':OPTION3NAME,'Option3 Value':OPTION3VALUE,'SKU':SKUS,'HS Code':HSCODES,'COO':COO,'INFINITUS CIFA':INFVAL,'SKU_URL':LINKS,'实际存货':LINKVAL,'状态':ETAT})
    return dfresult


def geterrorlog():
    dferrorlog = DataFrame({'Handle':HANDLES2,'Title':TITLES2,'Option1 Name':OPTION1NAME2,'Option1 Value':OPTION1VALUE2,'Option2 Name':OPTION2NAME2,'Option2 Value':OPTION2VALUE2,'Option3 Name':OPTION3NAME2,'Option3 Value':OPTION3VALUE2,'SKU':SKUS2,'HS Code':HSCODES2,'COO':COO2,'INFINITUS CIFA':INFVAL2,'SKU_URL':LINKS2,'存货情况':LINKVAL2,'状态':ETAT2})
    return dferrorlog

       