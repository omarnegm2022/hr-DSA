# -*- coding: utf-8 -*-
# https://stackoverflow.com/questions/42413670/whats-the-difference-between-super-and-parent-class-name
# https://docs.python.org/3/howto/mro.html#python-2-3-mro

from CQ import Printer, TasClass
import random
"""
Created on Thu Aug 27 19:55:27 2026

@author: omarn

But what if we need to store some data that is shared among all the instances of a class? 
For example, if we want to introduce a minimal salary across the entire organization. 
That data should not differ among objects. 
    Then, we can define an attribute directly in the class body, rather than when we define the init constructor. 
This will create a class attribute, that will serve as a "global variable" within a class.
(Inside the methods we only use class name-dot-attribute syntax rather than self.)



class Player:
  MAX_POSITION = 10
  
  # Define a constructor
  def __init__(self, position):
    global MAX_POSITION
    # Check if position is less than the class-level attribute value
    if position <= MAX_POSITION:
NameError: name 'MAX_POSITION' is not defined



# Create Players p1 and p2
p1 = Player(9)
p2 = Player(5)

print("MAX_POSITION of p1 and p2 before assignment:")
# Print p1.MAX_POSITION and p2.MAX_POSITION
print(p1.MAX_POSITION)
print(p2.MAX_POSITION)

# Assign 7 to p1.MAX_POSITION
Player(3).MAX_POSITION = 7 #TODO: try removing the calling operators; the parenthesis

print("MAX_POSITION of p1 and p2 after assignment:")
# Print p1.MAX_POSITION and p2.MAX_POSITION
print(p1.MAX_POSITION)
print(p2.MAX_POSITION)
>>
MAX_POSITION of p1 and p2 before assignment:
10
10
MAX_POSITION of p1 and p2 after assignment:
10
10


Remember, a decorator is convenience feature that allows us to modify the behavior of a function. 
Also remember that a method is a function that is specific to a class. 
So, the classmethod decorator allows us to modify the behavior of the method defined directly afterwards.

6. When to use class methods
03:23 - 04:12
Given class methods require a narrow scope, when should we use them? 
We've seen their application as an alternative constructor, such as creating an object from a file or accepting a different format than a regular constructor. 
Remember, class methods can't access instance attributes. 
While this might seem like a limitation, it means we can create methods that don't require these attributes to work correctly! 
Another scenario is when we want to restrict a class to a single object. 
This is known as the Singleton design pattern and can be useful when exactly one instance of a class is needed to control access to resources, such as database connections or configuration settings.

@classmethod
def _(cls,): #the special required argument
"""
"""
12. Inheritance: "is-a" relationship
04:02 - 04:27
That's because an instance of a Child class is an instance of the Parent class too. 
    However, this is not the case for a generic object(i.e. of the base, super class).
    
    {That's a tricky one! Pay attention to the language: 
     in reality, the child class inherits all - not just some - parts of the parent class. 
     Inheritance cannot be used to pick and choose desired parts of the class: it's all or nothing
}
        
The interface of the call is the same, and the actual method that is called is determined by the instance class, which is 
an application of polymorphism.
Violating polymorphism is when the parent and child class no longer have a unified interface - 
    their methods have different arguments, so they do not work in the same way.


! Class attributes CAN be inherited, and the value of class attributes CAN be overwritten in the child class !
"""
# if __name__ == "__main__":
#         """
#     Of interest for us is the average amount of time students will wait
# for their papers to be printed ( = the average amount of time a
# task waits in the queue ).

#     As students submit printing tasks, we will add them to a waiting
# list, a queue of print tasks attached to the printer.

#     To model this situation we need to use some probabilities.
#     """
#         print_device = Printer.UPrinter(5)
#         newMan = TasClass.TaskMan()
#         waiting_list = []
#         for second in range(1 * 60 * 60):
#             if random.choice(range(1,181)) == 180: #At some second,
#             #did any student assign a task?!
#                 newMan.record(second,random.randrange(1,21))
#             if not print_device.IS_BUSY:
#                     any_remaining_task = newMan.check_Q() #TasClass.Task.Q_stat(second)
#                     if any_remaining_task:
#                     # las_task = prin_tas_Q.dequeue()
#                         print_device.proceed(any_remaining_task)
#                     #las_task = tuple(assign time, n_of_pages)
#                         waiting_list.append(second - any_remaining_task.timeStamp)#prin_tas_Q.la_stamp
#             print_device.tick()
#         print(waiting_list)
if __name__ == "__main__":
    possible_rates = [5,10] # pages per minute
    print_device = Printer.UPrinter(random.choice(possible_rates))
    
    for _ in range(10):
        task_manager = TasClass.TaskMan()
        print(id(print_device), print_device.ppm)
        waiting_list = []
        
        for current_second in range(3600):  # 1 hour simulation
# 1. Simulate task arrival (1 in 180 chance per second)
            if random.randrange(1, 181) == 180:
                task_manager.record(current_second, random.randrange(1, 21))
                    
# 2. If printer is idle and queue has tasks
            if not print_device.IS_BUSY:
                any_remaining_task = task_manager.check_Q()
                if any_remaining_task:  # If check_Q didn't return False
                    # Calculate exact wait time using the task's unique timestamp
                    waiting_list.append(current_second - any_remaining_task.timeStamp)
                    
                    # Assign task to printer (ensuring total seconds calculation is used)
                    print_device.proceed(any_remaining_task) 
                    
# 3. Tick the printer forward by 1 second
            print_device.tick()
# . Reset the printer:
        print_device.ppm = random.choice(possible_rates)
        print_device.time_remaining = 0
        print_device.current_task = None
            
        print_device.IS_BUSY = False
        
        print("Avg Wait Times:", sum(waiting_list)/len(waiting_list))
        print("Remaining Tasks in Queue:", task_manager.size())
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        