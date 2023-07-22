class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        
        @cache
        def rec(x,y,mv):
            # if not 0<=x<n or not 0<=y<n: return 0
            if mv == 0: return 1
            tot = 0
            for i,j in ((x+1,y+2),(x+1,y-2),(x-1,y+2),(x-1,y-2),
                        (x+2,y+1),(x+2,y-1),(x-2,y+1),(x-2,y-1)):
                if 0<=i<n and 0<=j<n: tot += rec(i,j,mv-1)*0.125
            return tot
        
        return rec(row, column, k)

# 1 0 0
# 0 0 0
# 0 0 0