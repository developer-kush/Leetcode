class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        r, c = len(mat), len(mat[0])
        nummap = {}
        for i in range(r):
            for j in range(c):
                nummap[mat[i][j]] = (i, j)
        
        rows = [c]*r
        cols = [r]*c
        for idx, i in enumerate(arr):
            x, y  = nummap[i]
            rows[x] -= 1
            cols[y] -= 1
            if rows[x] == 0 or cols[y] == 0:
                return idx