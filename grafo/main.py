from graph import Graph

g1 = Graph(4)
g1.add_directed_edge(0, 2)
g1.add_directed_edge(0, 3)
g1.add_directed_edge(1, 0)
g1.add_directed_edge(2, 0)
g1.add_directed_edge(3, 2)

print(g1.degree_in(0))
print(g1.degree_in(1))
print(g1.degree_in(2))


print(g1.adj_list)
