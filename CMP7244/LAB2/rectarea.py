# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 15:21:04 2022

@author: harsha
"""

def rectarea(x,y):
    area = x*y
    print('Area of the rectangle is:', area)

width = float(input('Enter the width  of the  rectangle: '))
height = float(input('Enter the height of the rectangle:'))
rectarea(width, height)