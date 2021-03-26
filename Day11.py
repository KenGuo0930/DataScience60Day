# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 19:43:11 2021

@author: 郭奕志
"""
import numpy as np 
import pandas as pd


#1.  根據題目給的 DataFrame 完成下列操作：
# 2- 計算每個不同種類 animal 的 age 的平均數

# 4- 將 priority 欄位中的 yes 和 no 字串，換成是布林值 的 True 和 False
data = {
    'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
    'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
    'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(data, index=labels)
#  animal  age  visits priority
# a    cat  2.5       1      yes
# b    cat  3.0       3      yes
# c  snake  0.5       2       no
# d    dog  NaN       3      yes
# e    dog  5.0       2       no
# f    cat  2.0       3       no
# g  snake  4.5       1       no
# h    cat  NaN       1      yes
# i    dog  7.0       2       no
# j    dog  3.0       1       no

# 1- 計算每個不同種類 animal 的 age 的平均數
print(df.groupby(['animal']).mean())
#         age  visits
# animal             
# cat     2.5     2.0
# dog     5.0     2.0
# snake   2.5     1.5



# 3- 將資料依照 Age 欄位由小到大排序，再依照 visits 欄位由大到小排序
df1 = df.sort_values(by=['age'])

# animal  age  visits priority
# c  snake  0.5       2       no
# f    cat  2.0       3       no
# a    cat  2.5       1      yes
# b    cat  3.0       3      yes
# j    dog  3.0       1       no
# g  snake  4.5       1       no
# e    dog  5.0       2       no
# i    dog  7.0       2       no
# d    dog  NaN       3      yes
# h    cat  NaN       1      yes

df2 = df1.sort_values(by=['visits'])
print(df2)
#   animal  age  visits priority
# a    cat  2.5       1      yes
# j    dog  3.0       1       no
# g  snake  4.5       1       no
# h    cat  NaN       1      yes
# c  snake  0.5       2       no
# e    dog  5.0       2       no
# i    dog  7.0       2       no
# f    cat  2.0       3       no
# b    cat  3.0       3      yes
# d    dog  NaN       3      yes

df["priority"] = df["priority"].str.replace("yes","True")
df["priority"] = df["priority"].str.replace("no","False")
print(df.head())
#   animal  age  visits priority
# a    cat  2.5       1     True
# b    cat  3.0       3     True
# c  snake  0.5       2    False
# d    dog  NaN       3     True
# e    dog  5.0       2    False


#2.  一個包含兩個欄位的 DataFrame，將每個數字減去
df1 = pd.DataFrame(np.random.random(size=(5, 3)))
#           0         1         2
# 0  0.756203  0.198173  0.610786
# 1  0.969013  0.848438  0.907106
# 2  0.360219  0.976758  0.533840
# 3  0.239669  0.795646  0.217284
# 4  0.253962  0.774011  0.432123


# 1 該欄位的平均數
a = df1.mean()
# 0    0.691548
# 1    0.401544
# 2    0.454095



# 2 該筆資料平均數

#3. 承上題，請問：
#1 哪一比的資料總合最小
#1
#2 哪一欄位的資料總合最小
#2