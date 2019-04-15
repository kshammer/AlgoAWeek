import unittest
from bfs.models.base.graph import Graph
from bfs.models.base.node import Node
from bfs.models.factory.graph import GraphFactory

class GraphFactoryTest(unittest.TestCase):

    def test_oneItemGraph(self):
        data = {}
        key = "A"
        neighbors = {"C","D","E"}
        data[key]=neighbors
        graph = GraphFactory.create_graph(data)
        self.assertIsNotNone(graph.get_node("A"))
        self.assertEqual(len(graph.get_node("A").get_neighbor_ids()),3)
