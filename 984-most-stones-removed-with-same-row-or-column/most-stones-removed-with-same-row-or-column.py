class Disjoint_Set():
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.rank=[0]*n
        self.components=n
    
    def find(self,u):
        if self.parent[u]!=u:
            self.parent[u]=self.find(self.parent[u])
        return self.parent[u]

    def merge(self,u,v):
        u,v=self.find(u),self.find(v)
        if u==v:
            return
        if self.rank[u]<self.rank[v]:
            self.parent[u]=v
        elif self.rank[v]<self.rank[u]:
            self.parent[v]=u
        else:
            self.parent[v]=u
            self.rank[u]+=1
        self.components-=1

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n=len(stones)
        ds=Disjoint_Set(n)
        rows={}
        cols={}
        for i in range(n):
            r,c=stones[i]
            if r not in rows: rows[r]=[]
            if c not in cols: cols[c]=[]
            rows[r].append(i)
            cols[c].append(i)

        for r in rows:
            for i in range(1,len(rows[r])):
                ds.merge(rows[r][i-1],rows[r][i])
        for c in cols:
            for i in range(1,len(cols[c])):
                ds.merge(cols[c][i-1],cols[c][i])
            
        return n-ds.components
        