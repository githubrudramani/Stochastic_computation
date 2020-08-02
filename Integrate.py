#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 18:29:10 2020

@author: rudramani
"""


### integraion of a function
import math
def f(x):
    return math.exp(x)
f(5)

a = 0 ### lower boundary
b = 1 #### upper boundary
dx = 0.000001
s = 0
i = a
while i < b:
    s += f(i)*dx
    i += dx
    
## applyting scipy
import scipy.integrate 
f = lambda x: math.exp(x)
a = 0
b =1

print(s)
scipy.integrate.quad(f,a,b)
    