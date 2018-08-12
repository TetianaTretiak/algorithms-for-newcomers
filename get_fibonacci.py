# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 19:31:59 2018

@author: Midori

@various solutions for Fibonacci
"""

def get_fibonacci_array(base):
    
    fib_list = []
    
    for i in range(base):
        if i == 0 or i == 1:
            fib_list.append(1)        
        else:
            fib_list.append(fib_list[i - 1] + fib_list[i - 2])
            
    return fib_list

print(get_fibonacci_array(6))        


def get_fibonacci_tuple(n):
    
    a, b = 1, 1
    
    for i in range(n-1):
        a,b = b,a+b
    
    return a

print(get_fibonacci_tuple(6))
 

def get_fibonacci_recursion(n):

    if n == 1 or n == 2:
        return 1

    return get_fibonacci_recursion(n-1) + get_fibonacci_recursion(n-2)

print(get_fibonacci_recursion(6))