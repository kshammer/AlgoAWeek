class Node:

    def __init__(self, key, neighbors=None):
        #print(f'Creating Node key=[{key}] neighbors=[{neighbors}]')
        self.key = key
        if neighbors is None:
            self.neighbors = set() 
        else:
            self.neighbors = set(neighbors)
        self.visited = False

    def set_visited(self, visited):
        self.visited = visisted

    def is_visited(self):
        return self.visited

    def get_key(self):
        return self.key

    def set_key(self,key):
         self.key = key

    def get_neighbor_ids(self):
        return self.neighbors

    def set_neighbors(self, neighbors):
        self.neighbors = set(neighbors)

