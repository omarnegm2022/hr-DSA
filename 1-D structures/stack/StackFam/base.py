# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 18:31:08 2026

@author: omarn
"""

from abc import ABC, abstractmethod
"""
Special Note About Member Access
In Python, all class data members are public. There is no concept of private or protected membership as there is in C++ 
and Java. Conventionally, Python programs indicate access by pre-pending underscores to the data member names. One 
underscore indicates protected, two indicates private. I will expect everyone to follow this convention
"""

class MyStack:
    """

push(item) adds a new item to the top of the stack. It
needs the item and returns nothing.

pop() removes the top item from the stack. It needs no
parameters and returns the item. The stack is modified.

peek() returns the top item from the stack but does not
remove it. It needs no parameters. The stack is not
modified.

isEmpty() tests to see whether the stack is empty. It
needs no parameters and returns a boolean value.

size() returns the number of items on the stack. It needs
no parameters and returns an integer.
    """
    @abstractmethod    
    def pop(self):
        """"""
        pass
    @abstractmethod
    def size(self):
        """"""
    
    @abstractmethod
    def peek(self):
        """"""
    @abstractmethod
    def push(self,item):
        """"""
    @abstractmethod
    def is_empty(self):
        """"""