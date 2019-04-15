import unittest
from bfs.models.base.graph import Graph
from bfs.models.base.node import Node

class GraphTest(unittest.TestCase):

    def test_putNode(self):
        graph = Graph()
        key = "A"
        neighbors = {"C","D","E"}
        node = Node(key,neighbors)
        graph.put(key,node)
        self.assertIsNotNone(graph.get_node("A"))
        self.assertEqual(len(graph.get_node("A").get_neighbor_ids()),3)
