import unittest
import BinarySearchtress

class TestBinarySearchtress(unittest.TestCase):
    def setUp(self):
        self.t = BinarySearchtress.BSTmap()
        self.t.insert(4,'uet')
        self.t.insert(2,'uet')
        self.t.insert(7,'uet')
        self.t.insert(3,'uet')
        self.t.insert(4,'uet')
        self.t.insert(8,'uet')

    def test_display(self):
        BinarySearchtress.display(self.t.root)

    def test_find(self):
        self.assertTrue(self.t.find(4))
        self.assertTrue(self.t.find(2))
        self.assertTrue(self.t.find(7))
        self.assertTrue(self.t.find(3))
        self.assertFalse(self.t.find(5))
        self.assertFalse(self.t.find(9))

if __name__ == '__main__':
    unittest.main()
