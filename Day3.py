# -*- coding: utf-8 -*-
"""
正常的人耳能夠聽到最微弱的聲音叫作「聽覺閾」為 20 個微巴斯卡 (縮寫為 μPa) 
以聲壓 20μPa 定義為 0 分貝，表示 V0 為 20μPa，其餘聲壓為 V1(微巴斯卡)
例如將 V1 帶入 200μPa，V0 為 20μPa，可以得到 20GdB。
"""
import numpy as np

#1.正常的談話的聲壓為20000微巴斯卡，請問多少分貝?
v0 = 20*10**-6
v1 = 20000*10**-6#(μ=10^-6)
Gdb = 20*np.log10(np.divide(v1, v0))
print(' answer1 Gdb = ',Gdb)


#2.30分貝的聲壓會是50分貝的幾倍?
#[db = 20*log10(V1/V0)]→[db/20 = log10(V1/V0)]→[10^(db/20) = V1/V0]→[V1 = 10^(db/20)*v0] 
db_30 = 30
db_50 = 50
V_30 = 10**(db_30/20)*v0
V_50 = 10**(db_50/20)*v0

print('\n','answer2 gain = ',V_30/V_50)

'''2021/3/22 作業更新
題目
name_list = ['小明','小華','小菁','小美','小張','John','Mark','Tom']
sex_list = ['boy','boy','girl','girl','boy','boy','boy','boy']
weight_list = [67.5,75.3,50.1,45.5,80.8,90.4,78.4,70.7]
rank_list = [8,1,5,4,7,6,2,3]
myopia_list = [True,True,False,False,True,True,False,False]

(1) 將上列list依照['name', 'sex', 'weight', 'rank', 'myopia']順序擺入array，
    並且資料型態順序擺入[Unicode,Unicode,float,int,boolean]
(2)呈上題，將array中體重(weight)數據集取出算出全部平均體重
(3)呈上題，進一步算出男生(sex欄位是boy)平均體重、女生(sex欄位是girl)平均體重
[簡答題] 請比較 np.zeros 和 np.empty 產生出來的陣列有何差異？為什麼要設計兩種方法？
在不用「整數亂數方法」的限制下，如何將包含小數的轉換整數？請將給定的 a 陣列當中的元素變成去掉小數變成整數。
承上題，怎樣可以限制整數的範圍介於 m - n 之間？請將給定的 a 陣列當中的元素的範圍調整成 m - n 之間。

'''

#(1) 將上列list依照['name', 'sex', 'weight', 'rank', 'myopia']順序擺入array，
    #並且資料型態順序擺入[Unicode,Unicode,float,int,boolean]

name = ['小明','小華','小菁','小美','小張','John','Mark','Tom']
sex = ['boy','boy','girl','girl','boy','boy','boy','boy']
weight = [67.5,75.3,50.1,45.5,80.8,90.4,78.4,70.7]
rank = [8,1,5,4,7,6,2,3]
myopia = [True,True,False,False,True,True,False,False]

answer1_array= {'names':('name', 'sex', 'weight', 'rank', 'myopia'), 'formats':('U8','U8','f4','i4','?')}
answer1 = np.zeros(8,answer1_array)
answer1['name'] = name
answer1['sex'] = sex
answer1['weight'] = weight
answer1['rank'] = rank
answer1['myopia'] = myopia
print(answer1)

#(2)呈上題，將array中體重(weight)數據集取出算出全部平均體重
print(' Weight mean = ',np.mean(answer1['weight']))

#(3)呈上題，進一步算出男生(sex欄位是boy)平均體重、女生(sex欄位是girl)平均體重
boy_index = np.where(answer1['sex']=='boy')
print(' Weight mean of boy = ',np.mean(answer1['weight'][boy_index]))

girl_index = np.where(answer1['sex']!='boy')
print(' Weight mean of girl = ',np.mean(answer1['weight'][girl_index]))