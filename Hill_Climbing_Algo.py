# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 11:57:47 2026

@author: pc
"""
#hill climbing algorithm
def f(x):
     return -(x**2)+5
 
x=int(input("Enter the starting value"))
print("Step by step movement")
while True:
    print("Current x=",x," f(x)=",f(x))
    left=x-1
    right=x+1
    if f(left)>f(x):
        x=left
    elif f(right)>f(x):
        x=right
    else:
        break
    
print("\n Optimal solution found!")
print("Best x= ",x)
print("Maximum value f(x) =",f(x))
