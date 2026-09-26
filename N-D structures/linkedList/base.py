# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 22:57:18 2026

@author: omarn
Another way to ensure that an object has the same type as you expect is to use the isinstance(obj, Class) function. 
    This can be helpful when handling inheritance, as Python considers an object to be an instance of both the parent and the child class. 
Correct! Python always calls the child's __eq__() method 
    when comparing a child object to a parent object.



The functionality to display objects is incredibly important 
    as you integrate custom classes into your development workflows.

Wonderful! Notice that if you raise an exception inside an if statement, 
    you don't need to add an else branch to run the rest of the code. 
    Because raise terminates the function, the code after raise will only be executed if an exception did not occur.



"""

class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
        
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,newdata):
        self.data = newdata
    def setNext(self,newnext):
        self.next = newnext

    def __repr__(self):
        return f"{self.data}"


class UList:#TODO: refactor upon the Bu.Bl. class
    """sorted by timeStamp."""
    def __init__(self):
        self.head = None
    NODE_TRAVERSER = None
    
    def add(self,item):
            temp_var = Node(item)
            temp_var.setNext(self.head)
            self.head = temp_var
        #Result of Reversing the Order of the Two Steps:
        #the node will point to itself.
    
    def insertNodeAtTail(head, data):
        """
hackerrank.com/insert-a-node-at-the-tail-of-a-linked-list/problem
"""
        temp = Node(data)
        if head is None:
            head = temp
        else:
            current_ptr = head
            while current_ptr.getNext() != None:
                current_ptr = current_ptr.getNext()
            current_ptr.setNext(temp)
        return head
    
    def remove(self,item):
        UList.NODE_TRAVERSER = self.head
        item_state, item_ref, previous = self.search(item)
        if item_state:
#from PEP-0008: beware of writing `if x` when you really mean `if x is not None` 

            if previous is None:
                self.head = item_ref.getNext()
            else:             
                previous.setNext(previous.getNext().getNext())

            # item_ref.setNext(None)
###APPROVED from: https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list/copy-from/483695107


        # while UList.NODE_TRAVERSER.getData() != item:
            # UList.NODE_TRAVERSER = UList.NODE_TRAVERSER.getNext()
        
        # UList.NODE_TRAVERSER.setNext(UList.NODE_TRAVERSER.getNext().getNext())
        # UList.NODE_TRAVERSER.getNext().setNext(None)
        return f"""Found between
    {previous.getData()},
        {previous.getNext().getData()}
.
        """if previous is not None else "Found at the HEAD."
        
    def search(self,item,prev = None):
        """Moves only in forward direction.
        Does ~NOT~ retain the previous node*
        """
        UList.NODE_TRAVERSER = self.head#.getData()
        while UList.NODE_TRAVERSER != None:
            if  UList.NODE_TRAVERSER.getData() == item:
                return True,UList.NODE_TRAVERSER, prev
            else:
                prev = UList.NODE_TRAVERSER
                UList.NODE_TRAVERSER = UList.NODE_TRAVERSER.getNext()
        return False, None, prev
#TODO __repr__, __str__ override
        
    def __str__(self):
        return ""
    
    def length(self):
        n_nodes = 0
        UList.NODE_TRAVERSER = self.head
        while not UList.NODE_TRAVERSER == None:
            n_nodes += 1
            print(UList.NODE_TRAVERSER.getData())
            UList.NODE_TRAVERSER = UList.NODE_TRAVERSER.getNext()
        return n_nodes
    
    def isEmpty(self):
        return bool(self.head)
    
    
class OList(UList):
    """ordered by CHAR."""
    NODE_TRAVERSER = None #Ensure not retrieved from the parent.
    def add(self,item):
        temp_var = Node(item)
        previous = (self.search(item))
        if not isinstance(previous,Node):
            temp_var.setNext(self.head)
            self.head = temp_var
        else:
            temp_var.setNext(OList.NODE_TRAVERSER)
            previous.setNext(temp_var)
    def insertNodeAtPosition(llist, data, position = 0):
        """
hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem
"""
        temp = Node(data)
        if llist is None:
        #if position:
        ### print("List is empty!")
            return temp
        else:
            current_ptr = llist
            position -= 1
        while position:
            current_ptr = current_ptr.getNext()
            position -= 1
        temp.next = current_ptr.getNext()
        current_ptr.setNext(temp)
        return llist
    def search(self,item,prev=None):
        """uncertainty supported."""
        print("OList")
        OList.NODE_TRAVERSER = self.head
        
        while OList.NODE_TRAVERSER != None:
            if OList.NODE_TRAVERSER.getData() < item:
                prev = OList.NODE_TRAVERSER
                OList.NODE_TRAVERSER = OList.NODE_TRAVERSER.getNext()
                
            else:
                return True if OList.NODE_TRAVERSER.getData() == item \
                else f"Did you mean ${OList.NODE_TRAVERSER.getData()}$?"
        return prev
    
mlst = OList(); mlst.add(4)
mlst.add(3);mlst.add(5)
# print(mlst.search(3))
mlst.length()
if __name__ != "__main__":
    mylist = UList()
    mylist.add(31);mylist.add(77);mylist.add(17)
    mylist.add(93);mylist.add(26);mylist.add(54)
    
    print(mylist.remove(54))    
    print(mylist.search(54))
    print(mylist.search(93))
    print(mylist.search(77))
else:
    temp = Node(93)
    print(dir(temp))
    
    def reversePrint(llist):
    printStack = StackedList()
    while llist is not None:
        printStack.push(llist.data)
        llist = llist.next
    print(*printStack, sep = '\n')#NOTE: __iter__ return is rotated.