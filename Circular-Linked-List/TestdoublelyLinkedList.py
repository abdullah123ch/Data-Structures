import unittest
import doublelyLinkedList

class TestDoublelyLinkedList(unittest.TestCase):
    def setUp(self):
        self.dll = doublelyLinkedList.DLList()
        self.dll.addFirst(4)
        self.dll.addFirst(3)
        self.dll.addFirst(2)
        self.dll.addFirst(1)
        self.dll.addLast(5)
        self.dll.addLast(6)
        self.dll.addLast(7)
        self.dll.addLast(8)
        self.dll.addLast(9)
        self.dll.addLast(10)
        self.dll.removeFirst()
        self.dll.removeLast()

    def test_ToList(self):
        print(self.dll.ToList())

if __name__ == '__main__':
    unittest.main()