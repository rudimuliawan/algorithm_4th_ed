from unittest import TestCase

from data_structures import Stack


class TestStack(TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_stack_operation(self):
        self.assertTrue(self.stack.is_empty())

        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 1)

        self.stack.push(2)
        self.assertFalse(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 2)

        self.stack.push(3)
        self.assertFalse(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 3)

        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.size(), 2)

        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.size(), 1)

        self.assertEqual(self.stack.pop(), 1)
        self.assertEqual(self.stack.size(), 0)

        with self.assertRaises(Exception):
            self.stack.pop()
