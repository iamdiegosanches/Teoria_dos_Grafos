# from graph import Graph
from weightedGraph import WeightedGraph
import time
#
# g1 = Graph(7)
#
# g1.add_undirected_edge(0, 1)
# g1.add_undirected_edge(0, 3)
# g1.add_undirected_edge(1, 2)
# g1.add_undirected_edge(2, 3)
# g1.add_undirected_edge(2, 4)
# g1.add_undirected_edge(2, 6)
#
# print("GRAPH1: ", g1.adj_list)
# print(f"    |HIGHEST_DEGREE_OUT: {g1.highest_degree_out()}")
# print(f"    |LOWEST_DEGREE_OUT: {g1.lowest_degree_out()}")
# print(f"    |DEGREE_OUT(0): {g1.degree_out(0)}")
# print(f"    |DEGREE_OUT(1): {g1.degree_out(1)}")
# print(f"    |DENSITY: {g1.density():.4f}")
# print(f"    |IS_COMPLETE: {g1.is_complete()}")
# print(f"    |IS_REGULAR: {g1.is_regular()}")
# print(f"    |BFS(0): {g1.bfs(0)}")
# print(f"    |DEPTH_SEARCH(0): ", g1.depth_search(0))
# g3 = g1.complement()
# print(f"    |COMPLEMENT: {g3.adj_list}")
# print(f"    |CONNECTEDNESS: {g1.connected()}")
# print(f"    |IS_NEIGHBOR(3, 2): {g1.is_neighbor(3, 2)}")
# print(f"    |IS_NEIGHBOR(0, 14): {g1.is_neighbor(0, 14)}")
# print(f"    |IS_NEIGHBOR(0, 2): {g1.is_neighbor(0, 2)}")
# print(f"    |0-1-2-3-0 IS A VALID WALK: {g1.is_valid_walk([0, 1, 2, 3, 0])}")
# print(f"    |0-1-2-3-1 IS A VALID WALK: {g1.is_valid_walk([0, 1, 2, 3, 1])}")
# print(f"    |0-1-2-3-0 IS A CLOSED WALK: {g1.is_closed([0, 1, 2, 3, 0])}")
# print(f"    |0-1-2-3-1 IS A CLOSED WALK: {g1.is_closed([0, 1, 2, 3, 1])}")
# print(f"    |0-1-2-3 IS A VALID PATH: {g1.is_valid_path([0, 1, 2, 3])}")
# print(f"    |REMOVE UNDIRECTED EDGE 2-4:")
# g1.remove_undirected_edge(2, 4)
# print(f"    |NEW GRAPH1: ", g1.adj_list)
# print(f"    |NODES_HAVING_IN_DEGREE(3): {g1.nodes_having_in_degree(3)}): ")
# print(f"    |NODES_HAVING_OUT_DEGREE(3): {g1.nodes_having_out_degree(3)}): ")
# print(f"    |GRAPH ADJ LIST TO MAT LIST: ")
# m1 = g1.to_adj_matrix()
# for i in range(len(m1)):
#     print(f"    {m1[i]}")
# print(f"    |DIFF_MIN_MAX_OUT_DEGREE: {g1.diff_min_max_out_degree()}")
# print(f"    |DIFF_MIN_MAX_IN_DEGREE: {g1.diff_min_max_in_degree()}")
# print(f"    |DEGREE_OUT_MORE_THAN 1: {g1.degree_out_more_than(1)}")
# print(f"    |DEGREE_IN_MORE_THAN 1: {g1.degree_in_more_than(1)}")
# print(f"    |REMOVE NODE: 0")
# g1.remove_node(0)
# print(f"    |NEW GRAPH1: ", g1.adj_list)
# print(f"    |IS_DIRECTED: {g1.is_directed()}")
#
# g2 = Graph(3)
#
# g2.add_undirected_edge(0, 1)
# g2.add_undirected_edge(1, 2)
# g2.add_undirected_edge(2, 0)
#
# print("\nGRAPH2: ", g2.adj_list)
# print(f"    |GRAPH 2 IS SUBGRAPH OF 1?: {g1.subgraph(g2)}")


# Creating a grapy with brute force, by hand.
# g2 = WeightedGraph(5)
# g2.add_directed_edge(0, 1, 6)  # Origin node, destiny node, weight
# g2.add_directed_edge(0, 2, 2)
# g2.add_directed_edge(1, 2, 3)
# g2.add_directed_edge(1, 3, 1)
# g2.add_directed_edge(1, 4, 3)
# g2.add_directed_edge(2, 1, 2)
# g2.add_directed_edge(2, 3, 5)
# g2.add_directed_edge(3, 4, 3)

# print(g2.adj_list)

# Method for creating a weighted graph reading from a file .txt
g3 = WeightedGraph(9)
g3.read_file("datasets/shortestPath/USA-road-dt.NY.txt")

start_time = time.time()
g3.djikstra_heap_queue(0)
# g3.djikstra(0)

print(f"Tempo de execu????o {time.time() - start_time}")

# print(g3.adj_list)
