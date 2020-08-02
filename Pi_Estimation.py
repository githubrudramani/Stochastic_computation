#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 18:27:22 2020

@author: rudramani
"""

'''
Estimating Value of Pi using simple Monte-Carlo sampling:
Circle of readius one enclosed in a square of length two units.
lets (0,0) is the center of the circle

where (area of circle / area of Square) = Pi/4

'''

import random

def Pi_estimation(N):
    n_hits = 0
    for i in range(N):
        x,y = random.uniform(-1,1),random.uniform(-1,1)
        if x**2 + y**2 < 1:
            n_hits += 1 
    return 4* n_hits/float(N)


for i in range(1000):
    print(Pi_estimation(10000))
        


