class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0]*n
        self.components = n

    def find(self, val):
        if self.parent[val]!=val: self.parent[val] = self.find(self.parent[val])
        return self.parent[val]

    def areConnected(self, a, b):
        return self.find(a) == self.find(b)

    def notConnected(self, a, b):
        return self.find(a) != self.find(b)
    
    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if self.rank[a] < self.rank[b]: self.parent[b] = a
        elif self.rank[b]<self.rank[a]: self.parent[a] = b
        else:
            self.parent[a] = b
            self.rank[b] += 1
        self.components -= 1

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice = DSU(n)
        bob = DSU(n)
        cnt = 0
        type1, type2, type3 = [], [], []
        for t, x, y in edges:
            if t == 1: type1.append((x - 1, y - 1))
            elif t == 2: type2.append((x - 1, y - 1))
            else: type3.append((x - 1, y - 1))

        for u, v in type3:
            if alice.notConnected(u, v) or bob.notConnected(u, v):
                alice.union(u, v)
                bob.union(u, v)
            else: cnt += 1

        for u, v in type2:
            if bob.notConnected(u, v): bob.union(u, v)
            else: cnt += 1
        
        for u, v in type1:
            if alice.notConnected(u, v): alice.union(u, v)
            else: cnt += 1
        
        if alice.components == 1 and bob.components == 1:
            return cnt
        return -1
