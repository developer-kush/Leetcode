class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rmax, cmax = [0]*n, [0]*n

        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                rmax[i] = max(rmax[i], val)
                cmax[j] = max(cmax[j], val)
        
        tot = 0
        for i in range(n):
            for j in range(n):
                tot += min(rmax[i], cmax[j])-grid[i][j]
        
        return tot