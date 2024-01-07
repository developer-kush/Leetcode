class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:

        if a == e and (c!=e or sorted([b, d, f])[1]!=d): return 1
        if b == f: 
            if d == f :
                if sorted([a, c, e])[1]!=c: return 1
            else: return 1

        if c + d == e + f and (a+b!=e+f or sorted([c, a, e])[1]!=a): return 1

        if c - d == e - f and (a-b!=e-f or sorted([c, a, e])[1]!=a): return 1

        return 2