class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        vis = set()
        q = [(grid[0][0], 0, 0)]
        
        while q and (q[0][1:] != (n-1, m-1)):
            d, x, y = heappop(q)
            
            if (x, y) in vis: continue
            vis.add((x, y))

            for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
                nx, ny = x+dx, y+dy
                if 0<=nx<n and 0<=ny<m:
                    heappush(q, (d+grid[nx][ny], nx, ny))

        if q: return q[0][0]
        return 0