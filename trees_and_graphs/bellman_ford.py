# Implementation of Bellman-Ford Shortest path algorithm

def bellman_ford(g, s):
    # Initialize datastructures
    d = {k: float('inf') for k in g}
    p = {k: None for k in g}
    d[s] = 0
    # Iterate thrugh graph maximum of v-1 times
    for i in range(len(g) - 1):
        for v, wv in d.items():
            if wv != float('inf'):
                # Relax edges from v
                for n,wn in g[v].items():
                    if (d[v] + wn) < d[n]:
                        d[n] = d[v] + wn
                        p[n] = v
                    
    #return d, p 
    
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
            'A': {'B': -1, 'C': 4},
            'B': {'C': 3, 'D': -2, 'E': 2},
            'C': {},
            'D': {'B': 1, 'C':5 },
            'E': {'D': -3} 
        }

    print(bellman_ford(g, 'A'))