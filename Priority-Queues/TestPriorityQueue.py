import unittest
import PriorityQueue

class TestPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.pq = PriorityQueue.PQ()
        for k in [6,3,1,2,-5,4]:
            self.pq.insert(k)

    def test_insert(self):
        print("intial Priority queue",self.pq.L)
        print("intial size",self.pq.size)
        print("intial root",self.pq.peek())
        print(self.pq.poll())
        print("After poll",self.pq.L)
        print("After poll size",self.pq.size)
        print("After poll root",self.pq.peek())
        

if __name__ == '__main__':
    unittest.main()
   


