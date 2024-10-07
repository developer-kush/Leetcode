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
        
        if 1 in deg.values():
            st = [i for i in range(n) if deg[i]==1][0]
            bfs = getBFS(st)
            res = [0]*n
            for i in range(n): res[bfs[i]]=i
            return [res]

        starts = [i for i in range(n) if deg[i]==2]
        s1 = starts[0]
        bfs1 = getBFS(s1)
        maxd = max(bfs1.values())
        s2 = [i for i in starts if bfs1[i]!=0 and bfs1[i]!=maxd][0]
        bfs2 = getBFS(s2)
        
        m, n = (bfs1[s2]+1, maxd-bfs1[s2]+1)
        res = [[0]*m for _ in range(n)]

        # print(bfs1[s2], maxd)
        # print(n, m, ":", s1, s2)

        for i in range(len(graph)):
            a, b = bfs1[i], bfs2[i]
            b -= (m-1)
            x = (a+b)//2
            y = a - x
            res[x][y] = i

        return res