from collections import deque

def bfs(G, s):
    S = {}
    d = {}
    Q = deque()

    S[s] = None
    d[s] = 0
    Q.append(s)

    while len(Q) > 0:
        u = Q.popleft()
        for v in G[u]:
            if v not in S:
                S[v] = u
                d[v] = d[u] + 1
                Q.append(v)
    return S, d


if __name__ == "__main__":
    G = {
        'r': {'s', 'v'},
        's': {'r', 'w'},
        't': {'u', 'w', 'x'},
        'u': {'t', 'x', 'y'},
        'v': {'r'},
        'w': {'s', 't', 'x'},
        'x': {'t', 'u', 'y'},
        'y': {'x', 'u'}
    }

    print(bfs(G, 'r'))
        
