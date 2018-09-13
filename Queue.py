#python 3.5.2

'''
A queue is an ordered collection of items where the addition of new items happens at one end, called the “rear,” 
and the removal of existing items occurs at the other end, commonly called the “front.” As an element enters the 
queue it starts at the rear and makes its way toward the front, waiting until that time when it is the next 
element to be removed.

The most recently added item in the queue must wait at the end of the collection. The item that has been in the
collection the longest is at the front. This ordering principle is sometimes called FIFO, first-in first-out. 
It is also known as “first-come first-served.”

'''

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
        
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

'''
OUTPUT:

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
'''

