# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 21:02:06 2021

@author: 郭奕志
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
import seaborn as sns
from scipy import stats
import math 
# import statistics
df_train = pd.read_csv('Titanic_train.csv') 


print(df_train['Fare'].mean()) 
print(df_train['Fare'].std()) 
# 32.2042079685746
# 49.693428597180905


# 連續型用分布圖行來看
g = sns.FacetGrid(df_train, col='Survived')
g.map(sns.distplot, 'Fare', kde=False)#distplot 分佈圖



print(df_train['Fare'].describe()) 
# count    891.000000
# mean      32.204208
# std       49.693429
# min        0.000000
# 25%        7.910400
# 50%       14.454200
# 75%       31.000000
# max      512.329200
# Name: Fare, dtype: float64

# =============================================================================
# 創建一個函數，計算在這個資料中， ys:資料，times : 幾倍標準差，找出在這樣條件下的異常值。
# =============================================================================
def outliers_z_score(ys,times):
    mean = np.mean(ys)
    std = np.std(ys)
    z_scores = [(i - mean) / std for i in ys]
    return np.where(np.abs(z_scores) > times)
out_index=outliers_z_score(df_train['Fare'],3)
print(out_index[0])
# [ 27  88 118 258 299 311 341 377 380 438 527 557 679 689 700 716 730 737
#  742 779]
print("用第二種方法的找出的 outlier 有哪些?")
print(df_train.loc[out_index[0],'Fare'])
# 27     263.0000
# 88     263.0000
# 118    247.5208
# 258    512.3292
# 299    247.5208
# 311    262.3750
# 341    263.0000
# 377    211.5000
# 380    227.5250
# 438    263.0000
# 527    221.7792
# 557    227.5250
# 679    512.3292
# 689    211.3375
# 700    227.5250
# 716    227.5250
# 730    211.3375
# 737    512.3292
# 742    262.3750
# 779    211.3375
