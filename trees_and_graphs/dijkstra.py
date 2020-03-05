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

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class MinHeap:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def insert(self, key, value):
        n = Node(key, value)
        self.heap.append(n)
        self.heapify_up()

    def decrease_key(self, key, value):
        for i, n in enumerate(self.heap):
            if n.key == key:
                n.value = value
                self.heapify_up(i)

    def extract_min(self):
        min_node = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down()
        return min_node.key, min_node.value

    def heapify_down(self):
        node_index = 0
        while self.has_children(node_index):
            min_child_index = self.get_min_child_index(node_index)
            if self.heap[node_index].value > self.heap[min_child_index].value:
                # swap child and node
                self.heap[min_child_index], self.heap[node_index] = self.heap[node_index], self.heap[min_child_index]
                node_index = min_child_index
            else:
                break
     
    def heapify_up(self, node_index=None):
        if node_index == None:
            node_index = len(self.heap) - 1
        parent_index = self.get_parent_index(node_index)
        while parent_index > -1 and self.heap[node_index].value < self.heap[parent_index].value:
            # swap parent and node
            self.heap[parent_index], self.heap[node_index] = self.heap[node_index], self.heap[parent_index]
            node_index = parent_index
            parent_index = self.get_parent_index(node_index)


    def get_parent_index(self, node_index):
        return (node_index - 1) // 2

    def get_right_child_index(self, node_index):
        return (2 * node_index) + 2

    def get_left_child_index(self, node_index):
        return (2 * node_index) + 1

    def get_min_child_index(self, node_index):
        if self.has_children(node_index):
            min_child_index = self.get_left_child_index(node_index)
            if min_child_index != len(self.heap) - 1 and self.heap[min_child_index].value > self.heap[self.get_right_child_index(node_index)].value:
                min_child_index = self.get_right_child_index(node_index)

    def has_parent(self, node_index):
        return self.get_parent_index(node_index) >= 0

    def has_children(self, node_index):
        return self.get_left_child_index(node_index) >= len(self.heap)
        
def dijkstra_heap(g, s):
    processed = {}
    not_processed = MinHeap()
    for n in g.adjacency_list:
        not_processed.insert(n, float('inf'))

    not_processed.decrease_key(s, 0)

    while not not_processed.is_empty:
        node, distance = not_processed.extract_min()
        processed[node] = distance

        # Relax edges from node and evaluate path distance
        for n,w in g.adjacency_list[node].items():
            if n not in processed:
                d = distance + w
                if d < not_processed[n]:
                    not_processed[n] = d

    return processed

    




def dijkstra_array(g, s):
    # Initialize the data structures
    processed = {}
    not_processed = {n: float('inf') for n in g.adjacency_list}
    not_processed[s] = 0

    while not_processed:
        # Extract minimum value from not_processed
        node, distance = extract_min(not_processed)
        # need to add value and distance to processed
        processed[node]= distance

        # Relax edges from node and evaluate path distance
        for n,w in g.adjacency_list[node].items():
            if n in not_processed:
                d = distance + w
                if d < not_processed[n]:
                    not_processed[n] = d

    return processed

def extract_min(nodes):
    min_dist = float('inf')
    min_key = None
    for k,v in nodes.items():
        if v < min_dist:
            min_dist = v
            min_key = k
    del nodes[min_key]
    return min_key, min_dist


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

    #print(g.adjacency_list)
    #print(dijkstra_array(g,'A'))
    # Heap implementation not working
    print(dijkstra_heap(g,'A'))
