class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        mx = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not grid[i][j]: continue
                cnt = 0
                stack = [(i, j)]
                while stack:
                    x, y = stack.pop()
                    cnt += grid[x][y]
                    grid[x][y] = 0
                    for a, b in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                        if 0<=a<n and 0<=b<m and grid[a][b]:
                            stack.append((a, b))

                mx = max(mx, cnt)
        return mx