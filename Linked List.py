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

    def len(self):
        count = 0
        pointer = self.head
        while pointer.nextNode != None:
            count = count + 1
            pointer = pointer.nextNode
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
********** Linked List **********
('HEAD DATA: ', 0, ' NEXT NODE: ', <__main__.Node instance at 0x10cc6e7a0>)

('DATA: ', 0, ' NEXT NODE: ', <__main__.Node instance at 0x10cc6e7a0>)
('DATA: ', 1, ' NEXT NODE: ', <__main__.Node instance at 0x10cc6e7e8>)
('DATA: ', 2, ' NEXT NODE: ', <__main__.Node instance at 0x10cc6e830>)
('DATA: ', 3, ' NEXT NODE: ', <__main__.Node instance at 0x10cc6e878>)
--------------------
('Length', 4)
--------------------
'''



