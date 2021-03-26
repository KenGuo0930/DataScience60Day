# -*- coding: utf-8 -*-
"""
作業
"""

import numpy as np 
import pandas as pd 

data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# 根據給定的 DataFrame 中取出索引為 3, 4, 8 的 animal 和 age 欄位。

df = pd.DataFrame(data, index=labels)
print('\n',df)

#   animal  age  visits priority
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

print('\n',df.loc[df.index[[3, 4, 8]], ['animal', 'age']])

df1 = pd.DataFrame([
    ['tom', 'mark', 'mary'],
    ['bob', 'alice', 'john']
    ])
print('\n',df1)
#      0      1     2
# 0  tom   mark  mary
# 1  bob  alice  john
print('\n',df1.applymap(lambda x: x.title()))