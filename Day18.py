# -*- coding: utf-8 -*-
"""


分析全校女生與男生國文平均差幾分?
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
score_df = score_df.set_index('student_id')
print(score_df)

#student_id  math_score  english_score  chinese_score   sex  class
#                                                        
# 1                   50             80             70   boy      1
# 2                   60             45             50   boy      2
# 3                   98             43             55   boy      1
# 4                   70             69             89   boy      2
# 5                   56             79             60  girl      1
# 6                   60             68             55  girl      2
# 7                   45             70             77  girl      1
# 8                   55             77             76  girl      2
# 9                   25             57             60  girl      1
# 10                  88             40             43  girl      3
# 11                  25             60             45   boy      3
# 12                  80             60             23   boy      3
# 13                  20             90             66  girl      3
# 14                  50             50             50  girl      3
# 15                  89             67             77  girl      3


# =============================================================================
#        找出全年級各科成績最高分與最低分? 
# =============================================================================
print(score_df.max())
# math_score         98
# english_score      90
# chinese_score      89
# sex              girl
# class               3
dtype: object
print(score_df.min())
# math_score        20
# english_score     40
# chinese_score     23
# sex              boy
# class              1
# dtype: object


# =============================================================================
# 找出數學班平均最高的班級?
# =============================================================================
print(score_df.groupby('class').mean())

# class   math_score  english_score  chinese_score
#                                          
# 1       54.800000      65.800000      64.400000
# 2       61.250000      64.750000      67.500000
# 3       58.666667      61.166667      50.666667
print(score_df.groupby('class').mean().max())
# math_score       61.25
# english_score    65.80
# chinese_score    67.50
# dtype: float64


print(max(score_df.groupby('sex').mean()['chinese_score'])-min(score_df.groupby('sex').mean()['chinese_score']))
# 7.333333333333329


print(score_df.groupby('sex').mean()['chinese_score'])
# sex
# boy     55.333333
# girl    62.666667
# Name: chinese_score, dtype: float64