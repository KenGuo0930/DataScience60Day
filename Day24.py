# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 00:10:52 2021

@author: 郭奕志
"""
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


df = sns.load_dataset('titanic')
df.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 891 entries, 0 to 890
# Data columns (total 15 columns):
#  #   Column       Non-Null Count  Dtype   
# ---  ------       --------------  -----   
#  0   survived     891 non-null    int64   
#  1   pclass       891 non-null    int64   
#  2   sex          891 non-null    object  
#  3   age          714 non-null    float64 
#  4   sibsp        891 non-null    int64   
#  5   parch        891 non-null    int64   
#  6   fare         891 non-null    float64 
#  7   embarked     889 non-null    object  
#  8   class        891 non-null    category
#  9   who          891 non-null    object  
#  10  adult_male   891 non-null    bool    
#  11  deck         203 non-null    category
#  12  embark_town  889 non-null    object  
#  13  alive        891 non-null    object  
#  14  alone        891 non-null    bool    
# dtypes: bool(2), category(2), float64(2), int64(4), object(5)
# memory usage: 80.6+ KB
print(df)
#      survived  pclass     sex   age  ...  deck  embark_town  alive  alone
# 0           0       3    male  22.0  ...   NaN  Southampton     no  False
# 1           1       1  female  38.0  ...     C    Cherbourg    yes  False
# 2           1       3  female  26.0  ...   NaN  Southampton    yes   True
# 3           1       1  female  35.0  ...     C  Southampton    yes  False
# 4           0       3    male  35.0  ...   NaN  Southampton     no   True
# ..        ...     ...     ...   ...  ...   ...          ...    ...    ...
# 886         0       2    male  27.0  ...   NaN  Southampton     no   True
# 887         1       1  female  19.0  ...     B  Southampton    yes   True
# 888         0       3  female   NaN  ...   NaN  Southampton     no  False
# 889         1       1    male  26.0  ...     C    Cherbourg    yes   True
# 890         0       3    male  32.0  ...   NaN   Queenstown     no   True

# (1) 做條形圖
sns.barplot(x = "sex", y = "survived", hue = "class", data = df)


# (2) 異常值落點分析
df1 = sns.load_dataset('tips')
df1.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 244 entries, 0 to 243
# Data columns (total 7 columns):
#  #   Column      Non-Null Count  Dtype   
# ---  ------      --------------  -----   
#  0   total_bill  244 non-null    float64 
#  1   tip         244 non-null    float64 
#  2   sex         244 non-null    category
#  3   smoker      244 non-null    category
#  4   day         244 non-null    category
#  5   time        244 non-null    category
#  6   size        244 non-null    int64   
# dtypes: category(4), float64(2), int64(1)
# memory usage: 7.3 KB
sns.boxplot(x='day', y='tip', data=df1)
sns.stripplot(x='day', y='tip', data=df1, jitter=True)
plt.show()

























