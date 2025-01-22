class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n,m=len(isWater),len(isWater[0])
        
        for i in range(n):
            for j in range(m):
                isWater[i][j] = 0 if isWater[i][j] else inf
        for i in range(n):
            for j in range(1,m):
                isWater[i][j] = min(isWater[i][j-1]+1,isWater[i][j])
        for i in range(1,n):
            for j in range(m):
                isWater[i][j] = min(isWater[i-1][j]+1,isWater[i][j])
        for i in range(n):
            for j in range(m-2,-1,-1):
                isWater[i][j] = min(isWater[i][j+1]+1,isWater[i][j])
        for i in range(n-2,-1,-1):
            for j in range(m):
                isWater[i][j] = min(isWater[i+1][j]+1,isWater[i][j])
        return isWater
        # for i in isWater: print(*i)