class Graph:
    def __init__(self, count_nodes: int = 0, count_edges: int = 0, adj_list=None) -> None:
        if adj_list is None:
            adj_list = []
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

    def lowest_degree_out(self) -> int:
        min_degree_out = self.degree_out(0)
        lowest_degree_node = 0
        for i in range(self.count_nodes):
            if self.degree_out(i) < min_degree_out:
                min_degree_out = self.degree_out(i)
                lowest_degree_node = i
        return lowest_degree_node

    def lowest_degree_in(self) -> int:
        min_degree_in = self.degree_in(0)
        lowest_degree_node = 0
        for i in range(self.count_nodes):
            if self.degree_in(i) < min_degree_in:
                min_degree_in = self.degree_in(i)
                lowest_degree_node = i
        return lowest_degree_node

    def is_complete(self):
        # return self.count_nodes * (self.count_nodes - 1) == self.count_edges (my implementation)
        return self.density() == 1

    def is_regular(self):
        for i in range(1, len(self.adj_list)):
            if self.degree_out(0) != self.degree_out(i):
                return False
        return True

    def density(self):
        return self.count_edges / (self.count_nodes * (self.count_nodes - 1))

    def complement(self):
        g_aux = Graph(self.count_nodes)
        for i in range(len(self.adj_list)):
            for j in range(len(self.adj_list)):
                if j not in self.adj_list[i] and j != i and j not in g_aux.adj_list[i]:
                    g_aux.add_undirected_edge(i, j)
        return g_aux

    def subgraph(self, g2):
        if g2.count_nodes > self.count_nodes or g2.count_edges > self.count_edges:
            return False
        for i in range(len(g2.adj_list)):
            for j in g2.adj_list[i]:
                if j not in self.adj_list[i]:
                    return False
        return True

    def bfs(self, s: int):
        desc = [0 for _ in range(len(self.adj_list))]
        Q = [s]
        R = [s]
        desc[s] = 1
        while len(Q) != 0:
            u = Q.pop(0)
            for v in self.adj_list[u]:
                if desc[v] == 0:
                    Q.append(v)
                    R.append(v)
                    desc[v] = 1
        return R

    def depth_search(self, s):
        desc = [0 for _ in range(len(self.adj_list))]
        S = [s]
        R = [s]
        desc[s] = 1
        while len(S) != 0:
            u = S[-1]
            pop = True
            for v in self.adj_list[u]:
                if desc[v] == 0:
                    pop = False
                    S.append(v)
                    R.append(v)
                    desc[v] = 1
                    break
            if pop:
                S.pop()
        return R
    
        def depth_search(self, s):
        desc = [0 for _ in range(len(self.adj_list))]
        S = [s]
        R = [s]
        desc[s] = 1
        while len(S) != 0:
            u = S[-1]
            pop = True
            for v in self.adj_list[u]:
                if desc[v] == 0:
                    pop = False
                    S.append(v)
                    R.append(v)
                    desc[v] = 1
                    break
            if pop:
                S.pop()
        return R

    def connected(self):
        return len(self.depth_search(0)) == self.count_nodes

    def to_adj_matrix(self):
        adj_mat = [[0 for i in range(len(self.adj_list))] for j in range(len(self.adj_list))]
        for v in range(len(self.adj_list)):
            for e in self.adj_list[v]:
                adj_mat[v][e] = 1
        return adj_mat

    def is_neighbor(self, u, v):
        return v in self.adj_list[u] and u in self.adj_list[v]

    def is_valid_walk(self, walk: list[int]):
        for i in range(len(walk) - 1):
            if walk[i + 1] not in self.adj_list[walk[i]]:
                return False
        return True

    def is_valid_path(self, path: list[int]):  # Caminho
        desc = [0 for _ in range(self.count_nodes)]
        if self.is_valid_walk(path):
            for i in path:
                if desc[i] == 1:
                    return False
                desc[i] = 1
        else:
            return False
        return True

    def is_closed(self, walk: list[int]):
        if walk[0] == walk[-1] and self.is_valid_walk(walk):
            return True
        return False

    def degree_in_more_than(self, min_degree):
        """Returns the set of nodes that have the in degree larger than min_degree"""
        set_nodes = []
        for i in range(len(self.adj_list)):
            if self.degree_in(i) > min_degree:
                set_nodes.append(i)
        return set_nodes

    def degree_out_more_than(self, min_degree):
        """Returns the set of nodes that have the out degree larger than min_degree"""
        set_nodes = []
        for i in range(len(self.adj_list)):
            if self.degree_out(i) > min_degree:
                set_nodes.append(i)
        return set_nodes

    def nodes_having_in_degree(self, in_degree):
        """Returns the number of nodes having the given in_degree"""
        num = 0
        for i in range(len(self.adj_list)):
            if self.degree_in(i) == in_degree:
                num += 1
        return num

    def nodes_having_out_degree(self, out_degree):
        """Returns the number of nodes having the given out_degree"""
        num = 0
        for i in range(len(self.adj_list)):
            if self.degree_out(i) == out_degree:
                num += 1
        return num

    def diff_min_max_in_degree(self):
        """Returns the difference between the maximum and minimum in degree"""
        return self.degree_in(self.highest_degree_in()) - self.degree_in(self.lowest_degree_in())

    def diff_min_max_out_degree(self):
        """Returns the difference between the maximum and minimum out degree"""
        return self.degree_out(self.highest_degree_out()) - self.degree_out(self.lowest_degree_out())

    def is_directed(self):
        """Returns True if graph is directed, and False otherwise"""
        for i in range(self.count_nodes - 1):
            for j in self.adj_list[i]:
                if not (i in self.adj_list[j]):
                    return True
        return False

    def remove_directed_edge(self, u, v):
        if self.validate_node(u) and self.validate_node(v):
            print(f"Could not remove given edges cause nodes are out of range.")
        else:
            self.adj_list[u].remove(v)
            self.count_edges -= 1

    def remove_undirected_edge(self, u, v):
        if self.validate_node(u) and self.validate_node(v):
            print(f"Could not remove given edges cause nodes are out of range.")
        else:
            self.adj_list[u].remove(v)
            self.adj_list[v].remove(u)
            self.count_edges -= 2

    def add_node(self):
        self.adj_list.append([])
        self.count_nodes += 1

    def remove_node(self, u):
        if self.validate_node(u):
            print(f"Could not remove given edges cause nodes are out of range.")
        else:
            for i in range(len(self.adj_list)):
                if u in self.adj_list[i]:
                    self.adj_list[i].remove(u)
                    self.count_edges -= 2

                for j in range(len(self.adj_list[i])):
                    if self.adj_list[i][j] > u:
                        self.adj_list[i][j] -= 1
        self.adj_list.pop(u)
        self.count_nodes -= 1

    def __str__(self):
        repre = ""
        for adj in self.adj_list:
            repre += str(adj) + "\n"
        return repre
