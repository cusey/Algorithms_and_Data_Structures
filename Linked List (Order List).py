#python 3.5.2

print ( 'Linked List (Order List)' )

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
       
        newNode = Node(data)
        self.count = self.count + 1 

        if self.head == None:
            #Creating new Linked List
            self.head = newNode
        else:
            pointer = self.head
            
            
            if pointer.getData() > data:
            #Insert before head
                oldHead = pointer
                self.head  = newNode
                self.head.setNext(oldHead)
            
            else:
            #Insert node after head  
                while pointer.getNext() != None and self.peak(pointer).getData() < data:
                #Finding correct Node
                    pointer = pointer.getNext()
                
                if  pointer.getNext() != None:  
                #In middle of Linked List
                    newNode.setNext(pointer.getNext())
 
                pointer.setNext(newNode)

        self.showLinkedList()     

            
    def peak(self, pointer):
        if pointer == None:
            return None
        else:
            return pointer.getNext() 

    def showLinkedList(self):
        if  self.len()!= 0 :
            pointer = self.head
            while pointer.getNext() != None:
                self.printRow(pointer)
                pointer = pointer.getNext() 
            
            self.printRow(pointer)
        else:
            print('Empty Linked List')
            
            
        print('-'*20)


    def len(self):
        return self.count


link = LinkedList()

link.append(51)
link.append(23)
link.append(32)
link.append(91)
link.append(12)
link.append(63)


print('Length: ', link.len() )

print('-'*20) 

'''
OUTPUT:

Linked List (Order List)
--------------------
DATA:  51  NEXT NODE:  None
--------------------
DATA:  23  NEXT NODE:  <__main__.Node object at 0x7fdceb5e2b70>
DATA:  51  NEXT NODE:  None
--------------------
DATA:  23  NEXT NODE:  <__main__.Node object at 0x7fdceb5e2c88>
DATA:  32  NEXT NODE:  <__main__.Node object at 0x7fdceb5e2b70>
DATA:  51  NEXT NODE:  None
--------------------
DATA:  23  NEXT NODE:  <__main__.Node object at 0x7fdceb5e2c88>
DATA:  32  NEXT NODE:  <__main__.Node object at 0x7fdceb5e2b70>
DATA:  51  NEXT NODE:  <__main__.Node object at 0x7fdceb5e2cf8>
DATA:  91  NEXT NODE:  None
--------------------
DATA:  12  NEXT NODE:  <__main__.Node object at 0x7fdceb5e2c18>
DATA:  23  NEXT NODE:  <__main__.Node object at 0x7fdceb5e2c88>
DATA:  32  NEXT NODE:  <__main__.Node object at 0x7fdceb5e2b70>
DATA:  51  NEXT NODE:  <__main__.Node object at 0x7fdceb5e2cf8>
DATA:  91  NEXT NODE:  None
--------------------
DATA:  12  NEXT NODE:  <__main__.Node object at 0x7fdceb5e2c18>
DATA:  23  NEXT NODE:  <__main__.Node object at 0x7fdceb5e2c88>
DATA:  32  NEXT NODE:  <__main__.Node object at 0x7fdceb5e2b70>
DATA:  51  NEXT NODE:  <__main__.Node object at 0x7fdceb5e2dd8>
DATA:  63  NEXT NODE:  <__main__.Node object at 0x7fdceb5e2cf8>
DATA:  91  NEXT NODE:  None
--------------------
Length:  6
--------------------
'''
       
