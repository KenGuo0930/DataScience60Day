# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 14:40:10 2021

@author: 郭奕志
"""

import pandas as pd
import numpy as np
score_df = pd.DataFrame([[1,50,80,70,'boy',1],
                         [2,60,45,50,'boy',2],
                         [3,98,43,55,'boy',1],
                         [4,70,69,89,'boy',2],
                         [5,56,79,60,'girl',1],
                         [6,60,68,55,'girl',2],
                         [7,45,70,77,'girl',1],
                         [8,55,77,76,'girl',2],
                         [9,25,57,60,'girl',1],
                         [10,88,40,43,'girl',3],
                         [11,25,60,45,'boy',3],
                         [12,80,60,23,'boy',3],
                         [13,20,90,66,'girl',3],
                         [14,50,50,50,'girl',3],
                         [15,89,67,77,'girl',3]],
                        columns=['student_id','math_score','english_score','chinese_score','sex','class'])


#將索引(index)依序改為sex、class、student_id，欄位依序改成chinese_score、english_score、math_score
df = score_df.melt(id_vars=['sex','class','student_id'])
print(df.pivot_table(index=['sex','class','student_id'],columns='variable',values='value'))


# variable               chinese_score  english_score  math_score
# sex  class student_id                                          
# boy  1     1                      70             80          50
#            3                      55             43          98
#      2     2                      50             45          60
#            4                      89             69          70
#      3     11                     45             60          25
#            12                     23             60          80
# girl 1     5                      60             79          56
#            7                      77             70          45
#            9                      60             57          25
#      2     6                      55             68          60
#            8                      76             77          55
#      3     10                     43             40          88
#            13                     66             90          20
#            14                     50             50          50
#            15                     77             67          89