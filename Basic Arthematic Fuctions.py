# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 22:39:50 2019

@author: Ashu
"""


class Calculate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def divide(x, y):
        return x / y

    def multiply(x, y):
        return x * y

    def power(x, y):
        return x ^ y

    def compare(x,y):
        if x == y:
            print("Matching : True")
        else:
            print("Matching : False")
"""
Calling Function
"""

Calculate.compare(10,10)