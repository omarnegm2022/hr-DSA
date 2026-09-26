# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 17:44:50 2026

@author: omarn
"""
from .base import MyStack
class StackedList(MyStack):
    def __init__(self):
        self._protectedList = []
        
    def pop(self):
        top, self._protectedList = self._protectedList[-1], \
                                    self._protectedList[:-1]
        return top
    def size(self):
        return len(self._protectedList)
    
    
    def peek(self):
        return self._protectedList[-1]
    
    def push(self,item):
        self._protectedList.append(item)
    
    def is_empty(self):
        return True if not len(self._protectedList) \
        else False
    def __iter__(self):
        return iter(self._protectedList[::-1])