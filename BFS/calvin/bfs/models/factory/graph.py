from bfs.models.base.node import Node
from bfs.models.base.graph import Graph

class GraphFactory:

    @staticmethod
    def create_graph(data):
        graph = Graph()
        #print(f'Received data={data}')
        for key, config in data.items():
            node = Node(key, config)
            graph.put(key,node)
        return graph
