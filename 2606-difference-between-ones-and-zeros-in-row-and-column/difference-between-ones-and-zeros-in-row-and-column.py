class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        m=len(grid[0])
        rowzeroes=[]
        colzeroes=[]
        for i in grid:
            rowzeroes.append(i.count(0))
        for j in range(m):
            cnt=0
            for i in range(n):
                if grid[i][j]==0:
                    cnt+=1
            colzeroes.append(cnt)
        
        print(rowzeroes,colzeroes)
        
        for i in range(n):
            for j in range(m):
                grid[i][j]= m-rowzeroes[i]-rowzeroes[i]+n-colzeroes[j]-colzeroes[j]
        
        return grid