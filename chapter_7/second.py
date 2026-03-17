def BFS(graph, start):
    # use queue for BFS
    visited = {}
    queue = []

    visited[start] = None   # start node
    queue.append(start)

    # loop until queue empty
    while len(queue) > 0:
        u = queue.pop(0)   # take first element

        neighbors = graph._adj_map[u]

        # check all neighbors
        for v in neighbors:
            if v not in visited:
                visited[v] = u
                queue.append(v)

    return visited



