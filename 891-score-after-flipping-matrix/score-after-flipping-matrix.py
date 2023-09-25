class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        for i in range(n):
            if grid[i][0] == 0: 
                for j in range(m): grid[i][j] = 1-grid[i][j]
        
        curr, tot = 1, 0
        for i in range(m-1,-1,-1):
            ones = sum(grid[j][i] for j in range(n))
            ones = max(ones, n-ones)
            tot += curr*ones
            curr <<= 1
        
        return tot