class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        # grid = [['.']*8 for _ in range(8)]
        # grid[a-1][b-1] = 'R'
        # grid[c-1][d-1] = 'B'
        # grid[e-1][f-1] = 'Q'


        # for row in grid: print(*row)

        if a == e:
            if c == e :
                if sorted([b, d, f])[1]!=d: return 1
            else: return 1
        if b == f: 
            if d == f :
                if sorted([a, c, e])[1]!=c: return 1
            else: return 1

        if c + d == e + f and (a+b!=e+f or sorted([c, a, e])[1]!=a): return 1

        if c - d == e - f and (a-b!=e-f or sorted([c, a, e])[1]!=a): return 1

        return 2