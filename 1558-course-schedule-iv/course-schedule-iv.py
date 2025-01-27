class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        adj = [[float('inf')]*n for _ in range(n)]
        for u, v in prerequisites: adj[u][v] = 1
        for i in range(n): adj[i][i] = 0

        for k in range(n):
            for s in range(n):
                for t in range(n):
                    adj[s][t] = min(adj[s][t], adj[s][k]+adj[k][t])
        
        return [adj[x][y] !=float('inf') for x, y in queries]