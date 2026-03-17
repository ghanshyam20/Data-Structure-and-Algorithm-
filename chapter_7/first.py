def DFS(graph, u, visited=None):
    # if first time, create visited dict
    if visited is None:
        visited = {}
        visited[u] = None   # start node has no parent

    # go through neighbors of u
    neighbors = graph._adj_map[u]

    for v in neighbors:
        # if not visited then go deeper
        if v not in visited:
            visited[v] = u
            DFS(graph, v, visited)

    return visited


