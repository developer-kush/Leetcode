class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        # self.adj = [[inf]*n for _ in range(n)]
        self.cost = [[inf]*n for _ in range(n)]
        for i in range(n): self.cost[i][i] = 0
        for u, v, w in edges: self.cost[u][v] = w
        for k in range(self.n):
            for u in range(self.n):
                for v in range(self.n):
                    self.cost[u][v] = min(self.cost[u][v], self.cost[u][k]+self.cost[k][v])

    def addEdge(self, edge: List[int]) -> None:
        u, v, w = edge
        if w >= self.cost[u][v]: return
        self.cost[u][v] = w
        for k in sorted([u, v]):
            for u in range(self.n):
                for v in range(self.n):
                    self.cost[u][v] = min(self.cost[u][v], self.cost[u][k]+self.cost[k][v])

    def shortestPath(self, node1: int, node2: int) -> int:
        if self.cost[node1][node2] == inf: return -1
        return self.cost[node1][node2]

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)