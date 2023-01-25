from graph import Graph

g1 = Graph(7)

g1.add_undirected_edge(0, 1)
g1.add_undirected_edge(0, 3)
g1.add_undirected_edge(1, 2)
g1.add_undirected_edge(2, 3)
g1.add_undirected_edge(2, 4)
g1.add_undirected_edge(2, 6)

print("GRAPH1: ", g1.adj_list)
print(f"    |HIGHEST_DEGREE_OUT: {g1.highest_degree_out()}")
print(f"    |DEGREE_OUT(0): {g1.degree_out(0)}")
print(f"    |DEGREE_OUT(1): {g1.degree_out(1)}")
print(f"    |DENSITY: {g1.density():.4f}")
print(f"    |IS_COMPLETE: {g1.is_complete()}")
print(f"    |IS_REGULAR: {g1.is_regular()}")
print(f"    |BFS(0): {g1.bfs(0)}")
print(f"    |DEPTH_SEARCH(0): ", g1.depth_search(0))
g3 = g1.complement()
print(f"    |COMPLEMENT: {g3.adj_list}")
print(f"    |CONNECTEDNESS: {g1.connected()}")

g2 = Graph(3)

g2.add_undirected_edge(0, 1)
g2.add_undirected_edge(1, 2)
g2.add_undirected_edge(2, 0)

print("\nGRAPH2: ", g2.adj_list)
print(f"    |GRAPH 2 IS SUBGRAPH OF 1?: {g1.subgraph(g2)}")
