class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
    
    def find(self, val):
        if self.parent[val] != val: self.parent[val] = self.find(self.parent[val])
        return self.parent[val]

    def areConnected(self, a, b):
        return self.find(a) == self.find(b)

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b: return
        self.parent[b] = a

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges))

        for u, v in edges:
            if dsu.areConnected(u-1, v-1): return [u, v]
            dsu.union(u-1, v-1)