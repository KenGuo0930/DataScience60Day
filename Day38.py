# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 16:34:21 2021

@author: 郭奕志
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


from IPython.display import display
from IPython.display import display_html

# def display_side_by_side(*args):
#     html_str=''
#     for df in args:
#         html_str+=df.to_html()
#     display_html(html_str.replace('table','table style="display:inline"'),raw=True)
    
df_train = pd.read_csv("Titanic_train.csv")
df_test = pd.read_csv("Titanic_test.csv")


"""
'Q1: 判斷 測試資料集和訓練資料集"欄位"變數是否有差異性?
"""
print(df_test.columns)
print(df_train.columns)
# Index(['PassengerId', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch',
#        'Ticket', 'Fare', 'Cabin', 'Embarked'],
#       dtype='object')
# Index(['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
#        'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],
#       dtype='object')
"""沒有差異性"""
print(df_train)
#      PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
# 0              1         0       3  ...   7.2500   NaN         S
# 1              2         1       1  ...  71.2833   C85         C
# 2              3         1       3  ...   7.9250   NaN         S
# 3              4         1       1  ...  53.1000  C123         S
# 4              5         0       3  ...   8.0500   NaN         S
# ..           ...       ...     ...  ...      ...   ...       ...
# 886          887         0       2  ...  13.0000   NaN         S
# 887          888         1       1  ...  30.0000   B42         S
# 888          889         0       3  ...  23.4500   NaN         S
# 889          890         1       1  ...  30.0000  C148         C
# 890          891         0       3  ...   7.7500   NaN         Q

# [891 rows x 12 columns]
print(df_test)
#      PassengerId  Pclass  ... Cabin Embarked
# 0            892       3  ...   NaN        Q
# 1            893       3  ...   NaN        S
# 2            894       2  ...   NaN        Q
# 3            895       3  ...   NaN        S
# 4            896       3  ...   NaN        S
# ..           ...     ...  ...   ...      ...
# 413         1305       3  ...   NaN        S
# 414         1306       1  ...  C105        C
# 415         1307       3  ...   NaN        S
# 416         1308       3  ...   NaN        S
# 417         1309       3  ...   NaN        C

# [418 rows x 11 columns]



nodup_df_train=df_train.drop_duplicates(subset=None, keep='first', inplace=False)

# =============================================================================
# # subset : column label or sequence of labels, optional
# #     Only consider certain columns for identifying duplicates, by
# #     default use all of the columns
# # keep : {'first', 'last', False}, default 'first'
# #     - ``first`` : Drop duplicates except for the first occurrence.
# #     - ``last`` : Drop duplicates except for the last occurrence.
# #     - False : Drop all duplicates.
# # inplace : boolean, default False
# #     Whether to drop duplicates in place or to return a copy
# =============================================================================


"""Q2: 測試資料集是否有遺失值?"""
    
#any：判斷一個tuple或者list是否全為空，0，False。如果全為空
# 0返回False；如果不全為空，則返回True。
# isnull():檢查空值，回傳布林值
print(df_test.isnull().any())

# [418 rows x 11 columns]
# PassengerId    False
# Pclass         False
# Name           False
# Sex            False
# Age             True
# SibSp          False
# Parch          False
# Ticket         False
# Fare            True
# Cabin           True
# Embarked       False
# dtype: bool


# 統計 data 裡有空值的變數個數

print(df_test.isnull().any().sum())
# PassengerId    False
# Pclass         False
# Name           False
# Sex            False
# Age             True
# SibSp          False
# Parch          False
# Ticket         False
# Fare            True
# Cabin           True
# Embarked       False
# dtype: bool
# 3

data = df_train.append(df_test)

print(data)
#      PassengerId  Survived  Pclass  ...      Fare Cabin  Embarked
# 0              1       0.0       3  ...    7.2500   NaN         S
# 1              2       1.0       1  ...   71.2833   C85         C
# 2              3       1.0       3  ...    7.9250   NaN         S
# 3              4       1.0       1  ...   53.1000  C123         S
# 4              5       0.0       3  ...    8.0500   NaN         S
# ..           ...       ...     ...  ...       ...   ...       ...
# 413         1305       NaN       3  ...    8.0500   NaN         S
# 414         1306       NaN       1  ...  108.9000  C105         C
# 415         1307       NaN       3  ...    7.2500   NaN         S
# 416         1308       NaN       3  ...    8.0500   NaN         S
# 417         1309       NaN       3  ...   22.3583   NaN         C

# [1309 rows x 12 columns]

print(' 合併資料遺失值個數 = ',data['Cabin'].isnull().sum())
#  #   Column       Non-Null Count  Dtype  
# ---  ------       --------------  -----  
#  0   PassengerId  1309 non-null   int64  
#  1   Survived     891 non-null    float64
#  2   Pclass       1309 non-null   int64  
#  3   Name         1309 non-null   object 
#  4   Sex          1309 non-null   object 
#  5   Age          1046 non-null   float64
#  6   SibSp        1309 non-null   int64  
#  7   Parch        1309 non-null   int64  
#  8   Ticket       1309 non-null   object 
#  9   Fare         1308 non-null   float64
#  10  Cabin        295 non-null    object 
#  11  Embarked     1307 non-null   object 
# dtypes: float64(3), int64(4), object(5)
# memory usage: 132.9+ KB
# None
# 合併資料遺失值個數 = 1014


#* 方法1:遺失的屬於另一類。 
print(data['Cabin'].head(10))
# 0     NaN
# 1     C85
# 2     NaN
# 3    C123
# 4     NaN
# 5     NaN
# 6     E46
# 7     NaN
# 8     NaN
# 9     NaN
data["Cabin"] = data['Cabin'].apply(lambda x : str(x) if not pd.isnull(x) else 'NoCabin')
print(data["Cabin"])
# Name: Cabin, dtype: object
# 0      NoCabin
# 1            C
# 2      NoCabin
# 3            C
# 4      NoCabin
  
# 413    NoCabin
# 414          C
# 415    NoCabin
# 416    NoCabin
# 417    NoCabin
data["Cabin"].unique()
# pandas.unique(values)
# Parameters:	values : 1d array-like
# Returns:	    unique values.

# If the input is an Index, the return is an Index
# If the input is a Categorical dtype, the return is a Categorical
# If the input is a Series/ndarray, the return will be an ndarray

# 挑整後的 Cabin 觀察遺失的樣態
sns.countplot(data['Cabin'], hue=data['Survived'])


#數值計算
print(data[['Cabin', 'Survived']].groupby(['Cabin'], as_index=False).mean().sort_values(by='Survived', ascending=False))
#      Cabin  Survived
# 143    D56       1.0
# 149    E12       1.0
# 121    D17       1.0
# 122    D19       1.0
# 77    C148       1.0
# ..     ...       ...
# 166    E52       NaN
# 168    E60       NaN
# 174      F       NaN
# 175  F E46       NaN
# 176  F E57       NaN

# [187 rows x 2 columns]
















