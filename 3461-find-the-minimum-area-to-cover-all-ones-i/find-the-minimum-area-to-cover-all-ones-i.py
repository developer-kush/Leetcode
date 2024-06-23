class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        mn_x, mn_y, mx_x, mx_y = float('inf'), float('inf'), 0, 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    mn_x = min(mn_x, i)
                    mx_x = max(mx_x, i)
                    mn_y = min(mn_y, j)
                    mx_y = max(mx_y, j)
        
        return (mx_x-mn_x+1)*(mx_y-mn_y+1)