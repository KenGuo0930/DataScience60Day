# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 00:39:36 2021

@author: 郭奕志
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import math
import statistics
import seaborn as sns

boys=[164, 176, 169, 169, 165, 175, 159, 151, 144, 160, 183, 165, 156, 170,164, 173, 165, 163, 177, 171]

girls=[169, 183, 170, 168, 182, 170, 173, 185, 151, 156, 162, 169, 162, 181,159, 154, 167, 175, 170, 160]

#mean
print("boys height mean = ",np.mean(boys))
print("girls height mean = ",np.mean(girls))
# boys height mean =  165.95
# girls height mean =  168.3

#median
print("boys height median = ",np.median(boys))
print("girls hight median = ",np.median(girls))
# boys height median =  165.0
# girls hight median =  169.0

#mode
print("boys height mode = ",stats.mode(boys,axis=None))
print("girls height mode = ",stats.mode(girls,axis=None))
# boys height mode =  ModeResult(mode=array([165]), count=array([3]))
# girls height mode =  ModeResult(mode=array([170]), count=array([3]))

#range
print("boys height range = ",max(boys)-min(boys))
print("girlss height range = ",max(girls)-min(girls))
# boys height range =  39
# girlss height range =  34

#variance
print("boys height variance = ",np.var(boys,ddof=1))
print("girls height variance = ",np.var(girls,ddof=1))
# boys height variance =  84.89210526315789
# girls height variance =  95.37894736842104
# =============================================================================
# numpy.var(a, axis=None, dtype=None, out=None, ddof=0, keepdims=<no value>)
# ddof： ： int, 可選參數
#Delta Freedom Degrees”：計算中使用的除數為N - ddof，在哪裏N表示元素數。默認情況下，ddof為零。 
# =============================================================================

## python percent 
print("boys height 90% = ",np.percentile(boys, 90))
print("boys height 50% = ",np.percentile(boys, 50))
print("boys height 20% = ",np.percentile(boys, 20))
print("girls height 90% = ",np.percentile(girls, 90))
print("girls height 50% = ",np.percentile(girls, 50))
print("girls height 20% = ",np.percentile(girls, 20))
# boys height 90% =  176.1
# boys height 50% =  165.0
# boys height 20% =  159.8
# girls height 90% =  182.1
# girls height 50% =  169.0
# girls height 20% =  159.8

# skewness  kurtosis
print("boys height skewness = ",stats.skew(boys))
print("boys height kurtosis = ",stats.kurtosis(boys))
print("girls height skewness = ",stats.skew(girls))
print("girls height kurtosis = ",stats.kurtosis(girls))
# boys height skewness =  -0.47132127317376954
# boys height kurtosis =  0.19395882957876331
# girls height skewness =  0.05985321129365068
# girls height kurtosis =  -0.8203607083948947
mean_boy=np.mean(boys)
plt.hist(boys,alpha=.6,bins=40)
plt.title('boy,skewness={0},kurtosis={1}'.format(round(stats.skew(boys),2),round(stats.kurtosis(boys),2)))
plt.axvline(x=mean_boy)
plt.show()

mean_girl=np.mean(girls)
plt.hist(girls,alpha=.6,bins=40,color="khaki")
plt.title('girl,skewness={0},kurtosis={1}'.format(round(stats.skew(girls),2),round(stats.kurtosis(girls),2)))
plt.axvline(x=mean_girl,color="orange")
plt.show()

