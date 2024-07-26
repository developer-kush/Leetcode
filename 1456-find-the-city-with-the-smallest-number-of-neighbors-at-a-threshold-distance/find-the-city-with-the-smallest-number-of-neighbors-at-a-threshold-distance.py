class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = [[inf]*n for _ in range(n)]

        for u, v, w in edges: graph[u][v] = graph[v][u] = w
        for i in range(n): graph[i][i] = 0
        
        for m in range(n):
            for i in range(n):
                for j in range(n):
                    graph[i][j] = min(graph[i][j], graph[i][m] + graph[m][j])
        
        return min(range(n), key=lambda x: [sum(val <= distanceThreshold for val in graph[x]), -x])