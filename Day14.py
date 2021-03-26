# -*- coding: utf-8 -*-
"""
作業
"""
import numpy as np
import pandas as pd
#1. 讀取資料夾中 boston.csv 讀取其欄位 CHAS、NOX、RM，輸出成.xlsx檔案
# data = pd.read_csv('boston.csv',usecols = ['CHAS','NOX','RM'])
# data.to_csv('boston.xls') 

# [簡答題] 比較下列兩個讀入的 df 有什麼不同？為什麼造成的？

df1 = pd.read_csv('https://raw.githubusercontent.com/dataoptimal/posts/master/data%20cleaning%20with%20python%20and%20pandas/property%20data.csv')
print(df1)

#            PID  ST_NUM     ST_NAME OWN_OCCUPIED NUM_BEDROOMS NUM_BATH SQ_FT
# 0  100001000.0   104.0      PUTNAM            Y            3        1  1000
# 1  100002000.0   197.0   LEXINGTON            N            3      1.5    --
# 2  100003000.0     NaN   LEXINGTON            N          NaN        1   850
# 3  100004000.0   201.0    BERKELEY           12            1      NaN   700
# 4          NaN   203.0    BERKELEY            Y            3        2  1600
# 5  100006000.0   207.0    BERKELEY            Y          NaN        1   800
# 6  100007000.0     NaN  WASHINGTON          NaN            2   HURLEY   950
# 7  100008000.0   213.0     TREMONT            Y            1        1   NaN
# 8  100009000.0   215.0     TREMONT            Y           na        2  1800

df2 = pd.read_csv(
    'https://raw.githubusercontent.com/dataoptimal/posts/master/data%20cleaning%20with%20python%20and%20pandas/property%20data.csv',
    keep_default_na=True,
    na_values=['na', '--'])
print(df2)

#            PID  ST_NUM     ST_NAME OWN_OCCUPIED  NUM_BEDROOMS NUM_BATH   SQ_FT
# 0  100001000.0   104.0      PUTNAM            Y           3.0        1  1000.0
# 1  100002000.0   197.0   LEXINGTON            N           3.0      1.5     NaN
# 2  100003000.0     NaN   LEXINGTON            N           NaN        1   850.0
# 3  100004000.0   201.0    BERKELEY           12           1.0      NaN   700.0
# 4          NaN   203.0    BERKELEY            Y           3.0        2  1600.0
# 5  100006000.0   207.0    BERKELEY            Y           NaN        1   800.0
# 6  100007000.0     NaN  WASHINGTON          NaN           2.0   HURLEY   950.0
# 7  100008000.0   213.0     TREMONT            Y           1.0        1     NaN
# 8  100009000.0   215.0     TREMONT            Y           NaN        2  1800.0


# 會預設的 NaN 值做判斷，但 na、-- 不在預設的範圍內所以沒有被轉換。


# 請將 Dcard API 取得所有的看板資訊轉換成 DataFrame，並且依照熱門程度排序後存成一個 csv 的檔案。
import requests
r = requests.get('https://www.dcard.tw/_api/forums')
response = r.text

import json
data = json.loads(response)

# print(data)

df = pd.DataFrame(data)
df = df.sort_values('subscriptionCount', ascending=False)
df.to_csv('./dcard.csv')
print(df)


#                                        id  ...                                               logo
# 373  1ce3ebca-8701-42d5-b14c-076fc629bc8e  ...  {'url': 'https://megapx-assets.dcard.tw/images...
# 228  42851318-b9e2-4a75-8a05-9fe180becefe  ...  {'url': 'https://megapx-assets.dcard.tw/images...
# 224  be1a095b-175e-4523-9e06-66a05d939676  ...  {'url': 'https://megapx-assets.dcard.tw/images...
# 217  cbd5285f-3cba-4bfc-86d0-1ab52d201459  ...  {'url': 'https://megapx-assets.dcard.tw/images...
# 270  4c6964fc-8b39-4480-a844-847f09e4e09d  ...  {'url': 'https://megapx-assets.dcard.tw/images...
# ..                                    ...  ...                                                ...
# 208  1150ae79-6e67-46f2-bfec-74f8c365a4a1  ...  {'url': 'https://megapx-assets.dcard.tw/images...
# 207  019f0994-375e-479a-9b08-1b8addb64cc3  ...  {'url': 'https://megapx-assets.dcard.tw/images...
# 480  6e906a60-b8c9-401d-9183-f0bd376791b2  ...  {'url': 'https://megapx-assets.dcard.tw/images...
# 172  9e2ea80f-3342-4533-bb7a-d639e6c517e7  ...                                                NaN
# 209  36443e19-9334-42f4-b91e-95e601150f61  ...  {'url': 'https://megapx-assets.dcard.tw/images...

# [483 rows x 33 columns]