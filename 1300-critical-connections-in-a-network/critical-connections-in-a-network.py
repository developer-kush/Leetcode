class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        low = [0] * n
        disc = [0] * n
        parent = [-1] * n
        bridges = []
        time = [0]

        def dfs(u):
            disc[u] = low[u] = time[0]
            time[0] += 1

            for v in graph[u]:
                if disc[v] == 0:
                    parent[v] = u
                    dfs(v)
                    low[u] = min(low[u], low[v])
                    if low[v] > disc[u]:
                        bridges.append([u, v])
                elif v != parent[u]:
                    low[u] = min(low[u], disc[v])

        for i in range(n):
            if disc[i] == 0:
                dfs(i)

        return bridges