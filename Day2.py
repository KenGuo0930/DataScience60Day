"""
題目：
array1 = np.array(range(30))
將上列陣列(array1)，轉成維度為(5X6)的 array，順序按列填充。(hint:order="F")
呈上題的 array，找出被 6 除餘 1 的數的索引

"""
import numpy as np
array1 = np.array(range(30))
array2 = array1.reshape(5,6,order = 'F') #(hint:order="F")
print('\n',array1)
print('\n',array2)
print('\n',np.where(array1 % 6 == 1))