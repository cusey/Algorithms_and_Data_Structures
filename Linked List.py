#python 3.5.2

print ( '********** Linked List **********' )

class Node:
    def __init__(self, data=None):
        self.dataNode = data
        self.nextNode = None

class LinkedList:
    def __init__(self, debug=False):
        self.head = None

    def add(self, data=None):

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


link = LinkedList()

link.add(0)
link.add(1)
link.add(2)
link.add(3)
link.add(4)

link.showLinkedList()

print('-'*20)

'''
OUTPUT:
********** Linked List **********
('HEAD DATA: ', 0, ' NEXT NODE: ', <__main__.Node instance at 0x10ab246c8>)

('DATA: ', 0, ' NEXT NODE: ', <__main__.Node instance at 0x10ab246c8>)
('DATA: ', 1, ' NEXT NODE: ', <__main__.Node instance at 0x10ab24710>)
('DATA: ', 2, ' NEXT NODE: ', <__main__.Node instance at 0x10ab24758>)
('DATA: ', 3, ' NEXT NODE: ', <__main__.Node instance at 0x10ab247a0>)
--------------------
'''



