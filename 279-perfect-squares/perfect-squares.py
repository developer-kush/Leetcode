class Solution:
    def numSquares(self, n: int) -> int:
        
        @cache
        def rec(n):
            if n < 0: return float('inf')
            if n == 0: return 0

            res = float('inf')

            for i in range(int(sqrt(n)),0,-1):
                res = min(res, rec(n-i*i)+1)

            return res

        return rec(n)