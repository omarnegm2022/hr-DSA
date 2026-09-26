# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 09:41:43 2026

@author: omarn
"""
# from abc import abstractclassmethod
import numpy

class MyQ:
    """
    
    Queue() creates a new queue that is empty. It needs no
parameters and returns an empty queue.
    enqueue(item) adds a new item to the rear of the
queue. It needs the item and returns nothing.
    dequeue() removes the front item from the queue. It
needs no parameters and returns the item. The queue is
modified.
    isEmpty() tests to see whether the queue is empty. It
needs no parameters and returns a boolean value.
    size() returns the number of items in the queue. It needs
no parameters and returns an integer.
    """
    def __init__(self):
        """OVERRIDEN the default constructor*
        
        creates a new queue that is empty.
        It needs no parameter and returns an empty queue
        """
        # self.status = status
        self.array = numpy.array([], dtype = object)

    IS_OK = False #class STATUS flag
    @classmethod
    def test_class(cls):
        """
        SUMMARY.

        Returns
        -------
        TYPE
            DESCRIPTION.
        """
        trial = cls()
        size_before = trial.array.size
        trial.enqueue(3)
        if trial.size() > size_before:
                MyQ.IS_OK = "Ok!"
        size_before = trial.array.size
            # print(trial.dequeue())
        if not trial.size() < size_before:
                MyQ.IS_OK = "dequeue() has an issue. Please refer to the dev team."
        print(trial.is_empty())
        return MyQ.IS_OK
            
    def enqueue(self,item):
        """
        adds a new item to the rear of the queue.
        It needs the item and returns nothing.
        """
        if not MyQ.IS_OK:
            pass
        self.array = numpy.insert(self.array, 0, item)
    
    def dequeue(self):
        """
        removes the front item from the queue.
        It needs no parameters and returns the item.
        The queue is modified.
        """
        if not MyQ.IS_OK:
            pass
        item = self.array[-1]
        self.array = numpy.delete(self.array,-1)
        return item
    
    def is_empty(self):
        """tests to see whether the queue is empty. 
    It needs no parameters and returns a boolean value. 
       """
        if not MyQ.IS_OK:
            pass
        return not self.array.size
    
    def size(self):
        """
        returns the number of items
        in the queue. It needs no parameters and returns an integer.
        """
        if not MyQ.IS_OK:
            pass
        return self.array.size
    
if __name__ == "__main__":
    if input("Test?(y/n) ") == "y":
        print("base Q status: ", MyQ.test_class())