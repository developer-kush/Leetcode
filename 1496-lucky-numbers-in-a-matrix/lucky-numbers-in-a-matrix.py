class Solution:
    def luckyNumbers (self, mat: List[List[int]]) -> List[int]:
        n, m = len(mat), len(mat[0])
        row = [min(row) for row in mat]
        col = [max(mat[i][j] for i in range(n)) for j in range(m)]
        lucky = [mat[i][j] for i in range(n) for j in range(m) if mat[i][j] == row[i] == col[j]]
        return lucky