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
        newNode = self.Node(element)
        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode
        self.size += 1

    def addAtIndex(self, index: int, element:T):
        if index ==0:
            self.addHead(element)
            return
        if index == self.size-1:
            self.addTail(element)
            return
        if element is None:
            raise ValueError("Element must be not None")
        if index <0 and index >= self.size:
            raise ValueError("index must <0 and >=size")
        trav = self.head.next
        i:int =1
        while i != index:
            i += 1
            trav= trav.next
        newNode = self.Node(element)
        newNode.next = trav
        newNode.prev = trav.prev
        trav.prev.next = newNode
        trav.prev = newNode
        self.size += 1

    def addAfterElement(self, element: T, new_element: T):
        if element is None or new_element is None:
            raise ValueError("Element must be not None")
        if element == self.tail:
            self.addTail(new_element)
            return
        if self.size ==0 :
            self.addHead(new_element)
            return
        trav = self.head
        while trav:
            if trav.data == element:
                newNode = self.Node(new_element)
                newNode.prev = trav
                newNode.next = trav.next
                trav.next = newNode
                self.size += 1
                return
            trav = trav.next
        raise ValueError("Element not found")

    def addBeforeElement(self, element: T, new_element: T):
        if element is None or new_element is None:
            raise ValueError("Element must be not None")
        if self.size ==0 :
            self.addHead(new_element)
            return
        if element == self.head.data:
            self.addHead(new_element)
            return
        if element == self.tail.data:
            newNode = self.Node(new_element)
            newNode.prev = self.tail.prev
            self.tail.prev = newNode
            newNode.next = self.tail
            self.size += 1
            return
        trav= self.head.next
        while trav:
            if trav.data == element:
                newNode = self.Node(new_element)
                newNode.prev = trav.prev
                newNode.next = trav
                trav.prev.next =newNode
                self.size += 1
                return
        raise ValueError("Element not found")

    def removeHead(self):
        if self.isEmpty():
            raise Exception("Can not remove from an empty List")
        pass
    def removeTail(self):
        if self.isEmpty():
            raise Exception("Can not remove from an empty List")
        
        self.size -= 1
    def removeAtIndex(self, index: int):
        pass
    def removeAfterElement(self, element: T):
        pass
    def removeBeforeElement(self, element: T):
        pass
