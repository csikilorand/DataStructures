from typing import TypeVar
T = TypeVar('T')

class StackLinkedList:
    class Node:
        def __init__(self, data: T):
            self.data = data
            self.next = None

    def __init__(self):
        self.top = None
        self.size = 0

    def checkforNone(self, element: T ):
        if element is None:
            raise ValueError("Element must be not NONE")

    def isEmpty(self):
        return self.size == 0

    def push(self, element: T):
        self.checkforNone(element)
        if self.top is None:
            self.top = self.Node(element)
        else:
            newNode = self.Node(element)
            newNode.next = self.top
            self.top = newNode
        self.size += 1

    def getSize(self):
        return self.size

    def __repr__(self):
        return f"Element: {self.top.data}"

    def peek(self):
        if self.isEmpty():
            raise ValueError("The stack is empty")
        return self.top.data



    def pop(self):

        if self.isEmpty():
            raise ValueError("Can not remove from empty stack")
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.size -= 1
        return self.top