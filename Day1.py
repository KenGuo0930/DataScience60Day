import numpy as np

a = np.arange(0,21)
"""
home work 1
1.生成一個等差數列，首數為 0，尾數為 20，公差為 1 的數列。
2.呈上題，將以上數列取出偶數。
3.呈 1 題，將數列取出 3 的倍數。
"""
print(a)
print(a[::2])
print(a[::3])




'''[簡答題]'''

'''#1. 請問下列兩種將 Array 轉換成 List 的方式有何不同？'''
b = np.arange(15).reshape(3, 5)
print('\n','list(a): ', list(b))
print('tolist(): ', b.tolist())
#list(a):  [array([0, 1, 2, 3, 4]), array([5, 6, 7, 8, 9]), array([10, 11, 12, 13, 14])]
#tolist():  [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]
'''
list(a) 只會把第一層的元素轉換成 List，多層的話只有第一層會轉
tolist() 才能達成多層的型態轉換。
'''


'''#2. 請試著在程式中印出以下三個 NdArray 的屬性並且解釋結果？
（屬性：ndim、shape、size、dtype、itemsize、length、type）'''
a2 = np.random.randint(10, size=6) 
b2 = np.random.randint(10, size=(3,4)) 
c2 = np.random.randint(10, size=(2,3,2)) 
print('\n','ndarry.ndim a2 = ',a2.ndim)
print(' ndarry.shape a2 = ',a2.shape)
print(' ndarray.size a2 = ',a2.size)
print(' darray.dtype a2 = ',a2.dtype)
#print('ndarray.itemsize a2 = ',a1.itmesize)
print(' ndarray.data a2 = ',a2.data)

print('\n'' ndarry.ndim b2 = ',b2.ndim)
print(' ndarry.shape b2 = ',b2.shape)
print(' ndarray.size b2 = ',b2.size)
print(' darray.dtype b2 = ',b2.dtype)
#print('ndarray.itemsize a2 = ',b2.itmesize)
print(' ndarray.data b2 = ',b2.data)

print('\n','ndarry.ndim c2 = ',c2.ndim)
print(' ndarry.shape c2 = ',c2.shape)
print(' ndarray.size c2 = ',c2.size)
print(' darray.dtype c2 = ',c2.dtype)
#print('ndarray.itemsize c2 = ',c2.itmesize)
print(' ndarray.data c2 = ',c2.data)

# ndarray.ndim： 陣列有多少維度
# ndarray.shape： 每個維度的大小
# ndarray.size： 陣列當中有幾個元素
# ndarray.dtype： 陣列中的資料型態
# ndarray.itemsize： 陣列中每個元素佔用的空間
# ndarray.data： 陣列所存在的記憶體位置

'''#3. 如何利用 list(...) 實現 a.tolist() 的效果？試著用程式實作。'''

#random.randint(low, high=None, size=None, dtype='l')用來隨機建立資料：
a3 = np.random.randint(100, size=10) 
print(a3.tolist())
print(list(a3))
