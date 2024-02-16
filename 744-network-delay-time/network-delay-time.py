class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # Creating graph
        graph = defaultdict(dict)
        for u,v,w in times: graph[u][v] = w

        # A traversal
        visited = set()
        vismax = 0
        q = [[0, k]]

        while q:
            time, node = heappop(q)
            if node in visited: continue
            visited.add(node)
            vismax = max(vismax, time)

            for ne in graph[node]: heappush(q, [time+graph[node][ne], ne])

        # Returning Solution
        if len(visited) != n: return -1
        return vismax