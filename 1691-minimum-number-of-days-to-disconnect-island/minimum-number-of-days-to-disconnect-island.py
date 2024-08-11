class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        def count(grid, pc=False):
            nonlocal n, m

            cp = [list(row) for row in grid]

            comp = 0
            vis = set()
            for i in range(n):
                for j in range(m):
                    if not grid[i][j] or (i, j) in vis: continue
                    comp += 1
                    stack = [(i, j)]
                    vis.add((i, j))

                    while stack:
                        a, b = stack.pop()
                        cp[a][b] = 0
                        for x, y in [(a+1, b), (a, b+1), (a-1, b), (a, b-1)]:
                            if not (0 <= x < n and 0 <= y < m): continue
                            if not grid[x][y] or (x, y) in vis: continue
                            vis.add((x, y))
                            stack.append((x, y))

            return comp
        
        if count(grid) != 1: return 0
        
        for i in range(n):
            for j in range(m):

                if grid[i][j]: 
                    grid[i][j] = 0
                    if count(grid) != 1: return 1
                    grid[i][j] = 1

        return 2

# 1 5