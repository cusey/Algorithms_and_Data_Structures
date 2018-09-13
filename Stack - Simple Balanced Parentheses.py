#python 3.5.2

'''
Simple Balanced Parentheses
Once you agree that a stack is the appropriate data structure for keeping the parentheses, 
the statement of the algorithm is straightforward. Starting with an empty stack, process 
the parenthesis strings from left to right. If a symbol is an opening parenthesis, push 
it on the stack as a signal that a corresponding closing symbol needs to appear later. 
If, on the other hand, a symbol is a closing parenthesis, pop the stack. As long as 
it is possible to pop the stack to match every closing symbol, the parentheses remain 
balanced. If at any time there is no opening symbol on the stack to match a closing 
symbol, the string is not balanced properly. At the end of the string, when all symbols 
have been processed, the stack should be empty. 
'''
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

                
def parChecker(symbolString):
    s=Stack()
    index = 0
    
    print('Length=',len(symbolString))
    
    while len(symbolString) -1 >= index:
        print('symbolString[',index,']=',symbolString[index])
        
        if symbolString[index] == '(':
            print('push:')
            s.push(symbolString[index])
            
        if symbolString[index] == ')':
            if s.isEmpty():
                print('Missing Left Parentheses')
                return False
            print('pop:')
            s.pop()
            
        index = index + 1
 
    return s.isEmpty()

		
print( parChecker('((()))') )
print('-'*20)
print( parChecker('((())') )
print('-'*20)
print( parChecker('()(())') )
print('-'*20)
print( parChecker(')') )
print('-'*20)


'''
OUTPUT:

Length= 6
symbolString[ 0 ]= (
push:
symbolString[ 1 ]= (
push:
symbolString[ 2 ]= (
push:
symbolString[ 3 ]= )
pop:
symbolString[ 4 ]= )
pop:
symbolString[ 5 ]= )
pop:
True
--------------------
Length= 5
symbolString[ 0 ]= (
push:
symbolString[ 1 ]= (
push:
symbolString[ 2 ]= (
push:
symbolString[ 3 ]= )
pop:
symbolString[ 4 ]= )
pop:
False
--------------------
Length= 6
symbolString[ 0 ]= (
push:
symbolString[ 1 ]= )
pop:
symbolString[ 2 ]= (
push:
symbolString[ 3 ]= (
push:
symbolString[ 4 ]= )
pop:
symbolString[ 5 ]= )
pop:
True
--------------------
Length= 1
symbolString[ 0 ]= )
Missing Left Parentheses
False
--------------------
'''


	