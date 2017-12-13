# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 17:11:11 2017

@author: gejiajun

Two sample Kolmogorov-Smirnov Test
Remark: Data is randomly generated with skewness to present an example

"""

import numpy as np
import pandas as pd
import scipy as sp
import matplotlib.pyplot as plt
from scipy.stats import skewnorm

def c(alpha):
    ret = np.sqrt(-1 / 2.0 * np.log(alpha / 2.0))
    return ret

if __name__ == "__main__":
    # input arguments
    n_w = 80
    n_m = 62
    alpha = 0.05
    skew_w = 0.5
    skew_m = 0.4
    
    # generate data
    w = skewnorm.rvs(skew_w, size = n_w)
    m = skewnorm.rvs(skew_m, size = n_m)
    w.sort()
    m.sort()
        
    # plot profile of data
    fig, ax = plt.subplots(1)
    ax.hist(w)
    ax.hist(m)
    plt.show()
    
    # determine the axis
    wnm = np.r_[w, m]
    wnm = np.unique(wnm)
    n_wm = len(wnm)
    wnm.sort()

    # construct cumulatve function
    cum_w = np.array([(w <= wnm[i]).sum() / n_w for i in range(n_wm)])
    cum_m = np.array([(m <= wnm[i]).sum() / n_m for i in range(n_wm)])
    
    # find largest difference between the two cumulative probability function
    D_stat = np.max(np.abs(cum_w - cum_m))
    D_crit = c(alpha) * np.sqrt((n_w + n_m) / (n_w * n_m))
    max_ix = np.argmax(np.abs(cum_w - cum_m))
    print("if D_statistics is greater than D_critical value:", D_stat > D_crit)
    print("D_critical value:", D_crit, "and D_statistics value:", D_stat)
    
    # plot the cumulative probability function
    fig, ax = plt.subplots(1)
    ax.plot(wnm, cum_w, 'r')
    ax.plot(wnm, cum_m, 'b')
    ax.plot(wnm, (wnm == wnm[max_ix]), 'k')
    plt.show()
    
    