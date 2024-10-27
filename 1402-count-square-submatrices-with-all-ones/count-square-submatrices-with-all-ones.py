class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])

        maxu = list(matrix[0]) 
        for i in range(1, n):
            maxl = matrix[i][0]
            for j in range(1, m):
                if matrix[i][j] == 0: maxl = maxu[j] = 0; continue
                matrix[i][j] = min(maxl, maxu[j], matrix[i-1][j-1])+1
                maxu[j]+=1
                maxl+=1
        
        return sum(sum(row) for row in matrix)