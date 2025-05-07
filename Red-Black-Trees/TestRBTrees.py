import unittest
import RBTrees

class TestRBTrees(unittest.TestCase):
    def setUp(self):
        self.tree = RBTrees.BSTmap()
        for t in  [5,11,3,9,7,1,2]:
            self.tree.insert(t)

    def test_display(self):
        RBTrees.display(self.tree.root)

if __name__ == '__main__':
    unittest.main()
  