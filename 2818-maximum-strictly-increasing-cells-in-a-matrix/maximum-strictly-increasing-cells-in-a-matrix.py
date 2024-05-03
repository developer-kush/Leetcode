class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:    
        n, m = len(mat), len(mat[0])
        colmax, rowmax = defaultdict(int), defaultdict(int)

        valij = defaultdict(list)
        for i in range(n):
            for j in range(m):
                valij[mat[i][j]].append((i, j))

        res = 1

        for key in sorted(valij, reverse = True):
            row_c, col_c = defaultdict(int), defaultdict(int)
            for i, j in valij[key]:
                potential = max(rowmax[i], colmax[j]) + 1
                row_c[i] = max(row_c[i], potential)
                col_c[j] = max(col_c[j], potential)
                res = max(res, row_c[i], col_c[i])
            for key in row_c: rowmax[key] = max(rowmax[key], row_c[key])
            for key in col_c: colmax[key] = max(colmax[key], col_c[key])

        return res