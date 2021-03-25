# -*- coding: utf-8 -*-
"""
作業
"""
import pandas as pd 
import numpy as np
# 操作索引注意有分loc、iloc
# 合併資料方法concat、merge、join其中有參數可以調整inner或outer


# 1.簡答題] 請問下列四種不同的 DataFrame 選取結果有什麼差異？
# df.loc[ '2013-01-01', 'A'] 
# df.loc[ '2013-01-01', ['A', 'B'] ] 
# df.loc[ '2013-01-01':'2013-01-02', 'A' ] 
# df.loc[ '2013-01-01':'2013-01-05', 'A':'C'] 

"""
從index A 選取資料
從index A 、B選取資料
在2013-01-01':'2013-01-02 區間中選取index A 
在2013-01-01':'2013-01-05',選取 'A'至'C']
"""


# # 2.請根據提供的資料，選擇出下列的要求：
# # - select the first 3 rows.
# # - select the odd rows. (index = 1, 3, 5)
# # - select the last 2 columns.
# # - select the even columns. (index = 0, 2, 4)

# data = pd.read_csv('boston.csv')
# print(data[0:3])
# print(data.iloc[[1,3,5],])
# print(data[['key','CRIM']])#如果被挑選的欄位有多個的話，可以用兩層的方式做選取：
# print(data.iloc[[2,4,6],])




# 3.請根據提供的資料，選擇出下列的要求：
# - 1. filtered by first column > 20?
# - 2. filtered by first column + second column > 50
# - 3. filtered by first column < 30 or second column > 30
# - 4. filtered by total sum of row > 100

# df1 = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
# print(df1)
# df2 =df1[df1<20] 
# print(df2)
# df3 = pd.concat([df1,df2],axis=1)
# print(df3[df3>50])
# print(df1[df1>30]|df2[df2<30])


# 參考解答

# - 1. filtered by first column > 20?
df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
df.loc[df[0] > 20]
print(df[df[0] > 20])

# - 2. filtered by first column + second column > 50

df[df[0] + df[1] > 50]
print(df.loc[df[0] + df[1] > 50])

# - 3. filtered by first column < 30 or second column > 30

df[np.logical_or(df[0] < 30, df[1] > 30)]
print(df[(df[0] < 30) | (df[1] > 30)])

# - 4. filtered by total sum of row > 100

df[df[0] + df[1] + df[2] + df[3] > 100]
print(df[df.sum(axis=1) > 100])