#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
2024-12-25 14:35:37
@author: janmejoyarch
@hostname: suitpoc1

DESCRIPTION
"""

import matplotlib.pyplot as plt
import numpy as np

def parse_datetime(entry):
    return np.datetime64(entry)


if __name__=='__main__':
    SAVE=True
    data= np.loadtxt('data.txt', converters={0:parse_datetime}, 
                     dtype=[('date', 'datetime64[D]'),('wt', 'float')])
    mean= np.round(np.mean(data['wt']),1)
    stdev= np.round(np.std(data['wt']),1)

    plt.figure('Wastage', figsize=(8,4))
    plt.plot(data['date'], data['wt'], 'o-', color='black')
    plt.xticks(rotation=30)
    plt.ylabel('Food wastage at dinner (kg)')
    plt.xlabel('Date')
    plt.grid(alpha=0.5)
    plt.title(rf'Mean= {mean} kg | $\sigma$: {stdev} kg')
    plt.tight_layout()
    if SAVE: plt.savefig('plot.png', dpi=150); print("Plot updated")
    plt.close()
