# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 15:15:09 2022

@author: harsh
"""

occupants = [0, 1, 2, 3, 4, 5, 6, '>6']
h = []
def house():
    for x in range(7):    
        y = int(input('Enetr the number of houses with %d occupants '% x))
        h.append(y)
        
    y = int(input('Enetr the number of houses with more than 6 occupants'))
    h.append(y)
    return h
per=[]
def percentage():
    for x in range(7):
       y = (h[x]/sum(h))*100
       per.append(y)
house()
percentage()
print(per)