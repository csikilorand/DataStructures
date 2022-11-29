class MyQueueLinkedList:
    class ListNode:
        def _init__(self):
            self.data = self.next = None

    def __init__(self):
        self.top = self.bottom = self.ListNode
        self.size = 0

    def __isNone__(self, data):
        return data is None

    def isEmpty(self):
        return self.size == 0

    def getSize(self):
        return self.size

    def enqueue(self, data):
        if self.__isEmpty__():
            self.top.data = data
            self.top.next = self.ListNode()
            self.size += 1
            return
        if self.__isNone__(data):
            raise ValueError("Empty data can not be used")
        tempNode = self.ListNode()
        tempNode.data = data
        self.top.next = tempNode
        self.top = tempNode
        self.size += 1

    def dequeue(self):
        if self.__isEmpty__():
            raise ValueError("Can not remove from empty queue")
        tempNode = self.bottom
        self.bottom = self.bottom.next
        self.size -= 1
        return tempNode

