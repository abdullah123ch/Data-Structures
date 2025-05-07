import unittest
import ArrayList

class TestArrayList(unittest.TestCase):
    def setUp(self):
        self.list = ArrayList.AList()
        self.list.addLast(1)
        self.list.addLast(2)
        self.list.addLast(3)
        self.list.addLast(4)    
        self.list.addLast(5)
        self.list.addLast(6)
        self.list.addLast(7)
        self.list.addLast(8)
        self.list.addLast(9)
        self.list.addLast(10)
        self.list.getLast()
        self.list.removeLast()
        self.list.getLast()

    def test_printList(self):
        self.list.printList()

if __name__ == "__main__":
    unittest.main()
