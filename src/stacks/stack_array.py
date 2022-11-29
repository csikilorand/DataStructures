from array import array
"""Could not find that the module supports user-defined classes as elements"""

class StackArray:
    size:int
    items:array

    def __init__(self):
        self.items = array('i')

    def getSize(self):
        return len(self.items)

    @staticmethod
    def checkForValidElement(element):
        if element is None:
            raise ValueError('None type not accepted')

    def push(self, element):
        """Just int datatypes"""
        self.items.append(element)
        
    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[-1]