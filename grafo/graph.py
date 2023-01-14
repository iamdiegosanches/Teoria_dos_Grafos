class Graph:
    def __init__(self, count_nodes: int = 0, count_edges: int = 0, adj_list: list[list[int]] = []) -> None:
        self.count_nodes = count_nodes
        self.count_edges = count_edges
        self.adj_list = adj_list

        if not adj_list:
            for _ in range(self.count_nodes):
                adj_list.append([])

    def validate_node(self, u: int):
        if u < 0 or u >= self.count_nodes:
            return True

    def validate_edge(self, v: int):
        if v < 0 or v >= self.count_nodes:
            return True

    def add_directed_edge(self, u: int, v: int):
        if self.validate_node(u) or self.validate_edge(v):
            print(f'Edge ({u}, {v}) could not be added because one of the values is out of the allowed range')
        else:
            self.adj_list[u].append(v)
            self.count_edges += 1

    def add_undirected_edge(self, u: int, v: int):
        self.add_directed_edge(u, v)
        self.add_directed_edge(v, u)

    def add_node(self):
        self.adj_list.append([])
        self.count_nodes += 1

    def degree_out(self, u: int) -> int:
        if u < 0 or u >= self.count_nodes:
            return -1
        else:
            return len(self.adj_list[u])

    def degree_in(self, u: int) -> int:
        aux = 0
        for n in range(len(self.adj_list)):
            if u in self.adj_list[n]:
                aux += 1
        return aux
    
   def highest_degree_out(self) -> int:
        max_degree_out = 0
        highest_degree_node = 0
        for i in range(self.count_nodes):
            if self.degree_out(i) > max_degree_out:
                max_degree_out = self.degree_out(i)
                highest_degree_node = i
        return highest_degree_node

   def highest_degree_in(self) -> int:
        max_degree_in = 0
        highest_degree_node = 0
        for i in range(self.count_nodes):
            degree_in_node_i = self.degree_in(i)
            if degree_in_node_i > max_degree_in:
                max_degree_in = degree_in_node_i
                highest_degree_node = i
        return highest_degree_node
    
   def is_complete(self):
        for i in self.adj_list:
            if len(i) != len(self.adj_list)-1:
                return False
        return True
