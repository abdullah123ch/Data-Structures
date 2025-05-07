import unittest
import DFS

class TestDFS(unittest.TestCase):
    def setUp(self):
        # Example adjacency list for testing
        self.Adj = {
            0: [1, 2],
            1: [0, 3, 4],
            2: [0],
            3: [1],
            4: [1]
        }
    
    def test_dfs(self):
        dfs_instance = DFS.DFS()
        parent, order = dfs_instance.dfs(self.Adj, 0)
    
        # Check if the parent array is correct
        expected_parent = [0, 0, 0, 1, 1]
        self.assertEqual(parent, expected_parent)
        
        # Check if the order of nodes visited is correct
        expected_order = [3, 4, 1, 2, 0]
        self.assertEqual(order, expected_order)

if __name__ == '__main__':
    unittest.main()
   