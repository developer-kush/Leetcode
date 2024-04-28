class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        rows, cols = Counter(), Counter()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    rows[i] += 1
                    cols[j] += 1
        
        tot = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not grid[i][j]: continue
                tot += (rows[i] - 1)*(cols[j] - 1)
        return tot