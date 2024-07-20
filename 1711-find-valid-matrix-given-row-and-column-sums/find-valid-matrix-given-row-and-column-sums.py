class Solution:
    def restoreMatrix(self, rs: List[int], cs: List[int]) -> List[List[int]]:
        n, m = len(rs), len(cs)
        mat = [[0]*m for _ in range(n)]

        roworder = sorted(range(n), key = lambda x : rs[x])
        colorder = sorted(range(m), key = lambda x : cs[x])
        
        for r in roworder:
            curr = rs[r]
            for c in colorder:
                val = cs[c]
                fill = min(curr, val)
                mat[r][c] = fill
                curr -= fill
                cs[c] -= fill
                if not curr: break

        return mat