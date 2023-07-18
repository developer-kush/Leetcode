class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = {i+1:[] for i in range(n)}
        for u, v in paths: 
            graph[u].append(v)
            graph[v].append(u)
        
        res = [0]*n
        visited = set()

        for i in range(1,n+1):
            if i in visited: continue
            visited.add(i)
            queue = deque([i])
            while queue:
                curr = queue.popleft()
                available = set(res[i-1] for i in graph[curr] if res[i-1])
                for color in range(1,5):
                    if color not in available: res[curr-1] = color; break
                for ne in graph[curr]:
                    if ne not in visited:
                        visited.add(ne)
                        queue.append(ne)
                        
        return res