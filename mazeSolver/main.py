import pandas as pd
import time
from graph import Graph

with open("mazes/maze3.txt") as test:
    maze = []
    for line in test:
        maze.append([i for i in line.strip("\n")])
    df = pd.DataFrame(maze)
    print(df)
    test.close()

g1 = Graph(len(df.axes[0]), len(df.axes[1]))

start: tuple = (0, 0)
end: tuple = (0, 0)

for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j] == "#":
            g1.adj_list.pop((i, j))
        else:
            if maze[i][j] == "E":
                end = (i, j)
            if maze[i][j] == "S":
                start = (i, j)
            if i != 0:
                if maze[i - 1][j] != "#":
                    g1.add_directed_edge((i, j), (i - 1, j))
            if j != len(maze[i]) - 1:
                if maze[i][j + 1] != "#":
                    g1.add_directed_edge((i, j), (i, j + 1))
            if i != len(maze) - 1:
                if maze[i + 1][j] != "#":
                    g1.add_directed_edge((i, j), (i + 1, j))
            if j != 0:
                if maze[i][j - 1] != "#":
                    g1.add_directed_edge((i, j), (i, j-1))


# print(g1.adj_list)
start_time = time.time()
print(g1.depth_search(start, end))
print("--- %s seconds ---" % (time.time() - start_time))
