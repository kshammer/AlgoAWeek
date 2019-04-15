from bfs.models.base.node import Node

class Graph:

    def __init__(self):
        self.nodes = {}

    def put(self, key, node):
        self.nodes[key] = node

    def get_node(self, key):
        return self.nodes[key]
