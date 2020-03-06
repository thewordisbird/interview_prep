# Implementation of Bellman-Ford Shortest path algorithm

def bellman_ford(g, s):
    # Initialize datastructures
    d = {k: float('inf') for k in g}
    d[s] = 0
    # Iterate thrugh graph maximum of v-1 times
    for i in range(len(g) - 1):
        for k,v in d.items():
            if v != float('inf'):
                # Relax edges from v
                
    # Attemp to relax edges one more time. if any can be reduced, there is a negative cycle

