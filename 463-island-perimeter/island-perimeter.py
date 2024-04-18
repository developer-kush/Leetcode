class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        peri=0
        for i in range(n):
            for j in range(m):
                if not grid[i][j]: continue
                if i==0 or grid[i-1][j]==0: peri+=1
                if i==n-1 or grid[i+1][j]==0: peri+=1
                if j==0 or grid[i][j-1]==0: peri+=1
                if j==m-1 or grid[i][j+1]==0: peri+=1
        return peri