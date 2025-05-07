import unittest
import DeQueue

# Add the function to the TestLinkedList class
class TestDeQueue(unittest.TestCase):
    def setUp(self):
        self.list = DeQueue.AQueue()
        self.list.addFirst(4)
        self.list.addFirst(3)
        self.list.addFirst(2)
        self.list.addFirst(1)
        self.list.addLast(9)
        self.list.addLast(10)

    def test_printDeQueue(self):
        print(self.list.Tolist())    
        
if __name__ == '__main__':
    unittest.main()