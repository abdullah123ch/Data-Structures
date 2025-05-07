import unittest
import BFS

class TestBFS(unittest.TestCase):
    def setUp(self):
        # Example adjacency list for testing
        self.Adj = {
            0: [1, 2],
            1: [0, 3, 4],
            2: [0],
            3: [1],
            4: [1]
        }

    def test_bfs(self):
        bfs = BFS.BFS()
        parent = bfs.bfs(self.Adj, 0)
        expected_parent = [0,0,0,1,1]
        self.assertEqual(parent, expected_parent)

    def test_unweighted_shortest_path(self):
        bfs = BFS.BFS()
        path = bfs.unweighted_shortest_path(self.Adj, 0, 4)
        expected_path = [0, 1, 4]
        self.assertEqual(path, expected_path)

if __name__ == '__main__':
    unittest.main()