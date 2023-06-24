import unittest
from a2 import LinearProbingHash, ChainingHash
# from a2_tombstone import ChainingHash


class TestLinearProbingHash(unittest.TestCase):
    def setUp(self):
        self.table = LinearProbingHash()

    def test_insert(self):
        self.assertTrue(self.table.insert(1, "one"))
        self.assertTrue(self.table.insert(2, "two"))
        self.assertTrue(self.table.insert(3, "three"))
        self.assertFalse(self.table.insert(1, "one"))

    def test_modify(self):
        self.table.insert(1, "one")
        self.assertTrue(self.table.modify(1, "new one"))
        self.assertFalse(self.table.modify(2, "two"))

    def test_remove(self):
        self.table.insert(1, "one")
        self.assertTrue(self.table.remove(1))
        self.assertFalse(self.table.remove(2))

    def test_search(self):
        self.table.insert(1, "one")
        self.assertEqual(self.table.search(1), "one")
        self.assertIsNone(self.table.search(2))

    def test_grow(self):
        for i in range(10):
            self.table.insert(i, str(i))
        self.assertEqual(self.table.length, 10)
        self.table.grow()
        self.assertEqual(self.table.length, 11)


class TestChainingHash(unittest.TestCase):
    def setUp(self):
        self.table = ChainingHash()

    def test_insert(self):
        self.assertTrue(self.table.insert(1, "one"))
        self.assertTrue(self.table.insert(2, "two"))
        self.assertTrue(self.table.insert(3, "three"))
        self.assertFalse(self.table.insert(1, "one"))

    def test_modify(self):
        self.table.insert(1, "one")
        self.assertTrue(self.table.modify(1, "new one"))
        self.assertFalse(self.table.modify(2, "two"))

    def test_remove(self):
        self.table.insert(1, "one")
        self.assertTrue(self.table.remove(1))
        self.assertFalse(self.table.remove(2))

    def test_search(self):
        self.table.insert(1, "one")
        self.assertEqual(self.table.search(1), "one")
        self.assertIsNone(self.table.search(2))

    def test_grow(self):
        for i in range(10):
            self.table.insert(i, str(i))
        self.assertEqual(self.table.length, 10)
        self.table.grow()
        self.assertEqual(self.table.length, 11)




if __name__ == '__main__':
    unittest.main()
