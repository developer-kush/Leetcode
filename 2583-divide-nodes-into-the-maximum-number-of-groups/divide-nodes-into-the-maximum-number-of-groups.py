class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        vis = set()

        def bfs(start):
            q = deque([(1, start)])
            vis = {start:1}

            while q:
                d, node = q.popleft()
                for ne in graph[node]:
                    if ne in vis:
                        if abs(d-vis[ne]) != 1: return -1
                        continue
                    vis[ne] = d+1
                    q.append((d+1, ne)) 
            
            return max(vis.values())

        def solve(start):
            nodes = {start}
            q = deque([start])
            last = start
            while q:
                node = q.popleft()
                last = node
                for ne in graph[node]:
                    if ne in nodes: continue
                    nodes.add(ne)
                    q.append(ne)

            res = -1
            for node in nodes:
                res = max(res, bfs(node))
            return (res, nodes)

        res = 0
        for start in range(1,n+1):
            if start in vis: continue
            a, b = solve(start)
            if a == -1: return -1
            res += a
            vis |= b

        return res