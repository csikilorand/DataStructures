from unittest.mock import patch, call
from src.linked_lists import doubly_linked_list
import unittest


class DoublyLinkedListTest(unittest.TestCase):
    def setUp(self):
        self.index: int = 0
        self.myList = doubly_linked_list.DoublyLinkedList()

    def test_create_empty_list(self):
        self.assertEqual(self.myList.getSize(), self.index)

    @patch('builtins.print')
    def test_add_elements(self, mocked_print):
        self.myList.add(100)
        self.index += 1
        self.myList.add(200)
        self.index += 1
        self.myList.add(300)
        self.index += 1
        self.assertEqual(self.myList.getSize(), self.index)
        self.myList.display()
        mocked_print.assert_called_with('300')


