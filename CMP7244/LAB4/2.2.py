# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 09:19:00 2022

@author: harsh
"""

def fn(x):
        try:
            y=float(x)
            print(y**2)
        except ValueError:
            print("Sorry Man, I'm afraid I can't do that")
            return 0.0

a=input('Enter')
fn(a)