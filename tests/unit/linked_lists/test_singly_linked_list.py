import unittest
from unittest.mock import patch
from src.linked_lists import singly_linked_list


class SinglyLinkedListTest(unittest.TestCase):

    def setUp(self):
        # super(SinglyLinkedListTest, self).setUp()
        self.index: int = 0
        self.myList = singly_linked_list.SinglyLinkedList()

    def test_create_list(self):
        self.assertEqual(self.myList.getSize(), self.index)

    def test_removing_from_empty_list(self):
        self.assertRaises(ValueError, self.myList.removeTail)
        self.myList.addHead(-50)
        self.index += 1
        self.assertEqual(self.myList.getSize(), self.index)
        # indexing starts from 0
        self.assertEqual(self.myList.getIndexByElement(-50), 0)
        self.myList.addTail(-100)
        self.index += 1
        self.assertEqual(self.myList.getSize(), self.index)

    def test_add_elements_to_list(self):
        self.myList.addTail(90)
        self.index += 1
        self.assertEqual(self.myList.getSize(), self.index)
        self.myList.addHead(100)
        self.index += 1
        self.assertEqual(self.myList.getSize(), self.index)
        self.assertEqual(self.myList.isEmpty(), False)
        self.assertFalse(self.myList.isEmpty())
        self.assertTrue(self.index == self.myList.getSize())

    def test_simple_add(self):
        self.assertEqual(self.myList.getSize(), self.index)
        print(self.index)
        self.myList.add(9)
        self.index += 1
        self.assertEqual(self.myList.getSize(), self.index)
        print(self.myList.display())

    def test_remove_elements(self):
        self.myList.add(90)
        self.index += 1
        self.myList.add(200)
        self.index += 1
        self.myList.add(300)
        self.index += 1
        self.myList.addAfterElement(200, 400)
        self.index += 1
        self.assertEqual(self.myList.getSize(), self.index)
        self.myList.removeTail()
        self.index -= 1
        self.assertEqual(self.myList.getSize(), self.index)
        with patch('builtins.print') as mocked_print:
            self.myList.display()
            mocked_print.assert_called_with('400 ')




