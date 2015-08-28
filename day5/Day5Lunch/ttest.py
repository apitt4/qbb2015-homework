#!/usr/bin/env python

import numpy as np
from scipy import stats

for i in range(1000):

    rvs1 = stats.norm.rvs(loc=5, scale=10, size=500)
    rvs2 = stats.norm.rvs(loc=5, scale=10, size=500)

    print stats.ttest_ind(rvs1, rvs2)[1]