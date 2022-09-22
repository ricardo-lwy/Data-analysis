


####################
####################
############21/09/2022 by Weiyi LIU
########22/09/2022 更新: 编写了一个小型解决方案库










# #################
# 在运行程序前先清除所有变量   
#reset -f    # 相当于 clearall
##import subprocess as sp
##tmp = sp.call('reset',shell=True)
#

#clear    # 清空命令窗口



#######开源工具库
#from cmath import inf
from multiprocessing.dummy import Array
#from tkinter.font import NORMAL
#from bs4 import BeautifulSoup  # this module helps in web scrapping.
#import requests  # this module helps us to download a web page 
#import urllib.request
import pandas as pd
#from pandas.core.frame import DataFrame
#from openpyxl.writer.excel import ExcelWriter
#from lxml import etree
#from ast import Break
#from http.client import NOT_FOUND
import re
from time import sleep





#########引用设计的库中的内容。包含了sku对应链接以及不同网站对应的不同爬取方法

#from solution_class import SATINE,BOHM
import skudata
import solution_class
from solution_class import BOHM,SATINE,typeError






########start
df = pd.read_excel('DATA.xlsx', sheet_name='Feuille1')

###复查
#df = pd.read_excel('errorlog1.xlsx', sheet_name='Sheet1')




# 一共有多少行
sumline = len(df)



# print(data)
print(sumline+1)




# 休眠时判定
grabcount = 1

####读取数据流
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
        #error方法
        print("警报！,未找到", rowsku, "对应的SKU")
        print("调用error方法")
        typeError.soulution(df,i)
        print("调用完毕")
    # 没找到这个Sku，因此我们要将他添加到错误日志中
       
    else:
        requrl = skudata.all_url[indexnum]
        print("成功找到", rowsku, "名字为：",
              skudata.all_sku[indexnum], "对应的url为:", requrl)
        # 找到索引，开始爬虫任务；




            #########20/09/2022更新：需要找到解释器
            ######22/09/2022: 已经找到

        #bohm方法
        #22/09/2022 这里还可以再次建立无序表进行优化，但是由于目前只有两个供应商因此直接if更快
        if(len(re.findall("BM",rowsku))>0):
            print("调用bohm方法")
            BOHM().solution(df,i,requrl)
            print("调用完毕")
        #satine方法
        elif(len(re.findall("ST",rowsku))>0):
            print("调用satine方法")
            SATINE().solution(df,i,requrl)
            print("调用完毕")
            




    # 生成结果界面和错误日志
    ########################################################################
    #########################################################################
    ###########################################################################

dfresult=solution_class.getres()
dferrorlog=solution_class.geterrorlog()


####交互命令
print("完成运行\n")
print("输入： dfresult 查看库存不匹配的情况\n")
print("输入： dferrorlog 查看错误日志\n")
print("输入： reset -f 或者点击上方的restart 清除缓存数据（便于下次使用）\n")
print("输入： dfresult.to_excel('文件名.xlsx',index = False)或者dferrorlog.to_excel('文件名.xlsx',index = False) 来进行excel导出 \n")

    #df_pm1.to_excel('',index = False)
    #########要想办法把第一行删掉
    ####,index = False




    #######################################
    # 写入代码暂时没有写，在控制台中进行控制会更加方便
    # 写入结果到excel，询问具体需求。
    # 19/09/2022 by Weiyi LIU


    ####21/09/2022写了个很蠢的方法把这两个综合了起来。后面要考虑拆出重复代码。
    #####就只是用正则来判断了一下sku的属性：（




##SATINE().solution(url)
#satineobject.solution(url)





