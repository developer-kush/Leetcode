inf = float('inf')

class Solution:
    def numSquares(self, n: int) -> int:

        memo = [inf]*(n+1)
        memo[0] = 0

        for i in range(1, n+1):
            for j in range(int(sqrt(i))+1):
                memo[i] = min(memo[i], memo[i-j*j]+1)

        return memo[n]    
        

        # @cache
        # def rec(n): # MINIMUM PERFECT SQUARES TO MAKE N
        #     if n < 0: return float('inf')
        #     if n == 0: return 0

        #     res = float('inf')
        #     for i in range(int(sqrt(n)),0,-1):
        #         res = min(res, rec(n-i*i)+1)

        #     return res

        # return rec(n)
