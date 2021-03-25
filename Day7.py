# -*- coding: utf-8 -*-
"""
作業一
"""
import numpy as np


array1 = np.array([[10, 8], [3, 5]])

#1.運用上列array計算反矩陣，乘上原矩陣，並觀察是否為單位矩陣?
array2 = np.linalg.inv(array1)
print(array2)
print(np.dot(array1,array2))


#2. 運用上列array計算特徵值、特徵向量?
eigvalue, eigvector = np.linalg.eig(array1)
print('\n','eigvalue = ',eigvalue)
print('\n','eigvector = \n',eigvector)


#3. 運用上列array計算SVD?
print('\n','SVD = \n',np.linalg.svd(array1))


"""
作業二
"""
# 1. 請比較對一個 100 x 100 x 100 的陣列，使用不同方法對每一個元素 +1 的時間比較
Z = np.random.randint(0, 100, 1000000).reshape(100, 100, 100)

%timeit -n 10 a = 2
for i in Z:
    for j in i:
        for k in j:
            i = i + 1
            
%timeit -n 10 a = 2
for i in Z.flat:
    i = i+1
    
%timeit -n 10 a = 2
for i in np.nditer(Z):
    i = i+1
    
    
    
# 2. 如何從一個陣列中，找出出現頻率最高的數值與位置？
A = np.random.randint(0,10,50)
print(A)
B = (np.bincount(A).argmax())
print(B)
print(np.where(A == B))
# np.where()[0] 表示行索引，np.where()[1]表示列索引
print(np.where(A == B)[0])
#它大致說的是bin的數量比x中的最大值大1，每個bin給出了索引值在x中出現的次數，下面以例項說明



# 3. 如何利用 list(...) 實現 a.tolist() 的效果？試著用程式實作。
a = np.random.randint(10, size=6) 
print(a.tolist())
print(list(a))


b = np.random.randint(10, size=(3,4)) 
print(b.tolist())
print(list(b))


c = np.random.randint(10, size=(2,3,2)) 
print(c.tolist())
print(list(c))