import unittest
import Graphs

class TestGraphs(unittest.TestCase):
    def setUp(self):
        self.graph = Graphs.Graph(11)
        self.data = {
        0: "action",
        1: "change",
        2: "demotion",
        3: "descent",
        4: "jump parachuting",
        5: "increase",
        6: "jump leap",
        7: "augmentation",
        8: "antihistamine",
        9: "nasal_decongestant",
        10: "actifed"
        }
        self.graph.add_edge(0, 1)
        self.graph.add_edge(1, 2)
        self.graph.add_edge(3, 4)
        self.graph.add_edge(5, 6)
        self.graph.add_edge(5, 7)
        self.graph.add_edge(8, 10)
        self.graph.add_edge(9, 10)
        self.graph.display()

    def test_vertices(self):
        self.assertEqual(self.graph.vertices(), 11)

    def test_edges(self):
        self.assertEqual(self.graph.edges(), 7)

    def test_degree(self):
        self.assertEqual(self.graph.degree(0), 1)
        self.assertEqual(self.graph.degree(1), 2)
        self.assertEqual(self.graph.degree(3), 1)
        self.assertEqual(self.graph.degree(5), 2)
        self.assertEqual(self.graph.degree(8), 1)

if __name__ == '__main__':
    unittest.main()