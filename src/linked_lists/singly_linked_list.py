from typing import TypeVar

T = TypeVar('T')
class SinglyLinkedList:
    class Node:
        data:T
        next:None
        def __init__(self, data: T):
            self.data = data
            self.next = None

    head:Node
    tail:Node
    size:int
    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def getSize(self) -> int:
        return self.size

    def isEmpty(self) -> bool:
        return self.size == 0

    def contains(self, element: T) -> bool:
        if element is not None:
            raise ValueError('element must be not null')
        trav = self.head
        while trav:
            if trav.data == element:
                return True
            trav = trav.next
        return False

    def clear(self):
        if self.isEmpty():
            return
        trav = self.head
        temp = trav
        while trav:
            trav = trav.next
            temp.data = temp.next = None
            temp = trav
        self.size = 0

    def display(self):
        trav = self.head
      #  print(type(trav))
        while (trav):
            print("{} ".format(trav.data))
            trav = trav.next

    def addHead(self, element: T):
        if element is None:
            raise ValueError("Element must be not None")
        if self.head is None:
            self.head = self.Node(element)
            self.head.next = None
            self.tail = self.head
            self.size += 1
        else:
            newNode = self.Node(element)
            newNode.next = self.head
            self.head = newNode
            self.size += 1
    def add(self, element: T):
        if element is None:
            raise ValueError("Element must be not None")
        if self.isEmpty():
            self.addHead(element)
            return
        trav = self.head
        while trav.next:
            trav= trav.next
        newNode = self.Node(element)
        trav.next = newNode
        self.tail = newNode
        self.size += 1
    def addTail(self, element: T):
        if self.head  is None:
            self.addHead(element)
            return
        if element is None:
            raise ValueError("Element must be not None")
        newNode = self.Node(element)
        self.tail.next = newNode
        self.tail = newNode
        self.size += 1

    def addAtIndex(self, element: T, index: int):
        if element is None:
            raise ValueError("Data must be not None")
        if index < 0 or index > self.size:
            raise ValueError("index must be >0 and <size")
        if index == self.size:
            self.addTail(element)
            return
        if index == 0:
            self.addHead(element)
            return
        i:int = 1
        trav = self.head
        while i != index:
            i += 1
            trav = trav.next
        newNode = self.Node(element)
        newNode.next = trav.next
        trav.next = newNode
        self.size += 1

    def addAfterElement(self, element: T, new_element: T):
        if element is None:
            raise ValueError("element must be not null")
        if element == self.head.data:
            self.addHead(new_element)
            return
        if element == self.tail.data:
            self.addTail(new_element)
            return
        trav = self.head.next
        while trav.data != element:
            trav = trav.next
            if trav == self.tail:
                raise ValueError("Element not found")
        newNode = self.Node(new_element)
        newNode.next = trav.next
        trav.next = newNode
        self.size += 1

    def getIndexByElement(self, element: T) -> int:
        if element is None:
            raise ValueError("The searched element must be not null")
        if element == self.head.data:
            return 0
        if element == self.tail.data:
            return self.size
        trav = self.head.next
        i = 2
        while trav:
            if trav.data == element:
                return i
            trav = trav.next
            i += 1
        return -1

    def getElementByIndex(self, index: int) -> T:
        if index < 0 or index >= self.size:
            raise ValueError("only valid indexes: >0 and <size")
        if index == 0:
            return self.head.data
        if index == self.size-1:
            return self.tail.data
        i = 1
        trav = self.head.next
        while i != index:
            trav = trav.next
            i += 1
        return trav.data

    def peekHead(self) -> T:
        return self.head.data

    def peekTail(self) -> T:
        return self.tail.data

    def removeHead(self):
        tempNode = self.head
        self.head = self.head.next
        tempNode.next = None
        self.size -= 1

    def removeTail(self):
        if self.isEmpty():
            raise ValueError("Can not remove from empty list")
        trav = self.head
        while trav.next is not self.tail:
            trav= trav.next
        self.tail = trav
        self.tail.next = None
        self.size -= 1

    def removeByIndex(self, index: int) :
        """Indexing starts from 0"""
        if index <0 or index > self.size:
            raise ValueError("Index mut be  >0 and <size")
        if index == 0:
            self.removeHead()
            return
        if index == self.size:
            self.removeTail()
            return
        i:int =0
        trav = self.head
        while i != index:
            if i+1 == index:
                temp = trav.next
                trav.next = temp.next
                temp.next = None
                self.size -= 1
                return
            trav = trav.next
            i += 1


    def removeByElement(self, element: T):
        if element is None:
            raise ValueError("Element must be not NoneType")
        if element == self.head.data:
            self.removeHead()
            return
        if element == self.tail.data:
            self.removeTail()
            return
        trav = self.head
        while trav:
            if trav.next.data == element:
                temp = trav.next
                trav.next = temp.next
                temp.next = None
                self.size -= 1
                return
            trav= trav.next
        raise ValueError("Element not found the list")