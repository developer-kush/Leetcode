class Solution:
    def minNonZeroProduct(self, p: int) -> int:

        MOD = 10**9 + 7
        nums = 2**p - 1

        def fastPow(x, p):
            if p == 0: return 1

            res = fastPow(x, p>>1)

            if p&1: return res*res*x % MOD
            return res*res % MOD

        return (nums* fastPow(nums-1,nums//2))%MOD