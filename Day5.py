import numpy as np
'''作業一'''
#1.有多少學生英文成績比數學成績高?
english_score = np.array([55,89,76,65,48,70])
math_score = np.array([60,85,60,68,55,60])
chinese_score = np.array([65,90,82,72,66,77])

print(english_score[english_score > math_score])#3位
print(np.sum(english_score > math_score))

#2.是否全班同學最高分都是國文?
a =  chinese_score > english_score
b = chinese_score > math_score
print(a == b)



''''作業二'''
# 產生一個 1-11 的一維陣列，並且把 3-6 由正數變成負數。
c = np.arange(1,12)
c[(3 <= c) & (c < 7)] *= -1
print(c)


#試著從一個隨機陣列中，找出比 0.5 大的數有幾個？
d = np.random.rand(10,10) 
print(d)
print(d[d > 0.5].size)