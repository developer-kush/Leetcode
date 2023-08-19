class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0]*n
    
    def find(self, key):
        if self.parent[key]!=key: self.parent[key] = self.find(self.parent[key])
        return self.parent[key]

    def merge(self, u, v):
        u, v = self.find(u), self.find(v)
        if u == v : return False
        if self.rank[u]>self.rank[v]: self.parent[v] = u
        elif self.rank[v]>self.rank[u]: self.parent[u] = v
        else:
            self.rank[u]+=1
            self.parent[v] = u
        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edges = sorted([[idx,u,v,w] for idx, (u,v,w) in enumerate(edges)], key=lambda x:x[3])

        def mstScore(pretaken = None, discarded = None):
            dsu = DSU(n)
            rem = n-1
            tot = 0

            if pretaken is not None:
                dsu.merge(pretaken[0],pretaken[1])
                tot += pretaken[2]
                rem -=1

            for eid,u,v,w in edges:
                if eid is discarded: continue
                if dsu.merge(u,v): tot += w; rem -= 1
                if not n: break

            if rem: return float('inf')
            return tot
        
        critical = set()
        psuedo = set()

        mscore = mstScore()
        for eid,*rem in edges:
            if  mstScore(discarded = eid) > mscore: critical.add(eid)
            elif mstScore(pretaken = rem) == mscore: psuedo.add(eid)

        return [sorted(critical), sorted(psuedo)]
