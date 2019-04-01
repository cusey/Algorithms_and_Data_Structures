#python 3.5.2

class Stack:

    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        self.items == []
        
    def push(self, item):
        self.items.append(item)

    def pop(self):
         return self.items.pop()

    def peek(self):
         return self.items[len(self.items)-1]

    def size(self):
         return len(self.items)


def converDecToBinary(decimalNo, debug):

    s = Stack()
    temp = decimalNo
    remainder = 0
    pushNo = 0
    
    result = ""

    while temp > 0:
        remainder = temp%2
        if remainder == 0:
            if debug :
                pushNo = 0
            s.push('0')
        else:
            if debug :
                pushNo = 1
            s.push('1')
            
        temp = temp//2
        if debug :
            print( temp , 'remainder', pushNo)
            print( s.items )
            

        print('-'*20)
        
    print('REVERSE THE NUMBERS')   
        
    while  s.size() != 0:
        if debug :
            print( s.items )
        result = result + s.pop()
        
    print('-'*20)
        
    return result
        
 
        
print( converDecToBinary(6 , True)  )
print('-'*20)

'''
3 remainder 0
['0']
--------------------
1 remainder 1
['0', '1']
--------------------
0 remainder 1
['0', '1', '1']
--------------------
REVERSE THE NUMBERS
['0', '1', '1']
['0', '1']
['0']
--------------------
110
--------------------
'''
