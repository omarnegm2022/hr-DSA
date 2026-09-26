# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 18:23:45 2026

@author: omarn
"""
from .base import MyStack
import numpy
class NumStack(MyStack):

    def __init__(self):
        """needs no parameters and returns an empty stack."""
        self.array = numpy.array([])
    def push(self, item):
        """adds a new item to the top of the stack.
        It needs the `item` and returns nothing"""
        self.array = numpy.append(self.array,item)#.astype(self, dtype)
    def pop(self)->int:
        """
        removes the top item from the stack.
        It needs no parameters and returns the item. The stack is modified.
        """
        item = self.array[-1]
        self.array = self.array[:-1]
        return item

    def peek(self) -> float:
        """
        returns the top item from the stack but doesn't remove it.
        It needs no parameters.
        The stack is NOT modified.
        """
        return self.array[-1]
    
    def is_empty(self) -> bool:
        """tests to see whether the stack is empty.
        It needs no parameters and returns a boolean value.
        """
        return not self.array.size
    def size(self) ->int:
        """returns the number of items on the stack.
        It needs no parameters and returns an integer."""
        return self.array.size