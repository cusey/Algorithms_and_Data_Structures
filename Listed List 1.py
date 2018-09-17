#python 3.5.2

print ( 'Linked List' )

print('-'*20)

class Node:
    def __init__(self, data=None):
        self.dataNode = data
        self.nextNode = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.pointer = None
        self.count = 0
        
    def nop(*args):
        pass
    
    def increaseByOne(self):
        self.count = self.count +1
        
    def printRow(self):
        print('DATA: ', self.pointer.dataNode, ' NEXT NODE: ', self.pointer.nextNode)
        
    def step(self,excute):
        self.pointer = self.head
        while self.pointer.nextNode != None:
            excute()
            self.pointer = self.pointer.nextNode
            
    def append(self, data=None):

        temp = Node(data)

        if self.head == None:
            self.head = temp
        else:
            self.step( self.nop )
            self.pointer.nextNode = temp

    def showLinkedList(self):
        self.pointer = self.head
        self.step( self.printRow )
        self.printRow()

    def len(self):
        self.step( self.increaseByOne )
        self.increaseByOne()
        return self.count


link = LinkedList()

link.append(0)
link.append(1)
link.append(2)
link.append(3)
link.append(4)

link.showLinkedList()

print('-'*20)

print('Length: ', link.len() )

print('-'*20)

'''
OUTPUT:
Linked List
--------------------
DATA:  0  NEXT NODE:  <__main__.Node object at 0x7fe374c0a908>
DATA:  1  NEXT NODE:  <__main__.Node object at 0x7fe374c0a940>
DATA:  2  NEXT NODE:  <__main__.Node object at 0x7fe374c0a978>
DATA:  3  NEXT NODE:  <__main__.Node object at 0x7fe374c0a9b0>
DATA:  4  NEXT NODE:  None
--------------------
Length:  5
--------------------
'''