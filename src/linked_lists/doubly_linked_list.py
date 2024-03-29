from typing import TypeVar

T = TypeVar('T')

class DoublyLinkedList:
    class Node:
        data:T
        next:None
        prev:None
        def __init__(self, data: T):
            self.data = data
            self.next =None
            self.prev = None
    head:Node
    size:int
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

    def checkForNone(self, element: T):
        if element is None:
            raise ValueError("Element must be not None")


    def checkForValidIndex(self,  index: int):
        if index <0 or index >= self.getSize():
            raise ValueError("index must >0 and <size")


    def checkForEmptiness(self):
        if self.isEmpty():
            raise Exception("Can not remove from an empty List")

    def add(self, element: T):
        self.checkForNone(element)
        if self.head is None:
            self.addHead(element)
            return
        trav = self.head
        while trav.next:
            trav = trav.next
        newNode = self.Node(element)
        trav.next = newNode
        self.size += 1




    def addHead(self, element: T):
        self.checkForNone( element)
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
        self.checkForNone(element)
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
        self.checkForNone(element)
        self.checkForValidIndex(index)
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
        self.checkForNone(element)
        self.checkForNone(new_element)
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
        self.checkForNone(element)
        self.checkForNone(new_element)
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
        if  self.head.next is not None:
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1
        else:
            self.head.next =  self.tail.prev = None
            self.size  =0

    def removeTail(self):
        self.checkForEmptiness()
        if self.tail.prev is not None:
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1
        else:
            self.tail.prev = None
            self.size = 0

    def removeAtIndex(self, index: int):
        self.checkForValidIndex(index)
        self.checkForEmptiness()
        if index ==0:
            self.removeHead()
            return
        if index == self.size-1:
             self.removeTail()
             return
        i: int =1
        trav= self.head.next
        while trav:
            i += 1
            trav= trav.next
            if i == index:
                trav.prev.next = trav.next
                trav.next.rev = trav.prev
                trav.next = None
                trav.prev = None
                self.size -= 1
                return

    def removeElement(self, element: T):
        self.checkForEmptiness()
        self.checkForEmptiness()
        if self.head.data == element:
            self.removeHead()
            return
        if self.tail.data == element:
            self.removeTail()
            return
        trav = self.head.next
        while trav.data != element :
            if trav.next == self.tail:
                raise ValueError("Element not found")
            trav = trav.next
        trav.prev.next = trav.next
        trav.next.prev = trav.prev
        trav.next = trav.prev = None
        self.size -= 1

    def getIndexOfElement(self, element: T) -> int:
        self.checkForNone(element)
        i: int = 0
        trav = self.head
        while trav.data != element:
             i += 1
             if (trav == self.tail) and  (trav.data != element):
                raise ValueError("Element not found")
        trav = trav.next
        return i

    def getElementByIndex(self, index:int) -> T:
        self.checkForValidIndex(index)
        i: int =0
        trav = self.head
        while i != index:
            trav= trav.next
        return trav.data




