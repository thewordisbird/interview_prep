def transitive_closure(graph):
    result = []
    for i in range(len(graph)):
        result_row = [0 for _ in range(len(graph))]
        for j in range(len(graph)):
            if check_path(graph, i, j):
                result_row[j] = 1
        print(result_row)


def check_path(graph, node, target, visited = set()):
    if target in graph[node]:
        return True
    
    for neighbor in graph[node]:
        if node not in visited:
            visited.add(node)
        return check_path(graph, neighbor, target, visited)
    
    return False

if __name__ == "__main__":
    graph = [[0,1,3], [1,2], [2], [3]]

    print(transitive_closure(graph))