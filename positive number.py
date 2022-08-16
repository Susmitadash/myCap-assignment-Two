# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 12:24:58 2022

@author: LENOVO
"""

# print positive Numbers in a List

#input of list 
list=[]
n=int(input("Enter size of list "))
for i in range(0,n):
    e=int(input("Enter element of list "))
    list.append(e)

print("Positive numbers in",list,"are: ")
  
#traversing
for i in list:   
    # checking condition
    if i >= 0:
       print(i, end = " ")

