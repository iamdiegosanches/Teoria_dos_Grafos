import pandas as pd
import time
from graph import Graph

start_time = time.time()

with open("mazes/maze50.txt") as test:
    maze = []
    for line in test:
        maze.append([i for i in line.strip("\n")])
    df = pd.DataFrame(maze)
    # print(df)
    test.close()

g1 = Graph(len(df.axes[0]), len(df.axes[1]))


for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j] == "#":
            g1.adj_list.pop((i, j))
            continue
        try:
            if maze[i][j + 1] != "#":
                g1.add_directed_edge((i, j), (i, j+1))
        except IndexError:
            pass
        try:
            if maze[i + 1][j] != "#":
                g1.add_directed_edge((i, j), (i+1, j))
        except IndexError:
            pass
        try:
            if maze[i - 1][j] != "#":
                g1.add_directed_edge((i, j), (i-1, j))
        except IndexError:
            pass
        try:
            if maze[i][j - 1] != "#" and maze[i][j - 1] != "E":
                g1.add_directed_edge((i, j), (i, j-1))
        except IndexError:
            pass

# print(g1.adj_list)
print(g1.depth_search())
# TO-DO: NAO ADICIONAR CONEXAO -1 (ELEMENTO DE TRAS PARA FRENTE)

print("--- %s seconds ---" % (time.time() - start_time))
