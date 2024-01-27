class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp,MOD=[1]+[0]*k,10**9+7
        for i in range(n):
            tmp,curr=[],0
            for j in range(k+1):
                curr+=dp[j]
                if j-i>=1: curr-=dp[j-i-1]
                tmp.append(curr%MOD)
            dp=tmp
        return dp[-1]