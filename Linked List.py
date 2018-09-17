#python 3.5.2

print ( '********** Linked List **********' )

class Node:
    def __init__(self, data=None):
        self.dataNode = data
        self.nextNode = None

class LinkedList:
    def __init__(self, debug=False):
        self.head = None

    def append(self, data=None):

        temp = Node(data)

        if self.head == None:
            self.head = temp
        else:
            pointer = self.head
            while pointer.nextNode != None:
                pointer = pointer.nextNode
            pointer .nextNode = temp

    def showLinkedList(self):
        pointer = self.head
        print('HEAD DATA: ', pointer.dataNode, ' NEXT NODE: ', pointer.nextNode)
        print('')

        while pointer.nextNode != None:
            print('DATA: ',pointer.dataNode, ' NEXT NODE: ', pointer.nextNode)
            pointer = pointer.nextNode
            
        print('DATA: ',pointer.dataNode, ' NEXT NODE: ', pointer.nextNode)

    def len(self):
        count = 0
        pointer = self.head
        while pointer.nextNode != None:
            count = count + 1
            pointer = pointer.nextNode
            
        count = count + 1
        return count


link = LinkedList()

link.append(0)
link.append(1)
link.append(2)
link.append(3)
link.append(4)

link.showLinkedList()

print('-'*20)

print('Length', link.len() )

print('-'*20)
'''
OUTPUT:

********** Linked List **********
HEAD DATA:  0  NEXT NODE:  <__main__.Node object at 0x7f5335f8e828>

DATA:  0  NEXT NODE:  <__main__.Node object at 0x7f5335f8e828>
DATA:  1  NEXT NODE:  <__main__.Node object at 0x7f5335f8e860>
DATA:  2  NEXT NODE:  <__main__.Node object at 0x7f5335f8e898>
DATA:  3  NEXT NODE:  <__main__.Node object at 0x7f5335f8e8d0>
DATA:  4  NEXT NODE:  None
--------------------
Length 5
--------------------
'''


