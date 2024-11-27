class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = {i:{i+1} for i in range(n-1)}
        dist = {i:(n-1-i) for i in range(n)}

        res = []
        for u, v in queries:
            
            graph[u].add(v)
            for node in range(u, -1, -1):
                for ne in graph[node]:
                    dist[node] = min(dist[node], dist[ne]+1)

            res.append(dist[0])
        
        return res