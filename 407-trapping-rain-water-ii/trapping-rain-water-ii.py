class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        n, m = len(heightMap), len(heightMap[0])
        if n < 3 or m < 3: return 0

        mx = max(max(row) for row in heightMap)
        remap = [[mx]*m for _ in range(n)]

        vis = set()
        q = []

        for j in range(1, m-1): 
            heappush(q, (heightMap[0][j], 0, j))
            heappush(q, (heightMap[-1][j], n-1, j))
        for i in range(1, n-1):
            heappush(q, (heightMap[i][0], i, 0))
            heappush(q, (heightMap[i][-1], i, m-1))

        for i, j in ((0, 0), (0, m-1), (n-1, 0), (n-1, m-1)):
            remap[i][j] = heightMap[i][j]
        
        while q:
            h, x, y = heappop(q)
            if (x, y) in vis: continue
            vis.add((x, y))
            remap[x][y] = min(remap[x][y], h)
            for u, v in ((x, y-1), (x, y+1), (x-1, y), (x+1, y)):
                if not (0 <= u < n and 0 <= v < m): continue
                heappush(q, (max(h, heightMap[u][v]), u, v))
        
        return sum(sum(remap[i][j]-heightMap[i][j] for j in range(m)) for i in range(n))