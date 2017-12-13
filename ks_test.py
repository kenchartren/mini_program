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
    # part of critical function to calculate critical value
    ret = np.sqrt(-1 / 2.0 * np.log(alpha / 2.0))
    return ret

if __name__ == "__main__":
    # Part 1:
    # input arguments
    n_w = 80
    n_m = 62
    alpha = 0.05
    skew_w = 1
    skew_m = -1
    
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
#    plt.show()
    
    # Part 2:
    # input arguments
    n_bin = 10
    
    # construct bins to count the frequency
    bins = np.arange(wnm[0], wnm[-1], (wnm[-1] - wnm[0]) / n_bin)
    
    # calculate density
    dens_w = np.array([((w <= bins[i+1]) * (w >= bins[i])).sum() / n_w for i in range(n_bin-1)])
    dens_m = np.array([((m <= bins[i+1]) * (m >= bins[i])).sum() / n_m for i in range(n_bin-1)])
    
    # calculate cumulation
    cum_w_d = np.cumsum(dens_w)
    cum_m_d = np.cumsum(dens_m)
    cum_w_d = np.r_[0, cum_w_d]
    cum_m_d = np.r_[0, cum_m_d]

    # plot the cumulative chart
#    fig, ax = plt.subplots(1)
    ax.plot(bins, cum_w_d, 'p')
    ax.plot(bins, cum_m_d, 'y')
    plt.show()    
        
    
    



    
    