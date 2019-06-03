"""
File: Interpolate.py
Author: Jackson Bates
Created: 5/13/2019 10:50 PM 
"""


class Lagrange():

    def __init__(self, xset, yset, degree):
        self.x = xset
        self.y = yset
        self.deg = degree
        self.n = len(xset)



    def lagrange(self, n):
        return [self.poly(x) for x in range(1,n+1)]

    def poly(self, idx):
        lst = [self.y[idx-1]]
        for i in range(self.n):
            if i != idx:
                print("num: {}\nden: {}".format(1,2))




if __name__ == '__main__':
    import numpy as np




    print("Hello World!")