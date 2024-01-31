class Solution:
    def minCut(self, s: str) -> int:

        n = len(s)
        graph = defaultdict(list)

        # populating graph
        for i in range(n):
            l = r = i
            while l >= 0 and r < n and s[l]==s[r]:
                graph[l].append(r)
                l, r = l-1, r+1
            
        for i in range(n-1):
            l, r = i, i+1
            while l >= 0 and r < n and s[l]==s[r]:
                graph[l].append(r)
                l, r = l-1, r+1
        
        # using bfs
        q = deque([[0, 0]])
        visited = set([0])
        while q:
            dist, node = q.popleft()
            for ne in graph[node]:
                if ne == n-1: return dist
                if ne+1 in visited: continue
                visited.add(ne+1)
                q.append([dist+1, ne+1])
        
        return n