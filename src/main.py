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
    print("Size: " + str(myList.getSize()))
    myList.display()
def main():
    #testLinked_list()
    testDoublyLinkedList()

main()