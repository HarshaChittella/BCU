# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 09:50:32 2022

@author: harsh
"""

def prime(y):
    prime_list = []
    for i in range(2, y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list

a=int(input('Enter the number: '))
lst=prime(a)
print(lst)