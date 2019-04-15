import queue

class BFS:

    @classmethod
    def search(cls, graph, start_key, to_find):
        search_queue = queue.Queue()
        start_node = graph.get_node(start_key)

        # Initial check on start node
        if (start_node.get_key() == to_find):
            print(f'Found key')
            return
        #search_queue.put(list(start_node.get_neighbors()))
        list(map(search_queue.put,start_node.get_neighbor_ids()))
        visited = set()

        while not search_queue.empty():
            currId = search_queue.get()
            # idk, workaround for when putting neighbors in search queue twice, skip overhead of checking....
            if currId in visited:
                continue
            print(f'Checking {currId}')
            visited.add(currId)
            if(currId == to_find):
                print('Found key')
                return True;
            for neighbor in graph.get_node(currId).get_neighbor_ids():
                if neighbor not in visited :
                    search_queue.put(neighbor)
        print('Could not find key')
        return False
