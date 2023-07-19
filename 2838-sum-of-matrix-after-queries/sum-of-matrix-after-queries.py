class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        row = col = n
        rows = set()
        cols = set()

        tot = 0
        for i in range(len(queries)-1,-1,-1):
            typ, idx, val = queries[i]
            if typ: 
                if idx in cols: continue
                cols.add(idx)
                tot += val*row
                col -= 1
            else:
                if idx in rows: continue
                rows.add(idx)
                tot += val*col
                row-=1

        return tot