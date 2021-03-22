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


'''2021/03/22 作業更新'''

a = np.array(range(30))
# 1.[簡答題] 請問 type(...) 跟 a.dtype 這兩個語法有什麼不同？
"""type 看的是引數的資料型別，dtype 看的是列中元素的資料型別"""
print('type(a): ', type(a))
print('a.dtype: ', a.dtype)


# 2.請撰寫一個判斷 a 的元素是否等於指定資料型態的函式
a = np.random.randint(50, size=5) 
def is_dtype(a, t):
    
    return a.dtype == t

print('\n',is_dtype(a, 'int32')) # True
print(is_dtype(a, np.int32)) # True
print(is_dtype(a, np.dtype('int'))) # True



# 3.[簡答題] 承上題，請判斷下列三種寫法為何不正確？
def is_dtype(a, t):
    return a.dtype is t

def is_dtype(a, t):
    return type(a) == np.dtype(t)

def is_dtype(a, t):
    return type(a) is np.dtype(t)

'''
第一種:資料的所有型態、性質都要一模一樣
第二種:type 看的是引數的資料型別，dtype 看的是列中元素的資料型別，兩者不能比較
第三種:同二。資料的所有型態、性質不可能一模一樣
'''