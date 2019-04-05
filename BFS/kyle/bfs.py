import networkx as nx
import queue


def create_graph(nodes = 100, edges = 200):
    g = nx.gnm_random_graph(nodes, edges)
    return g

def bfs():
    g = create_graph(nodes = 15, edges = 25)
    q = queue.Queue()
    #g.add_node(-1)  I want to do some kind of find a node thing or something idk 
    #g.add_edge(14, -1)
    q.put(list(g.nodes()).pop(0))
    print(q.empty())
    while not q.empty(): # for some reason queue.full() doesn't return true even if something is in there. Very confusing. 
        print(q.get())

if __name__ == "__main__":
    bfs()
    print("done !")