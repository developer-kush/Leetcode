class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m,n=len(matrix),len(matrix[0])
        
        for i in range(m):
            for j in range(1,n):
                matrix[i][j]+=matrix[i][j-1]
        
        tot=0
        for x1 in range(n):
            for x2 in range(x1,n):
                memo={0:1}
                curr=0
                for y in range(m):
                    curr+=matrix[y][x2]-(matrix[y][x1-1] if x1>0 else 0)
                    tot+= memo[curr-target] if curr-target in memo else 0
                    if curr not in memo: memo[curr]=0
                    memo[curr]+=1
        return tot
                        