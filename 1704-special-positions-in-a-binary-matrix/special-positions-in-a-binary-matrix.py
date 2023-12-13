class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        col = Counter()
        row = Counter()
        for i, matrow in enumerate(mat):
            for j, matcol in enumerate(matrow):
                if matcol: 
                    row[i] += 1
                    col[j] += 1

        cnt = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if row[i] == col[j] == mat[i][j] == 1: cnt += 1
        
        return cnt