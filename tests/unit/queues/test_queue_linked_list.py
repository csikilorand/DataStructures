import unittest
from src.queues import queue_linked_list

class QueueLinkedListTest(unittest.TestCase):
    def setUp(self):
        self.capacity = 0
        self.queueLinkedList = queue_linked_list.MyQueueLinkedList()

    def test_is_the_queue_created(self):
        tempQueue = queue_linked_list.MyQueueLinkedList()
        self.assertTrue(self.queueLinkedList is not None)
        self.assertEqual(type(tempQueue), type(self.queueLinkedList))

    def test_isEmpty(self):
        self.assertTrue(self.queueLinkedList.isEmpty())


if __name__ == '__main__':
    unittest.main()
