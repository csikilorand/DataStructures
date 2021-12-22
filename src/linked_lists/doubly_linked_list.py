from typing import TypeVar

T = TypeVar('T')

class DoublyLinkedList:
    class Node:
        def __init__(self, data: T):
            self.data = data
            self.next =None
            self.prev = None

    def __init__(self ):
        self.head = self.tail = None
        self.size = 0

    def getSize(self) -> int:
        return self.size

    def isEmpty(self) -> bool:
        return self.size == 0

    def display(self):
        trav = self.head
        while( trav):
            print('{}'.format(trav.data))
            trav = trav.next


    def addHead(self, element: T):
        if element is None:
            raise ValueError("Element must be not None")
        if self.head is None:
            self.head = self.tail = self.Node(element)
        else:
            newNode = self.Node(element)
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        self.size += 1

    def addTail(self, element: T):
        if self.head is None:
            self.addHead(element)
            return
        if element is None:
            raise ValueError("Element must be not None")
