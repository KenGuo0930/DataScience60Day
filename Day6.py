import numpy as np

'''
將下兩列array存成npz檔

array1 = np.array(range(30))

array2 = np.array([2,3,5])

讀取剛剛的npz檔，加入下列array一起存成新的npz檔array3 = np.array([[4,5,6],[1,2,3]])
'''

# array1 = np.array(range(30))
# array2 = np.array([2,3,5])
# array3 = np.array([[4,5,6],[1,2,3]])
# np.save('testarray1.npy',array1)
# np.save('testarray2.npy',array2)
# a = np.load('testarray1.npy')
# b = np.load('testarray2.npy')
# np.savez('array_save.npz',a,b,array3)


'''
[簡答題]
'''

# 1. 請問下列這三種方法有什麼不同？
a = np.array(range(5))
print(a.sum())
print(np.sum(a))
print(sum(a)) 

'''
sum() 是 python 內建的函式，所有型態皆可以用。
np.sum(a) 為numpy 套件，僅使用在陣列
a.sum()  array 套件，僅使用在陣列
'''


# 2.請對一個 5x5 的隨機矩陣作正規化的操作。
"""最小值最大值正規化(Min-Max Normalization)"""
b = np.random.rand(5,5) 
B = (b - b.min())/(b.max()-b.min())
print(b)
print(B)


# 3.請建立一個長度等於 10 的正整數向量，並且將其中的最大值改成 -1。
Z = np.random.randint(0,100,10)
Z[Z.argmax()] =-1
print (Z)