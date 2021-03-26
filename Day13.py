# -*- coding: utf-8 -*-
"""
作業
"""
import numpy as np 
import pandas as pd 

# 1. 請接下列資料依照指定規則做合併：
df1 = pd.DataFrame({
    'fruit': ['apple', 'banana', 'orange'] * 3,
    'weight': ['high', 'medium', 'low'] * 3,
    'price': np.random.randint(0, 15, 9)})
#     fruit  weight  price
# 0   apple    high      3
# 1  banana  medium      5
# 2  orange     low      4
# 3   apple    high     14
# 4  banana  medium      4
# 5  orange     low      8
# 6   apple    high      9
# 7  banana  medium      0
# 8  orange     low     11

df2 = pd.DataFrame({
    'fruit': ['apple', 'orange', 'pine'] * 2,
    'weight': ['high', 'low'] * 3,
    'price': np.random.randint(0, 15, 6)})
#     fruit weight  price
# 0   apple   high      2
# 1  orange    low      4
# 2    pine   high     12
# 3   apple    low      6
# 4  orange   high     12
# 5    pine    low      8
print(pd.merge(df1, df2, on='fruit'))
#      fruit weight_x  price_x weight_y  price_y
# 0    apple     high       11     high        9
# 1    apple     high       11      low        6
# 2    apple     high        1     high        9
# 3    apple     high        1      low        6
# 4    apple     high        3     high        9
# 5    apple     high        3      low        6
# 6   orange      low        8      low        1
# 7   orange      low        8     high        9
# 8   orange      low        9      low        1
# 9   orange      low        9     high        9
# 10  orange      low        4      low        1
# 11  orange      low        4     high        9



# 2.依照 index 索引做合併

# print(df1.join(df2))
"""
[簡答題]
"""
# =============================================================================
# 2.  承上題，請問為什麼依照 merge 合併後有些資料不見了？
#  因為 merge 有預設的方法是兩邊同時存在才會合併，只存在一邊的資料就不見了
# =============================================================================



# =============================================================================
# 3.承上題，請問為什麼依照 index 合併會發生錯誤？請用程式解決。
# 因為原本的欄位重複，導致無法正確合併。
# =============================================================================


print(df1.join(df2, lsuffix=' df1', rsuffix=' df2'))


# df1 :
#     fruit  weight  price
# 0   apple    high      3
# 1  banana  medium      5
# 2  orange     low      4
# 3   apple    high     14
# 4  banana  medium      4
# 5  orange     low      8
# 6   apple    high      9
# 7  banana  medium      0
# 8  orange     low     11

# df2:
#     fruit weight  price
# 0   apple   high      2
# 1  orange    low      4
# 2    pine   high     12
# 3   apple    low      6
# 4  orange   high     12
# 5    pine    low      8

# df1.join(df2, lsuffix=' df1', rsuffix=' df2'):
#   fruit df1 weight df1  price df1 fruit df2 weight df2  price df2
# 0     apple       high          5     apple       high       14.0
# 1    banana     medium          1    orange        low        4.0
# 2    orange        low          7      pine       high       14.0
# 3     apple       high          4     apple        low        6.0
# 4    banana     medium          2    orange       high        0.0
# 5    orange        low          6      pine        low        4.0
# 6     apple       high         10       NaN        NaN        NaN
# 7    banana     medium         11       NaN        NaN        NaN
# 8    orange        low         11       NaN        NaN        NaN





