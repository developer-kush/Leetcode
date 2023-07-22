class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {}

        def rec(n):
            if n in memo: return memo[n]
            if n < 0: return 0
            if n == 0: return 1
            memo[n] = rec(n-1)+rec(n-2)
            return memo[n]
        
        return rec(n)


# 1 2 1 2 1 2 -> sum = n

# Dp Finding :

# choices          -->  Recursion
# Optimal/Total    ->

# Storage of Results for recurring subproblems

# MEMOIZATION
# TABULATION


