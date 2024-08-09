class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        otn=list(range(1,10))
        tot=0
        for i in range(1,len(grid)-1):
            for j in range(1,len(grid[0])-1):
                a = grid[i-1][j-1]
                b = grid[i-1][j]
                c = grid[i-1][j+1]
                d = grid[i][j-1]
                e = grid[i][j]
                f = grid[i][j+1]
                g = grid[i+1][j-1]
                h = grid[i+1][j]
                k = grid[i+1][j+1]
                if sorted([a,b,c,d,e,f,g,h,k])!=otn: continue
                tot+= (a+b+c)==(d+e+f)==(g+h+k)==(a+d+g)==(b+e+h)==(c+f+k)==(a+e+k)==(c+e+g)
        return tot