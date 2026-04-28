from structures.min_heap import MinHeap

def dijkstra(graph, start, target):
    distances = {}
    previous = {}
    visited = set()

    for vertex in graph.adjacency_list:
        distances[vertex] = float("inf")
        previous[vertex] = None

    distances[start] = 0

    heap = MinHeap()
    heap.push((0, start))

    while not heap.is_empty():
        current_distance, current_vertex = heap.pop()

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        if current_vertex == target:
            break

        for edge in graph.get_neighbors(current_vertex):
            neighbor = edge["to"]
            weight = edge["weight"]
            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_vertex
                heap.push((new_distance, neighbor))

    path = []
    current = target

    while current is not None:
        path.insert(0, current)
        current = previous[current]

    if len(path) == 0 or path[0] != start:
        return [], float("inf")

    return path, distances[target]