# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 09:41:49 2026


how to print the default class.__slots__ without explicit definition

It is **impossible** to print the default `__slots__` for a class that does not explicitly define them, because **classes without `__slots__` do not have this attribute**.

In Python, the `__slots__` attribute is only created when a class explicitly declares it. If a class relies on the default dynamic dictionary (`__dict__`) for instance attributes, the `__slots__` attribute is absent from the class namespace.

**Key Details:**
*   **Absence of Attribute**: Accessing `__slots__` on a class that hasn't defined it raises an `AttributeError`.
*   **Default Behavior**: Without `__slots__`, Python instances use a `__dict__` to store attributes dynamically, meaning there is no fixed set of slots to enumerate.
*   **Inheritance**: If a base class defines `__slots__`, subclasses inherit the *behavior* of slots but do not automatically gain a `__slots__` attribute unless they define their own. To gather all slot names from a class and its ancestors, you must iterate through the Method Resolution Order (MRO) and collect `__slots__` from each class that explicitly defines it.

```python
class Base:
    pass  # No __slots__ defined

# This will raise AttributeError
# print(Base.__slots__) 

# To check if slots exist:
hasattr(Base, '__slots__')  # Returns False
```


@author: omarn
"""
from base import MyQ

class Task:
    # __slots__ = ('timeStamp', "numberOFpages")
    def __init__(self,TS,NP):
        self.timeStamp = TS
        self.numberOFpages = NP
        
class TaskMan(MyQ):
    """
    The tasks are placed in a queue to be processed in that manner.
    The length of these tasks ranges from 1 to 20 pages at any hour/day.
    
    When the printer completes a task, it will 
    look at the queue to see if there are any remaining tasks to process.
    
    20 tasks per hour means that -on average- there will be one task every
    180 seconds. That is, if the number is 180; we say a task's been created.
    """
                
    def record(self, TS, NP):
        MyQ.enqueue(self, Task(TS, NP));
            
    def check_Q(self):
        return False if self.is_empty() \
            else self.dequeue()
            
            
if __name__ == "__main__":
    # d1 = Task(0,1).__dict__
    # d2 = Task(0,1).__dict__
    # d3 = Task(0,1).__slots__
    # d4 = Task(0,1).__slots__
    # n1 = 300
    # n2 = int("300")
    # print(n1 is n2)#False, since n2 is runtime allocated.
    # print(id(d3) )
    # print(id(d4) )
    # i = 0
    # for _ in range(10):
        # i = {}
    # print(id(Task(0,1).__dict__) )
    print(id([2]))
    print(id([2]))
    l1 = [2,3]; l2 = l1[:]
    print(id(l1))
    i = 1
    l1[0], i = i, l1[0]
    print(id(l1), id(l2))
    l2 = l1[:]
    print(l2,i)


"""
integer intrecing occurs in line-by-line (InteractiveInterpreter), while
constant pooling occurs in code blocks (script file)
"""