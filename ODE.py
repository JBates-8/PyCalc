"""
File: ODE.py
Author: Jackson Bates
Created: 7/30/2019 8:27 PM 
"""



class Differential:

    def __init__(self,_top,_bot,_deg):
        self.top = _top
        self.bot = _bot
        self.deg = _deg

    def __repr__(self):
        return "d{}/d{}".format(self.top,self.bot)

if __name__ == '__main__':
    diff = Differential('','',1)