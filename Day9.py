# -*- coding: utf-8 -*-
"""
作業
"""

import pandas as pd
import numpy as np



# 請建立類似提供結果的 DataFrame：
#    Apples  Bananas
# 0      30       21

#             Apples  Bananas
# 2017 Sales      35       21
# 2018 Sales      41       34

df = pd.DataFrame([[35,41],[41,34]],index = ['2017 sales ','2018 sale'],columns = ['Apples' ,'Bananas',])
print(df)


# 請問如果現在有一個 DataFrame 如下，請問資料在 Python 中可能長怎樣？

#      city  visitor weekday
# 0  Austin      139     Sun
# 1  Dallas      237     Sun
# 2  Austin      326     Mon
# 3  Dallas      456     Mon

df = pd.DataFrame([['Austin',139,'Sun'],
                   ['Dallas',237,'Sun'],
                   ['Austin',326,'Mon'],
                   ['Dallas',456,'Mon'] ],columns = ['city' ,'visitor','weekday'])
print(df)

# 假設你想知道每個 weekday 的平均 visitor 數量，可以怎麼做？
# print('visitor = \n',df['visitor'])
# print('Sun sum = ', df.visitor[df.weekday == 'Sun'].sum())
# print('Mon sum = ', df.visitor[df.weekday == 'Mon'].sum())
# print('number of Sun = ',df.visitor[df.weekday == 'Sun'].count())
# print('number of Mon = ',df.visitor[df.weekday == 'Mon'].count())
# print('Sun mean = ', df.visitor[df.weekday == 'Sun'].sum() / df.visitor[df.weekday == 'Sun'].count())
# print('Mon mean  = ', df.visitor[df.weekday == 'Mon'].sum() / df.visitor[df.weekday == 'Mon'].count())

print('Sun mean = ',df.visitor[df.weekday == 'Sun'].mean())
print('Mon mean = ',df.visitor[df.weekday == 'Mon'].mean())