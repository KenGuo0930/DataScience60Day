# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 12:50:22 2021

@author: 郭奕志
"""

import pandas as pd

s = pd.Series([1, 2, 3])
print(s)
# 0    1
# 1    2
# 2    3
# dtype: int64
print(type(s))
# <class 'pandas.core.series.Series'>

df = pd.DataFrame([1, 2, 3])
print(df)
#     0
# 0  1
# 1  2
# 2  3
print(type(df))
# <class 'pandas.core.frame.DataFrame'>

df1 = pd.DataFrame([[1,2,3],
                    [4,5,6],
                    [7,8,9]])
print(df1)
#    0  1  2
# 0  1  2  3
# 1  4  5  6
# 2  7  8  9
print(type(df1))
# <class 'pandas.core.frame.DataFrame'>

print('\n','Series 其實就是 NumPy 的 Array 的加工品，所以 Array 有的屬性， Series 絕大部分都可延用： \n')
s = pd.Series([1, 2, 3])
print(s.shape) # (3, )
print(s.size) # 3
print(s.dtype) # int64

print('\n','DataFrame 也是 NumPy 的 Array 的加工品，所以 Array 有的屬性， DataFrame 一樣可以使用用 : \n')
df = pd.DataFrame([1, 2, 3])
print(df.shape) # (3, 1)
print(df.size) # 3
print(df.dtypes) 


"""
Seies、DataFrame 與 NdArray 的比較
DataFrame 代表的是用「資料」的角度去思考程式中的實踐應該長什麼樣子、應該要提供哪些方法，是以資料的觀點出發。
那你可以會問既然 Seies、DataFrame 都是由陣列所封裝而成的加工品，那為什麼不直接用陣列就好呢？
1.陣列當中所有資料型態必須相同
2.而 DataFrame 是由  Seies 所組成，也就說同一個欄位形態相同，欄位與欄位間可不相同
"""