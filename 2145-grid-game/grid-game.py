class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:

        n = len(grid[0])

        def getRangeSum(arr):
            cpy = list(arr)
            for i in range(1, len(cpy)): cpy[i]+=cpy[i-1]
            def inner(l, r):
                if l == 0: return cpy[r]
                else: return cpy[r] - cpy[l-1]
            return inner
        
        a, b = grid
        geta, getb = getRangeSum(a), getRangeSum(b)

        res = min(geta(1, n-1), getb(0, n-2))
        for i in range(1, n-1):
            res = min(res, max(getb(0, i-1), geta(i+1, n-1)))

        return res