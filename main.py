print ( '********** Linked List **********' )

class Node:
    def __init__(self, data=None):
        self.dataNode = data
        self.nextNode = None

class LinkedList:
    def __init__(self, debug=False):
        self.head = None
        self.count = 0
        self.pointer = None

    def append(self, data=None):

        temp = Node(data)

        if self.head == None:
            self.head = temp
        else:
            pointer = self.head
            while pointer.nextNode != None:
                pointer = pointer.nextNode
            pointer .nextNode = temp

    def printer(self):
        print('DATA: ', self.pointer.dataNode, ' NEXT NODE: ', self.pointer.nextNode)

        self.step(self, self.printer())

    def showLinkedList(self):
        self.pointer = self.head
        print('HEAD DATA: ', self.pointer.dataNode, ' NEXT NODE: ', self.pointer.nextNode)
        print('')



    def len(self):
        count = 0
        counter = lambda: self.count + 1
        self.step(counter)
        return count

    def step(self,excute):
        pointer = self.head
        while pointer.nextNode != None:
            excute()
            pointer = pointer.nextNode


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
