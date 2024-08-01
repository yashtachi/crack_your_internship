class Graph:

    def __init__(self, row, col, graph):
        self.ROW = row
        self.COL = col
        self.graph = graph

    def DFS(self, i, j):
        if (i < 0 or i >= len(self.graph) or
            j < 0 or j >= len(self.graph[0]) or
            self.graph[i][j] != 1):
            return

        self.graph[i][j] = -1

        self.DFS(i - 1, j - 1)
        self.DFS(i - 1, j)
        self.DFS(i - 1, j + 1)
        self.DFS(i, j - 1)
        self.DFS(i, j + 1)
        self.DFS(i + 1, j - 1)
        self.DFS(i + 1, j)
        self.DFS(i + 1, j + 1)

    def countIslands(self):
        count = 0
        for i in range(self.ROW):
            for j in range(self.COL):
                if self.graph[i][j] == 1:
                    self.DFS(i, j)
                    count += 1

        return count


graph = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 1],
    [1, 0, 0, 1, 1],
    [0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1]
]


row = len(graph)
col = len(graph[0])

g = Graph(row, col, graph)

print("Number of islands is:", g.countIslands())