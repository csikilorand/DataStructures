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
        self.assertEqual(self.queueLinkedList.getSize(), self.capacity)

    def test_enqueue(self):
        for i in range(13):
            self.queueLinkedList.enqueue(i)
        tempValue = 0
        self.assertEqual(tempValue, self.queueLinkedList.dequeue())
        tempValue = 12
        self.assertEqual(tempValue, self.queueLinkedList.getSize())
        self.assertEqual(tempValue, self.queueLinkedList.getTopElement())

    def test_dequeue(self):
        with self.assertRaises(ValueError):
           self.queueLinkedList.dequeue()
        tempArray = [i for i in range(4, -1, -1)]
        for i in range(5):
            self.queueLinkedList.enqueue(i)
            self.assertEqual(tempArray[ (len(tempArray)-1) -i], self.queueLinkedList.getTopElement())

if __name__ == '__main__':
    unittest.main()
