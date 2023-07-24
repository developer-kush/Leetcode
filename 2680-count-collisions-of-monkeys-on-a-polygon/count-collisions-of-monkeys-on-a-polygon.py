class Solution:
    def monkeyMove(self, n: int) -> int:
        MOD = 10**9 + 7

        def fastPow(x, n):
            if x <= 1: return x
            if n == 0: return 1
            res = fastPow(x, n//2)
            if n&1 : return (res*res*x) % MOD
            return (res*res) % MOD

        return (fastPow(2, n)-2)%MOD