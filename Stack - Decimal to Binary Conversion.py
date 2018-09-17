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
    remaider = 0
    pushNo = 0
    
    result = ""

    while temp > 0:
        remaider = temp%2
        if remaider == 0:
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
            
    while  s.size() != 0:
        if debug :
            print( s.items )
        result = result + s.pop()
        
    return result
        
 
        
print( converDecToBinary(294 , True)  )
print('-'*20)
