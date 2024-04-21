class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination: return True

        graph = {i:set() for i in range(n)}
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
            
        visited = [False]*n
        def dfs(curr):
            if curr == destination:
                return True
            for ne in graph[curr]:
                if not visited[ne]:
                    visited[ne]=True
                    if dfs(ne):
                        return True
            return False
        return dfs(source)