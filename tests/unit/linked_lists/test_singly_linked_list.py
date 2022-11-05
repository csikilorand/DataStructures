import unittest
from unittest.mock import patch
from src.linked_lists import singly_linked_list


class SinglyLinkedListTest(unittest.TestCase):

    def setUp(self):
        # super(SinglyLinkedListTest, self).setUp()
        self.index: int = 0
        self.singlyLinkedList = singly_linked_list.SinglyLinkedList()

    def test_create_list(self):
        self.assertEqual(self.singlyLinkedList.getSize(), self.index)

    def test_removing_from_empty_list(self):
        self.assertRaises(ValueError, self.singlyLinkedList.removeTail)
        self.singlyLinkedList.addHead(-50)
        self.index += 1
        self.assertEqual(self.singlyLinkedList.getSize(), self.index)
        # indexing starts from 0
        self.assertEqual(self.singlyLinkedList.getIndexByElement(-50), 0)
        self.singlyLinkedList.addTail(-100)
        self.index += 1
        self.assertEqual(self.singlyLinkedList.getSize(), self.index)

    def test_add_elements_to_list(self):
        self.singlyLinkedList.addTail(90)
        self.index += 1
        self.assertEqual(self.singlyLinkedList.getSize(), self.index)
        self.singlyLinkedList.addHead(100)
        self.index += 1
        self.assertEqual(self.singlyLinkedList.getSize(), self.index)
        self.assertEqual(self.singlyLinkedList.isEmpty(), False)
        self.assertFalse(self.singlyLinkedList.isEmpty())
        self.assertTrue(self.index == self.singlyLinkedList.getSize())

    def test_simple_add(self):
        self.assertEqual(self.singlyLinkedList.getSize(), self.index)
        print(self.index)
        self.singlyLinkedList.add(9)
        self.index += 1
        self.assertEqual(self.singlyLinkedList.getSize(), self.index)
        print(self.singlyLinkedList.display())

    def test_remove_elements(self):
        self.singlyLinkedList.add(90)
        self.index += 1
        self.singlyLinkedList.add(200)
        self.index += 1
        self.singlyLinkedList.add(300)
        self.index += 1
        self.singlyLinkedList.addAfterElement(200, 400)
        self.index += 1
        self.assertEqual(self.singlyLinkedList.getSize(), self.index)
        self.singlyLinkedList.removeTail()
        self.index -= 1
        self.assertEqual(self.singlyLinkedList.getSize(), self.index)
        with patch('builtins.print') as mocked_print:
            self.singlyLinkedList.display()
            mocked_print.assert_called_with('400 ')




