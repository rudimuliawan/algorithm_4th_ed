from unittest import TestCase

from data_structures import Queue


class TestQueue(TestCase):

    def setUp(self):
        self.queue = Queue()

    def test_queue_operation(self):
        self.assertTrue(self.queue.is_empty())

        self.queue.enqueue(1)
        self.assertFalse(self.queue.is_empty())
        self.assertEqual(self.queue.size(), 1)

        self.queue.enqueue(2)
        self.assertFalse(self.queue.is_empty())
        self.assertEqual(self.queue.size(), 2)

        self.queue.enqueue(3)
        self.assertFalse(self.queue.is_empty())
        self.assertEqual(self.queue.size(), 3)

        self.assertEqual(self.queue.dequeue(), 1)
        self.assertFalse(self.queue.is_empty())
        self.assertEqual(self.queue.size(), 2)

        self.assertEqual(self.queue.dequeue(), 2)
        self.assertFalse(self.queue.is_empty())
        self.assertEqual(self.queue.size(), 1)

        self.assertEqual(self.queue.dequeue(), 3)
        self.assertTrue(self.queue.is_empty())
        self.assertEqual(self.queue.size(), 0)

        with self.assertRaises(Exception):
            self.queue.dequeue()
