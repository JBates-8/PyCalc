"""
File: Lagrange.py
Author: Jackson Bates
Created: 5/13/2019 10:50 PM 
"""


import matplotlib.pyplot as plt
import logging

class Lagrange:

    def __init__(self, x, y, f_name):
        assert len(x) == len(y)
        self.maxOrder = len(x)
        self.xData = x
        self.yData = y
        self.name = f_name
        self.logger = logging.getLogger(__name__)
        self.logger.info("Lagrange Polynomial '{}'".format(self.name))
        self.setup()

    def setup(self):
        """
        assuming x and y data are set
        """

        self.poly_list = []
        for j in range(self.maxOrder):
            basis = [self.yData[j]]
            for m in range(self.maxOrder):
                basis.append([self.xData[j],self.xData[m]])
            self.poly_list.append(basis)
        self.logger.info("Polylist generated: {}".format(self.poly_list))

    def plot_data(self, x_lim = None, y_lim = None, gridlines = True):
        self.clear_fig()
        axes = plt.gca()
        if x_lim is None:
            xmin = int(min(self.xData))-1
            xmax = int(max(self.xData))+1
        else:
            xmin = x_lim[0]
            xmax = x_lim[1]
        if y_lim is None:
            ymin = int(min(self.yData)) - 1
            ymax = int(max(self.yData)) + 1
        else:
            ymin = y_lim[0]
            ymax = y_lim[1]
        axes.set_xlim(xmin,xmax)
        axes.set_ylim(ymin,ymax)
        plt.grid(gridlines)
        plt.scatter(self.xData,self.yData)
        plt.show()

    def clear_fig(self):
        plt.clf()
        plt.cla()
        self.logger.info("Plot figure and axes cleared")

if __name__ == '__main__':
    L = Lagrange([0,1,2,3],[0,1,4,9],'L')




