class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0]*n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u, v):
        u, v = self.find(u), self.find(v)
        if u == v: return False
        if self.rank[u] < self.rank[v]:
            self.parent[u] = v
        elif self.rank[v] < self.rank[u]:
            self.parent[v] = u
        else:
            self.rank[u] += 1
            self.parent[v] = u

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        n, m = len(grid1), len(grid1[0])

        size = n*m
        def key(i,j): 
            nonlocal n, m
            return i*m + j

        dsu = DisjointSet(size)

        for i in range(n):
            for j in range(m):
                if i and grid1[i][j] == grid1[i-1][j]:
                    dsu.union(key(i, j), key(i-1, j))
                if j and grid1[i][j] == grid1[i][j-1]:
                    dsu.union(key(i, j), key(i, j-1))

        tot = 0

        for i in range(n):
            for j in range(m):
                if not grid2[i][j]: continue
                lands = set()
                st = [(i, j)]
                grid2[i][j] = 0
                while st:
                    x, y = st.pop()
                    lands.add(dsu.find(key(x, y)))
                    for p, q in ((x, y+1), (x+1, y), (x, y-1), (x-1, y)):
                        if not (0<=p<n and 0<=q<m) or not grid2[p][q]: continue
                        st.append((p, q))
                        grid2[p][q] = 0
                if len(lands) == 1 and grid1[i][j]: tot += 1

        return tot