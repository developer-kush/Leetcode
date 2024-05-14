class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        n, m = len(grid), len(grid[0])

        def rec(row, col):
            if grid[row][col] == 0: return float('-inf')

            gold = grid[row][col]
            grid[row][col] = 0

            res = 0
            for i, j in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                if 0 <= row + i < n and 0 <= col + j < m and grid[row+i][col+j] != 0:
                    res = max(res, rec(row+i, col+j))
            
            grid[row][col] = gold
            return res + gold

        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0: continue
                curr = rec(i, j)
                res = max(res, curr)

        return res