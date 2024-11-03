class Solution:
    def minTimeToReach(self, mat: List[List[int]]) -> int:

        N, M = len(mat), len(mat[0])
        hp = [(0, 0, 0, 0)]

        vis = set()
        
        while (hp[0][1], hp[0][2]) != (N-1, M-1):
            d, x, y, m = heappop(hp)
            vis.add((x, y, m))

            for u, v in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if not (0<=u<N and 0<=v<M) or (u, v) in vis: continue
                heappush(hp, (max(d+m+1, mat[u][v]+m+1), u, v, 1-m))
            
            while hp and (hp[0][1], hp[0][2], hp[0][3]) in vis: heappop(hp)

        return hp[0][0]