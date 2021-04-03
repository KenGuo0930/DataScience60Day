# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 22:23:49 2021

@author: 郭奕志
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# =============================================================================
# 多組數據
# =============================================================================
x = np.arange(0,1080)
y =np.cos(x * np.pi / 180.0)
plt.plot(x,y,color = 'r') 

#設定圖的範圍, 不設的話，系統會自行決定
plt.xlim(-30,390)
plt.ylim(-1.5,1.5)

# 照需要寫入 x 軸和 y 軸的 label 以及 title
plt.xlabel("x-axis") 
plt.ylabel("y-axis") 
plt.title("The Title")
plt.savefig("cos wave.png",dpi=300,format="png")