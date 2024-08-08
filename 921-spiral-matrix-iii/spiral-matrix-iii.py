class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, r: int, c: int) -> List[List[int]]:
        xdist = max(c, cols-1-c)
        ydist = max(r, rows-1-r)
        res = [[r, c]]

        for i in range(1, max(xdist, ydist)+1):
            if c+i < cols:
                for x in range(max(0, r-i+1), min(r+i+1, rows)): res.append([x, c+i])

            if r+i < rows:
                for x in range(min(cols-1, c+i-1), max(-1, c-i-1), -1): res.append([r+i, x])

            if c-i >= 0:
                for x in range(min(rows-1, r+i-1), max(-1, r-i-1), -1): res.append([x, c-i])

            if r-i >= 0:
                for x in range(max(0, c-i+1), min(c+i+1, cols)): res.append([r-i, x])

        # grid = [[0]*cols for _ in range(rows)]
        # for idx, (u, v) in enumerate(res, 1):
        #     try: grid[u][v] = idx
        #     except: pass
        # for row in grid: print(*row)

        return res