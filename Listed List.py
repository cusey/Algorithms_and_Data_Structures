#python 3.5.2

'''
Linked List
'''

debugList = []

class Node:
    def __init__(self, data=None):
        self.dataNode = data
        self.nextNode = None
        
class LinkedList:
    def __init__(self, debug=False):
        self.head = None
        self.tail = None
        self.debug = debug
        
    def add(self, data=None):
         
         if self.debug:
             print('add(',data,')') 
                
         temp = Node(data)

         if self.head == None:
             if self.debug:
                print('HEAD NODE')
             self.head = temp
             self.tail = self.head.nextNode
         elif self.head.nextNode == None:
             if self.debug:
                print('OTHER NODE')     
             
        
    def stepPrint(self):
        print(' ');
        pointer = self.head
        while pointer is not None:
            if pointer.nextNode == None:
                print (pointer.dataNode, ' NEXT None')
            else:
                print (pointer.dataNode, ' NEXT ', pointer.nextNode.dataNode)
            pointer = pointer.nextNode
            
#TESTING The stepPrint(self) Method

list = []

list.append( Node(0) )
list.append( Node(1) )
list.append( Node(2) )

list[0].nextNode = list[1]
list[1].nextNode = list[2]

link1 = LinkedList()
link1.head = list[0]

link1.stepPrint() 

print('-'*20)

#TESTING The add(self, data=None) Method
     
link2 = LinkedList(True)

link2.add(0)
link2.add(1)  


link2.stepPrint()
print('-'*20)

