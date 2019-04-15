import unittest
from bfs.models.base.graph import Graph
from bfs.models.base.node import Node
from bfs.models.factory.graph import GraphFactory
from bfs.utils.graph import GraphUtils

class GraphUtilsTest(unittest.TestCase):

    def test_graphCreationViaData(self):
        test_file_name = 'test_graph.txt'
        print(f'Opening file={test_file_name}')

        graph_data = None
        with open(test_file_name) as f:
            graph_data = f.read()
            graph = GraphUtils.parse_graph_config(graph_data)

        #assertions
        self.assertEqual(graph.get_node('A').get_key(), 'A')
        self.assertEqual(graph.get_node('A').is_visited(), False)
        expected_neighbors = {'B','C','D'}
        self.assertEqual(graph.get_node('A').get_neighbor_ids(), expected_neighbors)
