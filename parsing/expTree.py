"""
File: expTree.py
Author: Jackson Bates
Created: 6/11/2019 11:24 PM 
"""


class Node:

    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node



class ValueNode(Node):

    def __init__(self, val):
        super().__init__()
        self.type = type(val)
        assert self.type in [int,float]
        self.exp = val


if __name__ == '__main__':
    val1 = ValueNode(2)
    val2 = ValueNode(0.5)
    val3 = ValueNode('12')
