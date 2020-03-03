# Implementation of dijkstra algorithm for shortest path in a DAG or any non-negative cycle graph

# Optimal time complexity is O(vlgv + E) using fibonacci heaps, but this example will be evaluated using
# an array for the priority que, and again using a binary min-heap to compare the complexities
from collections import deque

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, value):
        if value not in self.adjacency_list:
            self.adjacency_list[value] = {}

    def add_edge(self, source, destination, weight):
        if source not in self.adjacency_list:
            self.add_node(source)
            
        self.adjacency_list[source][destination] = weight
        
def dijkstra_array(g, s):
    # Initialize the data structures
    processed = {}
    not_processed = {n: float('inf') for n in g.adjacency_list}

    while not_processed:
        # Extract minimum value from not_processed
        node = extract_min(not_processed)
        # need to add value and distance to processed
        processed(node) 

        # Relax edges from node and evaluate path distance
        for n,w in g.adjacency_list[node].items():
            d = distance to source + w
            if d < not_processed[n]:
                not_processed[n] = d




if __name__ == "__main__":
    g = Graph()
    g.add_node('A')
    g.add_node('B')
    g.add_node('C')
    g.add_node('D')
    g.add_node('E')

    g.add_edge('A', 'B', 10)
    g.add_edge('A', 'C', 3)
    
    g.add_edge('B', 'C', 1)
    g.add_edge('B', 'D', 2)
    
    g.add_edge('C', 'B', 4)
    g.add_edge('C', 'D', 8)
    g.add_edge('C', 'E', 2)
    
    g.add_edge('D', 'E', 7)
    
    g.add_edge('E', 'D', 9)

    print(g.adjacency_list)
