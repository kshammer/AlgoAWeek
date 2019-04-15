import sys

from bfs.models.factory.graph import GraphFactory
from bfs.utils.graph import GraphUtils
#from bfs.models.base.graph import Graph
from bfs.algorithms.breadth_first_search import BFS

def main():
    print(f'Staring with args={sys.argv}')
    print('Usage: python runner.py <graph_input.txt> <start_id> <to_find_id>')
    if(len(sys.argv) < 4):
        return
    # Open file handler
    file_name = sys.argv[1]
    print(f'Opening file={file_name}')

    graph_data = None
    with open(file_name) as f:
        graph_data = f.read()
    
    # Parse graph data into a config
    graph = GraphUtils.parse_graph_config(graph_data)


    print('=========================================')
    BFS.search(graph,sys.argv[2],sys.argv[3])
    print('=================END=====================')
    


if __name__ == "__main__":
    main()
