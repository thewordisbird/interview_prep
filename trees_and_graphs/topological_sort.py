# Given an graph as an adjacency list determine a topological sort ordering.
def topological_sort(vertex):
    visted = set()
    order = []
    _topological_sort(vertex, visted, order)
    return list(reversed(order))
    
def _topological_sort(vertex, visited, order):
    if vertex not in visited:
        visited.add(vertex)
        for neighbor in graph[vertex]:
            _topological_sort(neighbor, visited, order)
        order.append(vertex)
    return order

if __name__ == "__main__":
    graph = {
                'S': {'A': 1, 'B': 2, 'C': 3},
                'A': {'D': 4, 'E': 2},
                'B': {'D': 2, 'E': 1, 'F': 2},
                'C': {'E': 3, 'F': 2, 'G': 2},
                'D': {'G': 2},
                'E': {'G': 4},
                'F': {'G': 1},
                'G': {}
            }

    print(topological_sort('S'))