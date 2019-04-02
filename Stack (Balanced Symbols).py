#python 3.5.2


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
'''
Checking see if you have left symbol so you can pudh it on the stack
'''                

def isLeftSymbol(symbol):
    if (symbol == '(') or (symbol == '{') or (symbol == '['):
        return True
    return False


'''
print( isLeftSymbol('(') )
print( checkLeftSymbol('{') )
print( checkLeftSymbol('[') )

print( isLeftSymbol(')') )
print( isLeftSymbol('}') )
print( isLeftSymbol(']') )
'''

def isBalancedEquation(symbol): 
    s=Stack()
    index = 0
    
    while len(symbol)-1 >= index:
        print()
        
        if isLeftSymbol(symbol[index]):
            print('push: symbol[',index,'] = ',symbol[index])
            s.push(symbol[index])
        else:
            print('pop: symbol[',index,'] = ',symbol[index])
            leftSymbol = s.peek()
            
            if leftSymbol == symbol[index]:
                print('No responding symbol')
                return False
            
        index = index + 1
 
    return s.isEmpty()
    

print('BALANCED EQUATION')
print( isBalancedEquation('[(){()}]()') ) 
print('-'*20)
print('UN-BALANCED EQUATION')
print( isBalancedEquation('(){()}]()') ) 
print('-'*20)

'''
BALANCED EQUATION

push: symbol[ 0 ] =  [

push: symbol[ 1 ] =  (

pop: symbol[ 2 ] =  )

push: symbol[ 3 ] =  {

push: symbol[ 4 ] =  (

pop: symbol[ 5 ] =  )

pop: symbol[ 6 ] =  }

pop: symbol[ 7 ] =  ]

push: symbol[ 8 ] =  (

pop: symbol[ 9 ] =  )
False
--------------------
UN-BALANCED EQUATION

push: symbol[ 0 ] =  (

pop: symbol[ 1 ] =  )

push: symbol[ 2 ] =  {

push: symbol[ 3 ] =  (

pop: symbol[ 4 ] =  )

pop: symbol[ 5 ] =  }

pop: symbol[ 6 ] =  ]

push: symbol[ 7 ] =  (

pop: symbol[ 8 ] =  )
False
--------------------
'''


	
