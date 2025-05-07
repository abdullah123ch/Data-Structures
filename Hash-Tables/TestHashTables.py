import unittest
import HashTables

class TestHashTables(unittest.TestCase):
    def setUp(self):
        self.HT = HashTables.HashTable(10)
        self.HT.insert(20, 'red')
        self.HT.insert(13, 'red')
        self.HT.insert(16,'red')
        self.HT.insert(11, 'red')
        self.HT.insert(3, 'red')
        self.HT.insert(7, 'red')

    def test_display(self):
        self.HT.display()

    def test_contains(self):
        self.assertTrue(self.HT.contains(20, 'red'))
        self.assertTrue(self.HT.contains(13, 'red'))
        self.assertTrue(self.HT.contains(16, 'red'))
        self.assertTrue(self.HT.contains(11, 'red'))
        self.assertFalse(self.HT.contains(53, 'pink'))
        self.assertFalse(self.HT.contains(7, 'green'))
        self.assertFalse(self.HT.contains(100, 'blue'))

if __name__ == '__main__':
    unittest.main()