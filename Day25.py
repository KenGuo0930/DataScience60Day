# -*- coding: utf-8 -*-
"""
結合 Pandas 與 Matploglib 進行進階資料視覺化練習
"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

df_red = pd.read_csv("winequality_red.csv")
df_white = pd.read_csv("winequality_white.csv")
df_red["color"] = "R"
df_white["color"] = "W"
df_all=pd.concat([df_red,df_white],axis=0)
print(df_all.head())
#    fixed acidity  volatile acidity  citric acid  ...  alcohol  quality  color
# 0            7.4              0.70         0.00  ...      9.4        5      R
# 1            7.8              0.88         0.00  ...      9.8        5      R
# 2            7.8              0.76         0.04  ...      9.8        5      R
# 3           11.2              0.28         0.56  ...      9.8        6      R
# 4            7.4              0.70         0.00  ...      9.4        5      R

# [5 rows x 13 columns]

df_all.rename(columns={'fixed acidity': 'fixed_acidity','citric acid':'citric_acid',
                       'volatile acidity':'volatile_acidity','residual sugar':'residual_sugar',
                       'free sulfur dioxide':'free_sulfur_dioxide',
                       'total sulfur dioxide':'total_sulfur_dioxide'}, inplace=True)
# 檢查合併後的資料集
df_all.head()

#處理缺失值
df = pd.get_dummies(df_all, columns=["color"])
df_all.isnull().sum()
df_all.info()
<class 'pandas.core.frame.DataFrame'>
Int64Index: 6497 entries, 0 to 4897
Data columns (total 13 columns):
#  #   Column                Non-Null Count  Dtype  
# ---  ------                --------------  -----  
#  0   fixed_acidity         6497 non-null   float64
#  1   volatile_acidity      6497 non-null   float64
#  2   citric_acid           6497 non-null   float64
#  3   residual_sugar        6497 non-null   float64
#  4   chlorides             6497 non-null   float64
#  5   free_sulfur_dioxide   6497 non-null   float64
#  6   total_sulfur_dioxide  6497 non-null   float64
#  7   density               6497 non-null   float64
#  8   pH                    6497 non-null   float64
#  9   sulphates             6497 non-null   float64
#  10  alcohol               6497 non-null   float64
#  11  quality               6497 non-null   int64  
#  12  color                 6497 non-null   object 
# dtypes: float64(11), int64(1), object(1)
# memory usage: 710.6+ KB

#要瞭解數據集的統計摘要,即記錄數、平均值、標準差、最小值和最大值,我們使用描述()。
df_all.describe()
# 	fixed_acidity	volatile_acidity	citric_acid	residual_sugar	chlorides	free_sulfur_dioxide	total_sulfur_dioxide	density	pH	sulphates	alcohol	quality
# count	6497.000000	6497.000000	6497.000000	6497.000000	6497.000000	6497.000000	6497.000000	6497.000000	6497.000000	6497.000000	6497.000000	6497.000000
# mean	7.215307	0.339666	0.318633	5.443235	0.056034	30.525319	115.744574	0.994697	3.218501	0.531268	10.491801	5.818378
# std	1.296434	0.164636	0.145318	4.757804	0.035034	17.749400	56.521855	0.002999	0.160787	0.148806	1.192712	0.873255
# min	3.800000	0.080000	0.000000	0.600000	0.009000	1.000000	6.000000	0.987110	2.720000	0.220000	8.000000	3.000000
# 25%	6.400000	0.230000	0.250000	1.800000	0.038000	17.000000	77.000000	0.992340	3.110000	0.430000	9.500000	5.000000
# 50%	7.000000	0.290000	0.310000	3.000000	0.047000	29.000000	118.000000	0.994890	3.210000	0.510000	10.300000	6.000000
# 75%	7.700000	0.400000	0.390000	8.100000	0.065000	41.000000	156.000000	0.996990	3.320000	0.600000	11.300000	6.000000
# max	15.900000	1.580000	1.660000	65.800000	0.611000	289.000000	440.000000	1.038980	4.010000	2.000000	14.900000	9.000000

# 顯示所有數值數據。在垂直軸上計數,在水平軸上使用值範圍。hist 函數通過將所有屬性繪製在一起使操作變得簡單。
df_all.hist(bins=10, color='lightblue',edgecolor='blue',linewidth=1.0,
          xlabelsize=8, ylabelsize=8, grid=False)    

plt.tight_layout(rect=(0, 0, 1.2, 1.2))
# 作業(1):更改df_all.hist裡面bins的參數值, 看看資料分布的變化

x=6
df_all.hist(bins=x, color='lightblue',edgecolor='blue',linewidth=1.0,
          xlabelsize=8, ylabelsize=8, grid=False)  

plt.tight_layout(rect=(0, 0, 1.2, 1.2))


# 作業(2):延伸 作業(1), 更改df_all.hist裡面grid的參數值, 看看版面的變化, gird = True

x=6
df_all.hist(bins=x, color='lightblue',edgecolor='blue',linewidth=1.0,
          xlabelsize=8, ylabelsize=8, grid=True)  

plt.tight_layout(rect=(0, 0, 1.2, 1.2))

# 作業(3):更改 plt.tight_layout(rect=(x1, y1, x2, y2))

df_all.hist(bins=10, color='lightblue',edgecolor='blue',linewidth=1.0,
          xlabelsize=8, ylabelsize=8, grid=False)    

plt.tight_layout(rect=(0.5, 1, 2, 2))





