from unittest.mock import patch, call
from src.linked_lists import doubly_linked_list
import unittest


class DoublyLinkedListTest(unittest.TestCase):
    def setUp(self):
        self.index: int = 0
        self.doublyLinkedList = doubly_linked_list.DoublyLinkedList()

    def test_create_empty_list(self):
        self.assertEqual(self.doublyLinkedList.getSize(), self.index)

    @patch('builtins.print')
    def test_add_elements(self, mocked_print):
        self.doublyLinkedList.add(100)
        self.index += 1
        self.doublyLinkedList.add(200)
        self.index += 1
        self.doublyLinkedList.add(300)
        self.index += 1
        self.assertEqual(self.doublyLinkedList.getSize(), self.index)
        self.doublyLinkedList.display()
        mocked_print.assert_called_with('300')


