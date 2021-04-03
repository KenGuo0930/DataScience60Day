# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 22:34:28 2021

@author: 郭奕志
"""

import matplotlib.pyplot as plt
import numpy as np 




# =============================================================================
# 條型圖：Bar Plots

# 長條圖主要用來呈現兩個維度的資料，一個為X軸另一個則為Y軸(當然這邊指的是二維的狀況，較為常見)
# 主要用來呈現兩個維度的資料
# 問題：嘗試通過添加紅色條形標籤重現右側的圖形。
# =============================================================================

# 決定底框
# plt.axes([0.1,0.1,.5,.5])
# #給定刻度
# plt.xticks([]), plt.yticks([])
# plt.text(0.1,0.1, 'axes([0.1,0.1,.5,.5])',ha='left',size=16,alpha=.5)

# #決定第二層框
# #決定底框
# plt.axes([0.3,0.3,.5,.5])
# #給定刻度, 若不給定值, 圖的周邊無文字
# #plt.xticks([]), plt.yticks([])
# plt.text(0.1,0.1, 'axes([0.3,0.3,.5,.5])',ha='left',size=16,alpha=.5)

# #決定第三層框
# plt.axes([0.5,0.5,.5,.5])
# #給定刻度
# #plt.xticks([]), plt.yticks([])
# plt.text(0.1,0.1, 'axes([0.5,0.5,.5,.5])',ha='left',size=16,alpha=.5)


# #決定第四層框
# plt.axes([0.7,0.7,.5,.5])
# plt.xticks([]), plt.yticks([])
# plt.text(0.1,0.1, 'axes([0.7,0.7,.5,.5])',ha='left',size=16,alpha=.5)

# '''
# plt.xticks([]), plt.yticks([]) 沒有指定內容會不顯示
# '''

# plt.show()



# =============================================================================
# 軸圖進階

# 但是可以將圖放置在圖中的任何位置。因此，如果要在較大的圖中放置較小的圖，則可以使用軸。
# 特別提醒：tick 刻度線定位器
# 問題：使用 tick
# =============================================================================

#配置12 組 Bar
n = 12 
X = np.arange(n)

  #給定數學運算式
Y1 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)
Y2 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)

#指定上半部繪製區域, 給定 Bar 顏色, 邊界顏色
plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
# +Y 指的是 XY 四象限的第一象限
# -Y 指的是 XY 四象限的第二象限


#在此coding
#指定下半部繪製區域, 給定 Bar 顏色, 邊界顏色
#顏色除了用色標外, 也可以用顏色文字描述, red: 紅色
plt.bar(X, -Y2, facecolor='red', edgecolor='black')


  #設定繪圖圖示區間
for x,y in zip(X,Y1):
    plt.text(x+0.4, y+0.05, '%.2f' % y, ha='center', va= 'bottom')

  #設定Y軸區間
plt.ylim(-1.25,+1.25)
plt.show()