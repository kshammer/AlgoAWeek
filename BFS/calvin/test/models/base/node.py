from bfs.models.base.node import Node
import unittest

class NodeTest(unittest.TestCase):

    def test_init(self):
        node1 = Node("A")
        self.assertEqual(node1.get_key(), "A")
        self.assertFalse(node1.is_visited(), False)
        self.assertTrue(len(node1.get_neighbor_ids())==0)

    def test_initWithNeighbors(self):
        key = "A"
        neighbors = {"A", "B", "C"}
        node = Node(key, neighbors)
        self.assertEqual(len(node.get_neighbor_ids()),3)
        self.assertEqual(node.get_neighbor_ids(), neighbors)
