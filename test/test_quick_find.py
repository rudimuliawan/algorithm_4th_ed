from unittest import TestCase

from data_structures.union_find import QuickFind


class TestUnionFind(TestCase):

    def setUp(self):
        self.quick_find = QuickFind(size=10)

    def test_union(self):
        self.quick_find.union(1, 5)
        self.assertTrue(self.quick_find.is_connected(1, 5))
        self.assertFalse(self.quick_find.is_connected(1, 6))

        self.quick_find.union(1, 6)
        self.assertTrue(self.quick_find.is_connected(5, 6))

        self.quick_find.union(9, 6)
        self.assertTrue(self.quick_find.is_connected(9, 1))

        expected_ids = [0, 6, 2, 3, 4, 6, 6, 7, 8, 6]
        self.assertEqual(self.quick_find.id, expected_ids)
