#python 3.5.2

print ( 'Linked List' )

print('-'*20)

class Node:
    def __init__(self, data=None):
        self.dataNode = data
        # Pointer to the next object in the Link List
        self.nextNode = None
        
    def get_dataNode(self):
        return self.dataNode

class LinkedList:
    def __init__(self):
        self.head = None
        self.pointer = None
        self.count = 0
    '''
    This is No Operation method it is used when you want to move the the next node but
    you do not have no method you want to execute.
    ''' 
    def nop(*args):
        pass
    
    def increaseByOne(self):
        self.count = self.count +1
        
    def printRow(self):
        if self.pointer.nextNode == None :
            print('DATA: ', self.pointer.dataNode, 'NEXT NODE DATA: None')
        else:
            print('DATA: ', self.pointer.dataNode, 'NEXT NODE DATA: ', self.pointer.nextNode.dataNode ) 
        
        
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
        #Prints the last node
        self.printRow()

    #This method counts each node when it is called
    def len(self):
        self.step( self.increaseByOne )
        #Need to add one to count because does not count the last node
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
Linked List
--------------------
DATA:  0 NEXT NODE DATA:  1
DATA:  1 NEXT NODE DATA:  2
DATA:  2 NEXT NODE DATA:  3
DATA:  3 NEXT NODE DATA:  4
DATA:  4 NEXT NODE DATA: None
--------------------
Length:  5
--------------------
'''
