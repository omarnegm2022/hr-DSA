# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/queue-using-two-stacks/problem?isFullScreen=false
Created on Mon Sep  7 13:57:15 2026
https://stackoverflow.com/questions/21665485/how-to-make-a-custom-object-iterable
@author: omarn
"""

import os
class MyStack:
    
    def __init__(self):
        self.list = []
    def pop(self):
        try:
            itm, self.list = self.list[-1], self.list[:-1]
            return itm
        except IndexError:
            return "the DS's empty!"
    def size(self):
        return len(self.list)
    

    def peek(self):
        return self.list[-1]

    def push(self,item):
        self.list.append(item)

    def is_empty(self):
        return True if not len(self.list) \
        else False
class Q_of_Stacks:
    def __init__(self):
        self.ram = MyStack()
        self.rear = MyStack()
    def enqueue(self,item):
        self.rear.push(item)
    def dequeue(self):
        # if self.ram.is_empty():
        while not self.rear.is_empty():
                self.ram.push(self.rear.pop())
        return self.ram.pop()
    def elevate(self):
        return self.ram.peek()


number_of_queries = input().rstrip().split()
StacQ = Q_of_Stacks()
for q in range(number_of_queries):
    query = input().strip().split()
    if int(query[0]) == 1:
        StacQ.enqueue(query[-1])
    elif int(query[0]) == 2:
        StacQ.dequeue()
    elif int(query[0]) == 3:
        print(StacQ.elevate())
        
