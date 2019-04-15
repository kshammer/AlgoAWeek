import unittest
from bfs.algorithms.breadth_first_search import BFS 
from bfs.models.base.graph import Graph
from bfs.models.base.node import Node
from bfs.models.factory.graph import GraphFactory
from bfs.utils.graph import GraphUtils


class BFSTest(unittest.TestCase):

    def test_bfs1(self):
        test_file_name = 'test_graph.txt'
        print(f'Opening file={test_file_name}')
        
        graph = None
        graph_data = None
        with open(test_file_name) as f:
            graph_data = f.read()
            graph = GraphUtils.parse_graph_config(graph_data)

        #assertions
        BFS.search(graph,'A','C')
        #self.assertEqual(graph.get_node('A').get_key(), 'A')
        #self.assertEqual(graph.get_node('A').is_visited(), False)
        self.fail("Not completed")
