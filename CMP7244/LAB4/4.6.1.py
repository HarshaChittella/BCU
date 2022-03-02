# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 16:15:55 2022

@author: harsh
"""

def fn(a):
    for i in range(1,13):
        print('%d times %d is %d'%(i,a,i*a))
a= int(input('Enter the number: '))
fn(a)       
        
