# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 15:14:12 2022

@author: harsha
"""

import math
def areacirc(x):
    y=math.pi
    area = y*x*x
    print('Area of circle: ', area)

r= float(input('Enter the radius: '))
areacirc(r)
