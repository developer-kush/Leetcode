class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        for row in range(len(grid)-2, -1, -1):
            srt = sorted(grid[row+1])
            if srt[0] == srt[1]: 
                for j in range(len(grid)): grid[row][j] += srt[0]
            else:
                idx = grid[row+1].index(srt[0])
                for j in range(len(grid)):
                    if j == idx: grid[row][j] += srt[1]
                    else: grid[row][j] += srt[0]
        return min(grid[0])