#python 3.5.2

class Stack:
    def __init__(self):
        self.items = []
        
    def size(self):
        return len(self.items)
    
    def push(self, data):
        self.items.insert(len(self.items),data)
       
    def pop(self):
        return self.items.pop( len(self.items) - 1 ) 
    
    def peek(self):
        return self.items[ len(self.items) - 1 ]
    
    def isEmpty(self):
        return self.items == []
    
    
    
def convertBase(number, base):
    
    convertString = '0123456789ABCDEF'
    s = Stack()
    
    result = ''
    
    while number != 0:
        print( ' {} {}'.format(convertString [number % base ] , result)  ) 
        s.push( convertString [number % base ] )
        number = number // base
     
    while not s.isEmpty() :  
        result = result + s.pop() 
        
    return result
    
 
def recConvertBase(number, base, stackObj ):
    convertString = '0123456789ABCDEF'
    result = ''
    
    if number != 0:
       print(' recConvertBase( {} ,{})  convertString [{}] = {} result = {} )'.format(number // base , base , number % base  , convertString [number % base ] , result) ) 
       stackObj.push( convertString [number % base ] )
       return result + recConvertBase(number // base, base,  stackObj) 
    else:
        
    
        print(' number = {}, stack size = {}'.format(number, stackObj.size() )  ) 
        
        while stackObj.size() != 0 : 
            popValue = stackObj.pop()
            result = result + popValue
            print( 'pop() : {} result = {}'.format( popValue , result) )
        return result
        
    return result      
          

print('-'*20)         
           
print( convertBase(48879, 16) ) 

print('-'*20) 

s = Stack()
print (recConvertBase(48879, 16, s) ) 

print('-'*20)

'''
OUTPUT:

--------------------
 F 
 E 
 E 
 B 
BEEF
--------------------
 recConvertBase( 3054 ,16)  convertString [15] = F result =  )
 recConvertBase( 190 ,16)  convertString [14] = E result =  )
 recConvertBase( 11 ,16)  convertString [14] = E result =  )
 recConvertBase( 0 ,16)  convertString [11] = B result =  )
 number = 0, stack size = 4
pop() : B result = B
pop() : E result = BE
pop() : E result = BEE
pop() : F result = BEEF
BEEF
--------------------
'''



