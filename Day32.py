# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 15:37:17 2021

@author: 郭奕志
"""

from numpy.random import normal,uniform
from numpy.random import seed
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from scipy import stats
import math
import pylab


mu=0
sigma=1
b=  stats.norm.cdf(1,mu, sigma)
print("P(Z<1)=",b)


mu=0
sigma=1
b=  stats.norm.cdf(1,mu, sigma)
a=  stats.norm.cdf(-1,mu, sigma)
print("P(Z>1 or Z<-1)=",1-(b-a))



mu=0
sigma=1
b=  stats.norm.cdf(2,mu, sigma)
print("P(Z<2)=",b)