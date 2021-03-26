# -*- coding: utf-8 -*-
"""
作業
"""

import pandas as pd
import numpy as np



#1.畫出箱型圖，並判斷哪個欄位的中位數在300~400之間?
df = pd.read_csv("boston.csv")
df.boxplot()

#2. 畫出散佈圖 x='NOX', y='DIS' ，並說明這兩欄位有什麼關係?
df.plot.scatter(x='NOX', y='DIS')


