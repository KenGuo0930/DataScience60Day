# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 13:23:35 2021


2.6 號學生 3 科平均分數是否有贏過班上一半的同學？
3.由於班上同學成績不好，所以學校統一加分，加分方式為開根號乘以十，請問 6 號同學 3 科成績分別是？
承上題，加分後各科班平均變多少？
"""

import numpy as np 
import pandas as pd

score_df = pd.DataFrame([[1,56,66,70], 
                         [2,90,45,34], 
                         [3,45,32,55], 
                         [4,70,77,89], 
                         [5,56,80,70], 
                         [6,60,54,55], 
                         [7,45,70,79], 
                         [8,34,77,76], 
                         [9,25,87,60], 
                         [10,88,40,43]],
                        columns=['student_id','math_score','english_score','chinese_score'])

#     student_id  math_score  english_score  chinese_score
# 0           1          56             66             70
# 1           2          90             45             34
# 2           3          45             32             55
# 3           4          70             77             89
# 4           5          56             80             70
# 5           6          60             54             55
# 6           7          45             70             79
# 7           8          34             77             76
# 8           9          25             87             60
# 9          10          88             40             43

# 1.6 號學生(student_id=6) 3 科平均分數為何？
score_df = score_df.set_index('student_id')

# student_id
# 1     64.000000
# 2     56.333333
# 3     44.000000
# 4     78.666667
# 5     68.666667
# 6     56.333333
# 7     64.666667
# 8     62.333333
# 9     57.333333
# 10    57.000000
# dtype: float64

print(score_df.mean(axis=1))

# print('score data = \n',score_df)
# print('\n',' student 6 math mean score =  ',score_df.math_score.mean())
# print('\n',' student 6 english mean score =  ',score_df.english_score.mean())
# print('\n',' student 6 chinese mean score =  ',score_df.chinese_score.mean())


# 3.由於班上同學成績不好，所以學校統一加分，加分方式為開根號乘以十，請問 6 號同學 3 科成績分別是？

"""
lambda x
"""
print('\n','開根號乘以十 = \n ',score_df.apply(lambda x : x**(0.5)*10))
#               math_score  english_score  chinese_score
# student_id                                          
# 1            74.833148      81.240384      83.666003
# 2            94.868330      67.082039      58.309519
# 3            67.082039      56.568542      74.161985
# 4            83.666003      87.749644      94.339811
# 5            74.833148      89.442719      83.666003
# 6            77.459667      73.484692      74.161985
# 7            67.082039      83.666003      88.881944
# 8            58.309519      87.749644      87.177979
# 9            50.000000      93.273791      77.459667
# 10           93.808315      63.245553      65.574385
# 承上題，加分後各科班平均變多少

new_score_df = score_df.apply(lambda x : x**(0.5)*10)
print('\n',new_score_df.mean())

#  math_score       74.194221
# english_score    78.350301
# chinese_score    78.739928
# dtype: float64
