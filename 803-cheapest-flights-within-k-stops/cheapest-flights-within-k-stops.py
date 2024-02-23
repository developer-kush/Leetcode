class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {i:{} for i in range(n)}
        for u,v,w in flights: graph[v][u] = w
        mincost = {}
        
        def rec(src, k):
            if src == dst: return 0
            if (src,k) in mincost: return mincost[(src, k)]
            if k == 0 : return inf
            cost = float('inf')
            for neighbour in graph[src]:
                cost = min( cost, rec(neighbour, k-1) + graph[src][neighbour] )
            mincost[(src,k)] = cost
            return cost

        src, dst = dst, src
        ans = rec(src, k+1) 
        if ans == inf: return -1
        return ans