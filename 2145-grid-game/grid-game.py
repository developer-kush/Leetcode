class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:

        n = len(grid[0])
        
        a, b = grid
        for i in range(1, n):
            a[i] += a[i-1]
            b[i] += b[i-1]

        res = min(a[n-1]-a[0], b[n-2])
        for i in range(1, n-1): res = min(res, max(b[i-1], a[n-1]-a[i]))

        return res