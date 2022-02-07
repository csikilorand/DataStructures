def testLinked_list():
    from linked_lists import singly_linked_list
    myList =singly_linked_list.SinglyLinkedList()
    myList.addHead(0)
    myList.addHead(1)
    myList.addTail(2)
    myList.addAtIndex(element=99, index=1)
    myList.addAtIndex(element=990, index=4)
    myList.addAtIndex(element=9910, index=5)
    myList.display()
    print('Size:' + str(myList.getSize()))
    print("Now removing:")
    #myList.removeHead()
    #myList.removeTail()
    #myList.removeByIndex(index=2)
    myList.removeByElement(element= 990)

    #print('Element: ' + str(myList.getElementByIndex(3)))
  #  print('Size:' + str(myList.getSize()))
    myList.display()

    print('Size:' + str(myList.getSize()))

def testDoublyLinkedList():
    from linked_lists import doubly_linked_list
    myList = doubly_linked_list.DoublyLinkedList()
    myList.addHead(0)
    myList.addHead(1)
    myList.addHead(100)
    myList.addTail(99)
    myList.addTail(990)
    myList.addAtIndex(2, -90)
    myList.addAtIndex(2, -50)
    myList.addAfterElement(-90, 299)
    myList.addBeforeElement(1, 600)
    print("Size: " + str(myList.getSize()))
    myList.display()
    print("Now removing part...\n")
    myList.removeHead()
    myList.removeTail()
    print("Size: " + str(myList.getSize()))
    myList.display()
    myList.removeAtIndex(3)
    myList.removeAtIndex(2)
    myList.removeAtIndex(myList.getSize()-1)
    print("Size: " + str(myList.getSize()))
    myList.display()

def testStackLinkedList():
    from stacks import stack_linked_list
    myStack = stack_linked_list.StackLinkedList()
    myStack.push(0)
    myStack.push(2)
    myStack.push(-3)
    print(myStack.peek())
    print("Size: " + str(myStack.getSize()))
    myStack.pop()
    print(myStack.peek())
    myStack.pop()
    print(myStack.peek())
    print(myStack.pop())

    print(myStack.getSize())

def main():
    #testLinked_list()
    #testDoublyLinkedList()
    testStackLinkedList()

main()