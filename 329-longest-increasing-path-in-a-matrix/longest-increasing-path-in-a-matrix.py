class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        n, m = len(matrix), len(matrix[0])

        memo = [[0 for _ in range(m)] for _ in range(n)]

        def rec(x,y):
            if memo[x][y]: return memo[x][y]
            res = 0
            for i, j in ((x+1, y), (x,y+1), (x-1,y), (x,y-1)):
                if 0<=i<n and 0<=j<m and matrix[i][j] < matrix[x][y]:
                    res = max(res, rec(i, j))
            memo[x][y] = res + 1
            return res + 1
        
        return max(rec(i,j) for j in range(m) for i in range(n)) 