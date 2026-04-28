class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.adjacency_list:
            self.adjacency_list[vertex_id] = []

    def add_edge(self, source, target, weight, properties=None):
        if properties is None:
            properties = {}

        self.add_vertex(source)
        self.add_vertex(target)

        # Multigraph destegi:
        # Ayni iki durak arasinda farkli hatlar bulunabilir.
        self.adjacency_list[source].append({
            "to": target,
            "weight": weight,
            "properties": properties
        })

        self.adjacency_list[target].append({
            "to": source,
            "weight": weight,
            "properties": properties
        })

    def get_neighbors(self, vertex_id):
        return self.adjacency_list.get(vertex_id, [])