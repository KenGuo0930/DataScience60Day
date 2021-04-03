# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 23:12:19 2021

@author: 郭奕志
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")
fmri = sns.load_dataset("fmri")
print(tips)
#      total_bill   tip     sex smoker   day    time  size
# 0         16.99  1.01  Female     No   Sun  Dinner     2
# 1         10.34  1.66    Male     No   Sun  Dinner     3
# 2         21.01  3.50    Male     No   Sun  Dinner     3
# 3         23.68  3.31    Male     No   Sun  Dinner     2
# 4         24.59  3.61  Female     No   Sun  Dinner     4
# ..          ...   ...     ...    ...   ...     ...   ...
# 239       29.03  5.92    Male     No   Sat  Dinner     3
# 240       27.18  2.00  Female    Yes   Sat  Dinner     2
# 241       22.67  2.00    Male    Yes   Sat  Dinner     2
# 242       17.82  1.75    Male     No   Sat  Dinner     2
# 243       18.78  3.00  Female     No  Thur  Dinner     2

# [244 rows x 7 columns]



print(fmri)
#      subject  timepoint event    region    signal
# 0        s13         18  stim  parietal -0.017552
# 1         s5         14  stim  parietal -0.080883
# 2        s12         18  stim  parietal -0.081033
# 3        s11         18  stim  parietal -0.046134
# 4        s10         18  stim  parietal -0.037970
#      ...        ...   ...       ...       ...
# 1059      s0          8   cue   frontal  0.018165
# 1060     s13          7   cue   frontal -0.029130
# 1061     s12          7   cue   frontal -0.004939
# 1062     s11          7   cue   frontal -0.025367
# 1063      s0          0   cue  parietal -0.006899

# [1064 rows x 5 columns




sns.set_style('whitegrid')
print(sns.relplot(x="total_bill", y="tip", hue="sex", style="time", data=tips))
print(sns.relplot(x="timepoint", y="signal", hue="event", style="region", data=fmri))

# =============================================================================
# 以常用的散點圖曲線圖來表示變數之間的關係： sns.relplot()
# 關注的是統計量之間的關係。 x，y 數值型數據，關注兩個數值變數之間的關係
# =============================================================================
# relplot() - relationship plot

# replot 常用參數

# hue： 在同一維度上，用顏色區分不同數據

# style： 在同一維度上， 用線的不同表現形式區分， 如 點線， 虛線等

# size： 控制點大小或者線條粗細 

# kind： 繪製圖的型態. kind= 'scatter'（散點圖, 預設值） kind='line' (線圖)，可以通過參數 ci：（confidence interval）參數，來控制陰影部分


