import unittest
from src.queues import queue_array

class QueueArrayTest(unittest.TestCase):
    def setUp(self):
        self.queue = queue_array.QueueArray()


if __name__ == '__main__':
    unittest.main()
