# Implementation of Bellman-Ford Shortest path algorithm

def bellman_ford(g, s):
    # Initialize datastructures
    d = {x: float('inf') for x in g}
    p = {y: None for y in g}
    d[s] = 0
    # Iterate thrugh graph maximum of v-1 times
    for i in range(len(g) - 1):
        for u, wu in d.items():            
            for v,wv in g[u].items():
                print(f'i: {i}, u: {u, wu}, v: {v, wv}, ({d[u]} + {wv}) < {d[v]}')
                if  d[v] > (d[u] + wv):
                    d[v] = d[u] + wv
                    p[v] = u
  
    # Attemp to relax edges one more time. if any can be reduced, there is a negative cycle
    for v, wv in d.items():
        if wv != float('inf'):
            # Relax edges from v
            for n,wn in g[v].items():
                if (d[v] + wn) < d[n]:
                    return False, None, None

    return True, d, p




if __name__ == "__main__":
    g = {
            'A': {'B': 1, 'C': 4},
            'B': {'C': 3, 'D': 2, 'E': 2},
            'C': {},
            'D': {'B': 1, 'C':5 },
            'E': {'D': 3} 
        }

    print(bellman_ford(g, 'A'))