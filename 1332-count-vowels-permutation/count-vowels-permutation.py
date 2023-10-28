class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = int(1e9 + 7)
        
        dp=[1,1,1,1,1]
        
        for i in range(2,n+1):
            dp = [
                (dp[1]+dp[2]+dp[4])%MOD,
                (dp[0]+dp[2])%MOD,
                (dp[1]+dp[3])%MOD,
                dp[2],
                (dp[2]+dp[3])%MOD
            ]
        
        return sum(dp)%MOD