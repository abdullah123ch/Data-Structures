import unittest
import LinkedList

# Add the function to the TestLinkedList class
class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.list = LinkedList.SLList()
        self.list.addFirst(4)
        self.list.addFirst(3)
        self.list.addFirst(2)
        self.list.addFirst(1)
        self.list.addLast(5)
        self.list.addLast(6)
        self.list.addLast(7)
        self.list.addLast(8)
        self.list.addLast(9)
        self.list.addLast(10)

    def test_printLinkedList(self):
        self.list.printLinkedList()    
        
if __name__ == '__main__':
    unittest.main()