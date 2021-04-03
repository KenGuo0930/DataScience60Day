# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 23:35:51 2021

@author: 郭奕志
"""

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
In [43]:
# 創建基本地圖。
# 當 "projection" 參數為“ortho"時，所得圖位地球儀截面
'''
由此開始寫code 
'''
#設定圖形大小
plt.figure(figsize=(5,5))

#設定投影型態
m=Basemap(projection='ortho',resolution=None,lat_0=50,lon_0=-100)

#設定圖形顏色, 選用NASA 寶石藍輸出 
m.bluemarble(scale=0.5)

#秀圖
plt.show()



m = Basemap(projection='mill',
            llcrnrlat = -90,
            llcrnrlon = -180,
            urcrnrlat = 90,
            urcrnrlon = 180,
           resolution='c') # 成圖設定resolution 

#創建邊線
m.drawcoastlines()
#畫出國家，並使用線寬為2 的線條生成分界線。
m.drawcountries(linewidth=2)
#畫出州界
m.drawstates(color='b')
#畫出城市
m.drawcounties(color='darkred')

plt.title('Basemap Tutorial')
plt.show()


由此開始寫code 
'''
#設置Lambert保形底圖。
#set resolution = None跳過邊界數據集的處理
# projection='lcc'

m = Basemap(width=12000000,height=9000000,projection='lcc',
            resolution=None,lat_1=45.,lat_2=55,lat_0=50,lon_0=-107.)

#選用NASA 寶石藍輸出 
m.bluemarble()

#秀圖
plt.show()