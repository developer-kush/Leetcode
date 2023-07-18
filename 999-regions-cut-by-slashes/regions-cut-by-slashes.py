class DisjointSet:

    def __init__(self, grid):
        n, m = len(grid), len(grid[0])
        self.parent = {(x,y,c):(x,y,c) for c in range(4) for y in range(m) for x in range(n)}
        self.rank = {(x,y,c):0 for c in range(4) for y in range(m) for x in range(n)}
        self.components = 4*n*m

        for i in range(n):
            for j in range(m):
                if grid[i][j] == ' ':
                    self.merge((i,j,0), (i,j,1))
                    self.merge((i,j,0), (i,j,2))
                    self.merge((i,j,0), (i,j,3))
                elif grid[i][j] == '/':
                    self.merge((i,j,0),(i,j,1))
                    self.merge((i,j,2),(i,j,3))
                elif grid[i][j] == '\\':
                    self.merge((i,j,0),(i,j,2))
                    self.merge((i,j,1),(i,j,3))
                
        for i in range(n):
            for j in range(m):
                if j<m-1: self.merge((i,j,2),(i,j+1,1))
                if i<n-1: self.merge((i,j,3),(i+1,j,0))

    def find(self, key):
        if self.parent[key]!=key: 
            self.parent[key] = self.find(self.parent[key])
        return self.parent[key]
    
    def merge(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b: return
        if self.rank[a] < self.rank[b]: self.parent[a] = b
        elif self.rank[b] < self.rank[a]: self.parent[b] = a
        else:
            self.parent[a] = b
            self.rank[b] += 1
        self.components -= 1

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:

        ds = DisjointSet(grid)
        return ds.components