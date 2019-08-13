"""
File: Limit.py
Author: Jackson Bates
Created: 8/12/2019 11:37 PM 
"""

class Limit:

    possible_sides = ["left","right","both"]

    def __init__(self,function,aproach_val,side = "both"):
        self.function = function
        self.var = function.var
        self.aproaching = aproach_val
        self.direction = side

    def __str__(self):
        if self.direction == "both":
            return "Lim {} as {} goes to {} from both sides".format(self.function,self.var,self.aproaching)
        else:
            return "Lim {} as {} goes to {} from the ".format(self.function,self.var,self.aproaching,self.direction)