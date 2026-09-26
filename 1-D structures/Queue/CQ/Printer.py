# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 09:41:38 2026
https://stackoverflow.com/questions/6760685/what-is-the-best-way-of-implementing-a-singleton-in-python
https://docs.python.org/3/reference/datamodel.html#metaclasses
@author: omarn
"""

#TODO: https://refactoring.guru/design-patterns/singleton/python/example#example-1
class OldPrinter:
#NOTE: It is ONE printer in the lab, so use Singleton DP.
    """
    For every second, we can simulate the chance that a print task occurs by 
    generating a random number between 1 and 180 (((inclusive))).
    """
    IS_BUSY = False
    @classmethod
    def INIT(cls,ppm):
        """Pages Per Minute"""
        cls.ppm = ppm
        cls.time_remaining = 0
        cls.curren_task = None        
        return cls()
    
    @classmethod
    def proceed(cls, new_task,n_of_pages):
        print(cls.curren_task,n_of_pages)
        if cls.curren_task:
            cls.time_remaining -= 1
            if not cls.time_remaining:
                cls.curren_task = None; Printer.IS_BUSY = False        
            return cls(current_task,Printer.IS_BUSY)
#The printer does one second of printing if necessary. It also subtracts one second from the time required for that task.
        
            
        cls.current_task = new_task
        Printer.IS_BUSY = True
        cls.time_remaining = n_of_pages * 60/cls.ppm
        # if not(queue.is_empty()):# and not Printer.IS_BUSY:
        #     IS_BUSY = True
        #     queue.dequeue()
        #     pass
        return cls(new_task,n_of_pages)
    
    
class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class UPrinter():#metaclass=SingletonMeta
    """
    Finally, any singleton should define some business logic, which can be
    executed on its instance.
    """
    def __init__(self,ppm):
        """Pages Per Minute"""
        self.ppm = ppm
        self.time_remaining = 0
        self.current_task = None
        
        self.IS_BUSY = False
    
    def proceed(self, new_task):
            # return self(current_task,Printer.IS_BUSY)
#The printer does one second of printing if necessary. It also subtracts one second from the time required for that task.
        self.current_task = new_task
        self.IS_BUSY  = True
        self.time_remaining = (new_task.numberOFpages * 60)/self.ppm

    def tick(self):
        if self.current_task != None:
            self.time_remaining -= 1
            if self.time_remaining == 0:#NOTE: watch out for the indentation!
                self.curren_task = None; self.IS_BUSY = False        
                
        

        # ...