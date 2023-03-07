from typing import Tuple
import heapq


class WeightedGraph:
    def __init__(self, count_nodes: int = 0, count_edges: int = 0, adj_list: list[list[Tuple[int, int]]] = []) -> None:
        self.count_nodes = count_nodes  # numero de nos
        self.count_edges = count_edges  # numero de arestas
        self.adj_list = adj_list  # lista de adjacencia

        if not adj_list:
            for _ in range(self.count_nodes):
                adj_list.append([])

    def add_directed_edge(self, u: int, v: int, w: int):
        if u < 0 or u >= len(self.adj_list) or v < 0 or v >= len(self.adj_list):
            print(f"Node u={u} or v={v} is out of allowed range (0, {self.count_nodes - 1})")
        self.adj_list[u].append((v, w))
        self.count_edges += 1

    def add_undirected_edge(self, u: int, v: int, w: int):
        self.add_directed_edge(u, v, w)
        self.add_directed_edge(v, u, w)

    def read_file(self, file_name):
        """Read graph file in Dimacs format"""
        with open(file_name, "r") as file:
            i = 0
            for line in file:
                i += 1
                if i == 1:
                    header = line.split(" ")
                    self.count_nodes = int(header[0])
                    self.adj_list = [[] for i in range(self.count_nodes)]
                else:
                    edge_data = line.split(" ")
                    u = int(edge_data[0])  # Source node
                    v = int(edge_data[1])  # Sink node
                    w = int(edge_data[2])  # Edge (u, v) weight
                    self.add_directed_edge(u, v, w)

    def bellmand_ford(self, s):
        dist = [float("inf") for _ in range(self.count_nodes)]
        pred = [None for _ in range(self.count_nodes)]

        dist[s] = 0

        for i in range(self.count_nodes - 1):
            for u in range(self.count_nodes):
                for (v, w) in self.adj_list[u]:
                    if dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w
                        pred[v] = u
        return dist, pred

    def bellmand_ford_better(self, s):
        dist = [float("inf") for _ in range(self.count_nodes)]
        pred = [None for _ in range(self.count_nodes)]

        dist[s] = 0

        for i in range(self.count_nodes - 1):
            trocou = False
            for u in range(self.count_nodes):
                for (v, w) in self.adj_list[u]:
                    if dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w
                        pred[v] = u
                        trocou = True
            if not trocou:
                break
        return dist, pred

    def min_dist_Q(self, Q, dist):
        min_dist = float("inf")
        min_node = None
        for n in Q:
            if dist[n] < min_dist:
                min_dist = dist[n]
                min_node = n
        return min_node

    def djikstra(self, s):
        dist = [float("inf") for _ in range(self.count_nodes)]
        pred = [None for _ in range(self.count_nodes)]
        dist[s] = 0
        Q = [v for v in range(self.count_nodes)]
        while len(Q) != 0:
            u = self.min_dist_Q(Q, dist)
            Q.remove(u)
            for v, w in self.adj_list[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    pred[v] = u
        return dist, pred

    def dijkstra_pq(self, s):
        dist = [float("inf")] * self.count_nodes
        pred = [-1] * self.count_nodes
        pq = []
        heapq.heapify(pq)  # Empty priority queue
        dist[s] = 0
        heapq.heappush(pq, [0, s])
        while len(pq) != 0:
            [min_dist, u] = heapq.heappop(pq)
            for (v, w) in self.adj_list[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    pred[v] = u
                    heapq.heappush(pq, [dist[v], v])
        return dist, pred
