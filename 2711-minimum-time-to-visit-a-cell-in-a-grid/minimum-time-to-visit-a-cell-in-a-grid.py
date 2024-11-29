class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        vis = set()

        q = [(0, 0, 0)]

        if grid[0][1] > 1 and grid[1][0] > 1: return -1
        
        while q:
            d, x, y = heappop(q)
            if (x, y) == (n-1, m-1): return d

            for nx, ny in ((x, y-1), (x-1, y), (x, y+1), (x+1, y)):
                if not (0 <= nx < n and 0 <= ny < m) or (nx, ny) in vis: continue
                vis.add((nx, ny))

                nd = max(d+1, grid[nx][ny]) + ((grid[nx][ny]-d-1)&1 if grid[nx][ny] > d else 0)

                heappush(q, (nd , nx, ny))