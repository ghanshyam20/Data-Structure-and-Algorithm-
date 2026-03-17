def dijkstra_shortest_path(source_vertex, destination_vertex, graph):
    vertices = graph.get_vertices()

    dist = {}
    prev = {}

    # start values
    for v in vertices:
        dist[v] = float('inf')
        prev[v] = None

    dist[source_vertex] = 0

    visited = []

    while len(visited) < len(vertices):
        current = None
        min_val = float('inf')

        # find smallest distance node
        for v in vertices:
            if v not in visited and dist[v] < min_val:
                min_val = dist[v]
                current = v

        if current is None:
            break

        visited.append(current)

        neighbors = graph.get_adjacent_vertices(current)

        for n in neighbors:
            edge = graph.get_edge(current, n)

            # try to get weight (this version works in most course graphs)
            weight = edge._value

            new_dist = dist[current] + weight

            if new_dist < dist[n]:
                dist[n] = new_dist
                prev[n] = current

    # build path
    path = []
    node = destination_vertex

    while node is not None:
        path.insert(0, node)
        node = prev[node]

    return (dist[destination_vertex], path)