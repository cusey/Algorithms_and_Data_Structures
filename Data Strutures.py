#python 3.5.2

# I am just using the INSERT and POP to write the queue and stack

class Stack:
    def __init__(self):
        self.items = []
        
    def size(self):
        return len(self.items)
    
    def push(self, data):
    #THE ONLY BETWEEN STACK AND QUEUE
        self.items.insert(len(self.items),data)
       
    def pop(self):
        return self.items.pop( len(self.items) - 1 ) 
    
    def peek(self):
        return self.items[ len(self.items) - 1 ]
    
    def isEmpty(self):
        return self.items == []
    
class Qeueu:
    def __init__(self):
        self.items = []
        
    def size(self):
        return len(self.items)
    
    def enqueue(self, data):
    #THE ONLY BETWEEN STACK AND QUEUE
        self.items.insert(0,data)
       
    def dequeue(self):
        return self.items.pop( len(self.items) - 1 ) 
    
    def peek(self):
        return self.items[ len(self.items) - 1 ]
    
    def isEmpty(self):
        return self.items == []
    
print ( '-'*20 )
print ( 'STACK' )
print ( '-'*20 )

s=Stack()

print('isEmpty:',s.isEmpty())
print('-'*20)
s.push(4)
print('push(4): s=',s.items)
s.push('dog')
print('push(dog): s=',s.items)
s.push(8.4)
print('push(8.4): s=',s.items)
print('s=',s.items)
print('-'*20)
print('peek:',s.peek())
print('-'*20)
s.push(True)
print('push(True): s=',s.items)
print('s=',s.items)
print('size:',s.size())
print('-'*20)
print('s=',s.items)
print('pop:',s.pop())
print('pop:',s.pop())
print('s=',s.items)
print('size:',s.size())

print ( '-'*20 )
print ( 'STACK' )
print ( '-'*20 )


print ( '-'*20 )
print ( 'QUEUE' )
print ( '-'*20 )

q=Queue()

print('isEmpty:',q.isEmpty())
print('-'*20)
q.enqueue(4)
print('enqueue(4): q=',q.items)
q.enqueue('dog')
print('enqueue(dog): q=',q.items)
q.enqueue(8.4)
print('enqueue(8.4): q=',q.items)
print('-'*20)
print('q=',q.items)
print('dequeue:',q.dequeue())
print('q=',q.items)
print('dequeue:',q.dequeue())
print('q=',q.items)

print ( '-'*20 )
print ( 'QUEUE' )
print ( '-'*20 )



'''
OUTPUT

--------------------
STACK
--------------------
isEmpty: True
--------------------
push(4): s= [4]
push(dog): s= [4, 'dog']
push(8.4): s= [4, 'dog', 8.4]
s= [4, 'dog', 8.4]
--------------------
peek: 8.4
--------------------
push(True): s= [4, 'dog', 8.4, True]
s= [4, 'dog', 8.4, True]
size: 4
--------------------
s= [4, 'dog', 8.4, True]
pop: True
pop: 8.4
s= [4, 'dog']
size: 2
--------------------
STACK
--------------------
--------------------
QUEUE
--------------------
isEmpty: True
--------------------
enqueue(4): q= [4]
enqueue(dog): q= ['dog', 4]
enqueue(8.4): q= [8.4, 'dog', 4]
--------------------
q= [8.4, 'dog', 4]
dequeue: 4
q= [8.4, 'dog']
dequeue: dog
q= [8.4]
--------------------
QUEUE
--------------------

'''