class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n=len(grid)
        islands={0:0}
        i_id=2
        currmax=0
        
        def rec(i,j,island):
            grid[i][j]=island
            tot=1
            for x,y in ([i+1,j],[i-1,j],[i,j+1],[i,j-1]):
                if 0<=x<n and 0<=y<n and grid[x][y]==1:
                    tot+=rec(x,y,island)
            return tot
        
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    islands[i_id]=rec(i,j,i_id)
                    currmax=max(currmax,islands[i_id])
                    i_id+=1
            
        for i in range(n):
            for j in range(n):
                if grid[i][j]==0:
                    st=set(grid[x][y] for x,y in ([i+1,j],[i-1,j],[i,j-1],[i,j+1]) if 0<=x<n and 0<=y<n)
                    currtot=sum(islands[i] for i in st)+1
                    currmax=max(currmax,currtot)
            
        return currmax