#python 3.5.2

class Deque: 
     def __init__(self): 
         self.items = [] 
  
     def isEmpty(self): 
         return self.items == [] 
  
     def addFront(self, item): 
         self.items.append(item) 
  
     def addRear(self, item): 
         self.items.insert(0,item) 
  
     def removeFront(self): 
         return self.items.pop() 
  
     def removeRear(self): 
         return self.items.pop(0) 
  
     def size(self): 
         return len(self.items) 
  
d=Deque() 
dashNo = 40
print('Is Empty:', d.isEmpty()) 
print('-'*dashNo)
d.addRear(4) 
print('addRear(4) ',d.items)
print('-'*dashNo)
d.addRear('dog') 
print('addRear("dog") ',d.items)
print('-'*dashNo)
d.addFront('cat') 
print('addFront("cat")  ',d.items)
print('-'*dashNo)
d.addFront(True) 
print('addFront(True)  ',d.items)
print('-'*dashNo)

print('Size: ',d.size()) 
print('Is Empty:',d.isEmpty()) 
print('-'*dashNo)

d.addRear(8.4) 
print('addRear(8.4)   ',d.items)
print('-'*dashNo)

print(d.removeRear())
print('removeRear:   ',d.items)
print('-'*dashNo)
print(d.removeFront()) 
print('removeFront:   ',d.items)
print('-'*dashNo)

'''
OUTPUT:

Is Empty: True
----------------------------------------
addRear(4)  [4]
----------------------------------------
addRear("dog")  ['dog', 4]
----------------------------------------
addFront("cat")   ['dog', 4, 'cat']
----------------------------------------
addFront(True)   ['dog', 4, 'cat', True]
----------------------------------------
Size:  4
Is Empty: False
----------------------------------------
addRear(8.4)    [8.4, 'dog', 4, 'cat', True]
----------------------------------------
8.4
removeRear:    ['dog', 4, 'cat', True]
----------------------------------------
True
removeFront:    ['dog', 4, 'cat']
----------------------------------------
'''


