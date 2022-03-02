# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 15:09:21 2022

@author: harsh
"""

x1,y1=0,0
distance=[0]
def dist(x1,y1):
    while x1!=999:
        x2 = int(input('Enter the value of X2: '))
        y2 = int(input('Enter the value of Y2: '))
        if x2==999 and y2==999:
            s=sum(distance)
            print(s)
            break
        x=x2-x1
        y=y2-y1
        d=((x**2)+(y**2))**(1/2.0)
        distance.append(d)
        location(x2,y2)
        x1=x2
        y1=y2
        
def location(x2,y2):
    if y2>y1:
        if x2>x1:
            print('Top Right')
        if x2<x1:
            print('Top Left')
        if x1==x2:
            print('Top')
    if y2<y1:
        if x2>x1:
            print('Bottom Right')
        if x2<x1:
            print('Bottom Left')
        if x1==x2:
            print('Bottom')
    if y2==y1:
        if x2>x1:
            print('Right')
        if x2<x1:
            print('Left')
dist(x1,y1)