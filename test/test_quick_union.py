from unittest import TestCase

from data_structures.union_find import QuickUnion


class TestUnionFind(TestCase):

    def setUp(self):
        self.quick_union = QuickUnion(size=10)

    def test_union(self):
        self.quick_union.union(1, 5)
        self.assertTrue(self.quick_union.is_connected(1, 5))
        self.assertFalse(self.quick_union.is_connected(1, 6))

        self.quick_union.union(1, 6)
        self.assertTrue(self.quick_union.is_connected(5, 6))

        self.quick_union.union(9, 6)
        self.assertTrue(self.quick_union.is_connected(9, 1))
