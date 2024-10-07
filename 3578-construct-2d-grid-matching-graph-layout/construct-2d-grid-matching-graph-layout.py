class Solution:
    def constructGridLayout(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def getBFS(src):
            q = deque([(0, src)])
            res = {src : 0}
            while q:
                d, curr = q.popleft()
                for ne in graph[curr]:
                    if ne in res: continue
                    res[ne] = d+1
                    q.append((d+1, ne))
            return res
        
        deg = {i:len(graph[i]) for i in range(n)}

        mndeg = min(deg.values())
        starts = [i for i in range(n) if deg[i]==mndeg]
        s1 = starts[0]
        bfs1 = getBFS(s1)
        maxd = max(bfs1.values())
        s2 = sorted(starts, key=lambda x: bfs1[x])[1]
        bfs2 = getBFS(s2)
        
        m, n = (bfs1[s2]+1, maxd-bfs1[s2]+1)
        res = [[0]*m for _ in range(n)]
        
        for i in range(len(graph)):
            a, b = bfs1[i], bfs2[i]
            b -= (m-1)
            x = (a+b)//2
            y = a - x
            res[x][y] = i

        return res