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


g2 = Graph(7)
g1.complement(g2)

print(g2.adj_list)

print(f"Is_regular: {g2.is_regular()}")
