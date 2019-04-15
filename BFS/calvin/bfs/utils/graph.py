from bfs.models.factory.graph import GraphFactory

class GraphUtils:

    @classmethod
    def parse_graph_config(cls, data):
        data_configs = data.splitlines()
        graph_config = {}
        for config in data_configs:
            node_config = config.split("=",1)
            key = node_config[0]
            value = node_config[1].strip("{}").split(",")
            graph_config[key]=value
        graph = GraphFactory.create_graph(graph_config)
        return graph

