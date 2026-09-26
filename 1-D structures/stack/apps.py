# -*- coding: utf-8 -*-
#https://docs.python.org/3/reference/import.html#packages
"""
Created on Thu Aug 27 13:54:01 2026
Abstract Data Type (ADT)

 A programmer-defined data type specified by:
 a set of data values
 a collection of well-defined operations

 Defined independent of its implementation.

Object = data       + functionality
           ^            ^
        state(attr.)   behavior(method)

a class is an abstract template, while an object is a concrete representation of a class.

dir(obj/cls) # shows the bundled items within it.
type(obj) #shows the class title.

if you need more information on something specific you can use help(), passing, 
    for example, one of the object's methods.
    
ch.2 from DataCamp: anatomy of the class
- `self` is included referring to the object will be created. 
    Put another way, it's a stand-in for the future object.
    self.attr is self.obj syntax

@author: omarn
"""

from StackFam import ArrStack

### SOME EXAMPLE
#class Employee:
  
#   # Include a set_name method
#   def set_name(self, name):
#     self.name = name

# emp = Employee()

# # Use set_name() on emp to set the name of emp to 'Korel Rossi'
# # emp.set_name('Korel Rossi')
# print(emp.name)
#// AttributeError: 'Employee' object has no attribute 'name'
code = """
int sumList( int theList[], int size )
{" "
int sum = 0;
int i = 0;
while( i < size ) {
sum += theList[ i ];
i += 1;
}
return sum;
}
"""
def code_validation(script):
    opens = '{ [ ( "'.split()
    print(opens)
    closes = '} ] ) "'.split()
    print(closes)
    tokenStack = ArrStack.NumStack()
    for char in code:
        
        if char in closes:
            print(char)
            if opens.index(tokenStack.pop()) != closes.index(char):
                return "Invalid!"
        if char in opens:# and (tokenStack.peek() != '"'):
            #TODO: Discover the fix
            #return self.array[-1]
#>> IndexError: index -1 is out of bounds for axis 0 with size 0
            tokenStack.push(char)
    
    return True

if __name__ == "__main__":
    if input("Test? (y/n)") == 'y':
    # print(dir(NumStack()))
        trial = ArrStack.NumStack()
        trial.push(int(1))
    # print(trial.peek())
        print(trial.pop())
        print(trial.is_empty())
        print(trial.size())
    else:
        print(code_validation(code))
# classs.p()
