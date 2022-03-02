# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 10:05:26 2022

@author: harsh
"""

def pyramid(rows):
    t=(2*rows)-2
    for r in range(0, rows):
        for c in range(0,t):
            print(end=" ")
        t=t-1   
        for s in range(0,r+1):
            print("*", end=" ")
        print(" ")
        
pyramid(5)