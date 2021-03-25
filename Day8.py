# -*- coding: utf-8 -*-
"""
作業
"""
import numpy as np
import pandas as pd


# 1. [簡答題] 請問 Pandas 套件最主要的貢獻是什麼？
"""
將適用於數學的陣列型態，封裝成適合用於資料分析的型態
提供了快速高效的 DataFrame 結構（底層使用 Cython 或 C 的實作對效能進行高度優化）
廣泛地在學術傑與商業領域中使用，包括金融，神經科學，經濟學，統計學，廣告，Web分析等。
對於資料格式有高度的銜接性，包含 CSV、Excel 或資料庫（SQL）皆能提供彈性的讀寫工具
"""
# Comma-Separated Values，CSV，有時也稱為字元分隔值，因為分隔字元也可以不是逗號
df = pd.read_csv('https://raw.githubusercontent.com/MachineLearningLiuMing/scikit-learn-primer-guide/master/Data.csv')
print('\n','df = \n',df)
print('\n','shape =',df.shape) 
print('\n','size = ',df.size) 
print('\n','dtypes = \n',df.dtypes) 
print('\n','values = \n',df.values)
print('\n','index = \n',df.index)
print('\n','columns = \n',df.columns)
print('\n','dtypes = \n',df.dtypes)

