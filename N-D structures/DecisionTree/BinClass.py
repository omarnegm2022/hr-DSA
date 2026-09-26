# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 07:09:02 2026
Thoughts to refactor simple implementation of the parse tree of fully parenthesised expression:
- use the stack to store sub expressions instead of just keeping the root >> some subExpr are inbalanced, very deep (size++)
- use UList instead of stack >> overhead of creating new lists at each right traversals.
- depending solely on the tree >> lose of the node history
- counting the parentheses(hence the operations at first step, #TODO it had been a PROJECT !!!
           removing 2 steps from the iteration >> uncertainty raised of the order
           of ops.
           
@author: omarn
https://en.wikipedia.org/wiki/AVL_tree

# Overriding
Child implements a method that was inherited from parent in a new way.

#Overloading
Customize the behavior of Python operators for a class
    (e.g. __eq__()  is used to overload ==).
"""

class Node:
    def __init__(self,initdata, parent = None):
        self.data = initdata 
        self.next = None    #NOTE: for LLs
        self.parent = parent
        
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

class BinaryTree:
    def __init__(self,v):
        self.root = v
        self.right = None; self.left = None
        self.approach = "MISO SISO" #NOTE: better to be in the app.py
    
    def getLeftChild(self):
        return self.left
    
    def getRightChild(self):
        """returns the binary tree corresponding
to the right child of the current node."""
        return self.right
    
    def setRootVal(self,value):
        """stores the object in parameter val in
the current node."""
        self.root = value
    
    def getRootVal(self):
        
        return self.root
    
    def insertLeft(self,value):
        if self.left == None:
            self.left = BinaryTree(value)
        else:
            TT = BinaryTree(value)
            TT.left = self.left
            self.left = TT
        
    def insertRight(self,value):
        """ creates a new binary tree and
        installs it as the right child of the current node."""
        if self.right is None:
            self.right = BinaryTree(value)
        else:
            TT = BinaryTree(value)
            TT.right = self.right
            self.right = TT


"""
 If the current token is a ’(’, add a new node as the left
child of the current node, and descend to the left child.
2 If the current token is in the list [’+’,’-’,’/’,’*’], set
the root value of the current node to the operator
represented by the current token. Add a new node as the
right child of the current node and descend to the right
child.
3 If the current token is a number, set the root value of the
current node to the number and return to the parent.
4 If the current token is a ’)’, go to the parent of the current
node
"""            
if __name__ == "__main__":
    expression = "( 5 + 3 )"
    parse_tree = BinaryTree(Node(''))
    tokens = expression.strip().split()
    for token in tokens:
        if token == '(':
            parse_tree.insertLeft(Node('',parse_tree.root))
            parse_tree = parse_tree.getLeftChild()
        elif token in ['+','-','-','*']:
            parse_tree.insertRight(Node('',parse_tree.root))
            parse_tree = parse_tree.getRightChild()
        elif token.isdigit():
            parse_tree.setRootVal(Node(int(token)))
            parse_tree = parse_tree.getRootVal().parent
        elif token == ')':
            parse_tree = parse_tree.getRootVal().parent
    result = 0
    # leftC = parse_tree.getLeftChild()
    # rightC = parse_tree.getRightChild()
    # while rightC and leftC:
        # leftC = leftC.PROCEEDING LIKE THIS RESULTS IN 2 * 2 LINES
        #... INSIDE `WHILE` BLOCK.
        # pass
    
    import operator            
    def parsEval(parseTree):
        opers = {'+':operator.add, '-':operator.sub,
                 '*':operator.mul, '/':operator.truediv}
        leftC = parse_tree.getLeftChild()
        rightC = parse_tree.getRightChild()
        
        if leftC and rightC:
            fn = opers[parseTree.getRootVal()]
            return fn(parsEval(leftC), parsEval(rightC))
        else:
            return parseTree.getRootVal()
    
    print(parsEval(parse_tree))