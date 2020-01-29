
def shortest_path(graph, source):
    distance = {}
    path = {}
    _shortest_path(graph, source, distance, path)
    return distance[source], get_path(path, source)
   
def get_path(path, node):
    p = []
    while path[node] != None:
        p.append(node)
        node = path[node]
    p.append(node)
    return p

def _shortest_path(graph, vertex, distance={}, path={}):
    print(f'_shortest_path(graph, {vertex}, {distance}, {path})')
    if len(graph[vertex]) == 0:
        distance[vertex] = 0
        path[vertex] = None
        return distance[vertex]
    
    if vertex in distance:
        return distance[vertex]

    distance[vertex] = float('inf')
    path[vertex] = None
    for neighbor, weight in graph[vertex].items():
        new_distance = _shortest_path(graph, neighbor, distance, path) + weight
        if new_distance < distance[vertex]:
            print(f'updating distance for {vertex} from {distance[vertex]} to {new_distance}')
            distance[vertex] = new_distance
            path[vertex] = neighbor
    return distance[vertex]



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

    print(shortest_path(graph, 'S'))