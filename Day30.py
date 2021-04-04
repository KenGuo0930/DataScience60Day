# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 15:30:13 2021

@author: 郭奕志
"""
from scipy import stats
import math
import statistics
p = 0.5
n = 100  
r = 50 
probs = stats.binom.pmf(r, n, p)
print(probs)

# 0.07958923738717888