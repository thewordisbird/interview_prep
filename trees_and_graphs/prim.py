def general_mst(G):
    A = {}  # Nodes in spanning tree
    
    
    # Evaluate all edges across cut:
    
    while len(G) - len(A) > 0:
        
        for u in G:
            if len(A) == 0:
                A[u] = None
            q = float('inf')
            c = None
            for v, w in u.items():
                if w < q:
                    q = w,
                    c = v
            A[v] = u


