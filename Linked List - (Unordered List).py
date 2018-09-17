#python 3.5.2

print ( 'Linked List (Unorder List)' )

print('-'*20)

class Node:
    def __init__(self, data=None):
        self.dataNode = data
        self.nextNode = None
        
    def getData(self):
        return self.dataNode
        
    def setData(self, data=None):
        self.dataNode = data
    
    def getNext(self):
        return self.nextNode
        
    def setNext(self, next=None):
        self.nextNode = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0
        
    def printRow(self, pointer):
        print('DATA: ', pointer.getData(), ' NEXT NODE: ', pointer.getNext() )
            
    def append(self, data=None):

        temp = Node(data)
        self.count = self.count + 1 

        if self.head == None:
            self.head = temp
        else:
            pointer = self.head
            while pointer.getNext() != None:
                pointer = pointer.getNext() 
            pointer.nextNode = temp

    def showLinkedList(self):
        pointer = self.head
        while pointer.getNext() != None:
            self.printRow(pointer)
            pointer = pointer.getNext() 
            
        self.printRow(pointer)


    def len(self):
        return self.count


link = LinkedList()

link.append(51)
link.append(23)
link.append(91)
link.append(12)
link.append(32)

link.showLinkedList()

print('-'*20)

print('Length: ', link.len() )

print('-'*20)

'''
OUTPUT:

Linked List (Unorder List)
--------------------
DATA:  51  NEXT NODE:  <__main__.Node object at 0x7fc19d92eb38>
DATA:  23  NEXT NODE:  <__main__.Node object at 0x7fc19d92eb70>
DATA:  91  NEXT NODE:  <__main__.Node object at 0x7fc19d92eba8>
DATA:  12  NEXT NODE:  <__main__.Node object at 0x7fc19d92ebe0>
DATA:  32  NEXT NODE:  None
--------------------
Length:  5
--------------------

'''
