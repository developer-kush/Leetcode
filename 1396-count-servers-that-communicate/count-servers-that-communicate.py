class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rowc = [0]*len(grid)
        colc = [0]*len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    rowc[i] += 1
                    colc[j] += 1
        
        cnt = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (rowc[i] > 1 or colc[j] > 1): 
                    cnt += 1

        return cnt