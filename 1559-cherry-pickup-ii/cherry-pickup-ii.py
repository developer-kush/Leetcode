class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        dp = {(0, m-1): grid[0][0] + grid[0][m-1]}

        for row in range(1, n):
            curr = {}
            for i in range(m):
                for j in range(i+1, m):
                    first = [i-1, i, i+1]
                    second = [j-1, j, j+1]
                    pairs = [(x, y) for x in first for y in second if x != y]
                    for x, y in pairs: curr[(i, j)] = max(curr.get((i,j), float('-inf')), grid[row][i]+grid[row][j] + dp.get((x,y), float('-inf')) )

            dp = curr

        return max(dp.values())