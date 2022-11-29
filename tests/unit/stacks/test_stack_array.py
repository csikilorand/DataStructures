import unittest
from src.stacks import stack_array


class StackArrayTest(unittest.TestCase):
    def setUp(self):
        self.index = 0
        self.stackArray = stack_array.StackArray()

    def test_is_the_stack_created(self):
        self.assertEqual(self.stackArray.getSize(), self.index)

    def test_add_elements(self):
        self.stackArray.push(1)
        self.index += 1
        self.assertEqual(self.stackArray.getSize(), self.index)
        self.assertEqual(self.stackArray.peek(), 1)
        self.stackArray.push(3)
        self.index += 1
        self.assertEqual(self.stackArray.getSize(), self.index)
        self.assertEqual(self.stackArray.peek(), 3)

    def test_remove_elements(self):
        self.stackArray.push(1)
        self.index += 1
        self.stackArray.push(3)
        self.index += 1
        self.stackArray.push(5)
        self.index += 1
        self.assertEqual(self.stackArray.getSize(), self.index)
        self.assertEqual(self.stackArray.peek(), 5)
        self.stackArray.pop()
        self.index -= 1
        self.assertEqual(self.stackArray.peek(), 3)
        self.assertEqual(self.stackArray.getSize(), self.index)
        self.stackArray.pop()
        self.index -= 1
        self.assertEqual(self.stackArray.peek(), 1)
        self.assertEqual(self.stackArray.getSize(), self.index)