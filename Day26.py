# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 23:33:37 2021

@author: 郭奕志
"""

import bokeh.io
from bokeh.resources import INLINE
from bokeh.plotting import figure, output_file, show, output_notebook, ColumnDataSource
from bokeh.sampledata.stocks import AAPL, GOOG, IBM, MSFT
import pandas as pd

# 環境 settings
bokeh.io.reset_output()
bokeh.io.output_notebook(INLINE)
output_file("bars.html")

#給定資料
fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
counts = [5, 3, 4, 2, 4, 6]

# 不增設按鈕 toolbar_location=None, tools=""
# plot_height 設定條形高度
#配置圖表
p = figure(x_range=sorted_fruits, plot_height=250, title="Fruit Counts",
           toolbar_location=None, tools="")

p.vbar(x=fruits, top=counts, width=0.9)

#Y座標從0開始
p.y_range.start = 0

show(p)