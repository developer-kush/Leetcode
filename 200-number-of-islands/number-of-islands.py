class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        tot=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    tot+=1
                    stack=[[i,j]]
                    grid[i][j]='0'
                    while len(stack):
                        x,y=stack.pop()
                        for a,b in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                            if 0<=a<len(grid) and 0<=b<len(grid[0]) and grid[a][b]=='1':
                                grid[a][b]='0'
                                stack.append((a,b))
        return tot