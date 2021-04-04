# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 16:36:18 2021

@author: 郭奕志
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math
from scipy import stats

total = 100
men = 90
women = total - men
men_long = men * 0.1
men_short = men - men_long
women_long = women * 0.5
women_short = women - women_long

women_long/(women_long + men_long)