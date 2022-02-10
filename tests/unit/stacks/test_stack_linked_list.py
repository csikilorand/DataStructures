import unittest
from src.stacks import stack_linked_list


class StackLinkedListTest(unittest.TestCase):
    def test_create_stack(self):
        myStack = stack_linked_list.StackLinkedList()
        self.assertEqual(myStack.getSize(), 0)  # add assertion here

    def test_add_element(self):
        myStack = stack_linked_list.StackLinkedList()
        myStack.push(-1)
        self.assertEqual(myStack.getSize(), 1)
        self.assertEqual(myStack.peek(), -1)

        myStack.push(-2)
        self.assertEqual(myStack.peek(), -2)
        self.assertEqual(myStack.getSize(), 2)

    def test_remove_elements(self):
        listOfExpectedTestElements = [-1, -2, -3, -4]
        myStack = stack_linked_list.StackLinkedList()
        myStack.push(-1)
        myStack.push(-2)
        myStack.push(-3)
        myStack.push(-4)
        self.assertEqual(myStack.getSize(), len(listOfExpectedTestElements))
        myStack.pop()
        self.assertEqual(myStack.peek(), listOfExpectedTestElements[2])
        myStack.pop()
        myStack.pop()
        myStack.pop()
        self.assertEqual(myStack.getSize(), 0)
        self.assertRaises(ValueError, myStack.peek)
        


