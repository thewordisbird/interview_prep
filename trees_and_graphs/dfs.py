class DFSResult:
    """Object to hold DFS results from processing"""
    def __init__(self):
        self.parent = {}
        self.start_time = {}
        self.finish_time = {}
        self.edges = {}
        self.order = []
        self.time = 0

def dfs(G):
    """Set up DFS. Find source node for tree in forest and recurse."""
    # Initialize DFSResult Object
    result = DFSResult()

    for u in G:
        if u not in result.parent:
            dfs_visit(G, u, result)
    return result


def dfs_visit(G, u, result, parent=None):
    # Initialize current node
    result.parent[u] = parent
    result.time += 1
    # Set the start time for node evaluation
    result.start_time[u] = result.time

    # Classify Edges
    if parent:
        result.edges[parent, u] = 'Tree'
    for n in G[u]:
        if n not in result.start_time:
            # The node has not been evaluated. Recurse and continue DFS
            dfs_visit(G, n, result, u)
        elif n not in result.finish_time:
            # The node is already in progress, this makes edge (u,n) a backedge or a cycle in the graph
            result.edges[(u, n)] = 'Back'
        elif result.start_time[u] < result.start_time[n]:
            # This is a forward edge, it would allow skipping a generation
            result.edges[(u, n)] = 'Forward'
        else:
            # The edge (u,n) is a cross edge
            result.edges[(u, n)] = 'Cross'
    
    # Finishe evaluation on node once no more recursion is possible.
    result.time += 1
    result.finish_time[u] = result.time
    result.order.append(u)


def topological_sort(G):
    # Perform DFS on the graph
    dfs_result = dfs(G)
    # Reverse the result order
    dfs_result.order.reverse()
    return dfs_result.order
