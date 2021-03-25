# -*- coding: utf-8 -*-
"""
多維陣列的切片與索引

@author: 郭奕志
"""

import numpy as np 

data = np.array([[1, 2,3],[4,5,6],[7,8,9]])
print('\n','data  \n',data) 
print('\n','data[0,1] \n',data[0,1]) # 取出第 0 個
print('\n','data[0:3] \n',data[0:3]) 
print('\n','data[0:3,0] \n',data[0:3,0]) 
print('\n','data[0:2,1] \n',data[0:2,1]) 
print('\n','data[1:3,2] \n',data[1:3,2]) 
