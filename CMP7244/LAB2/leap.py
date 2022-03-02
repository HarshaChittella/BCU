# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 15:49:39 2022

@author: harsha
"""

def isleap(y):
   if y%400 == 0:
       return 'True'
   elif y%100 == 0:
       return 'False'
   elif y%4==0:
       return 'True'

def daysinmonth(month, year):

    if month == 2:
        if isleap(year):
            print(29)
        else:
            print(28)
        
    elif month == 4 or month== 6 or month== 9 or month==11:
        print(30)
    else: print(31)
    
        