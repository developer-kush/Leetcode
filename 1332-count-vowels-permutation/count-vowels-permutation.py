class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = int(1e9 + 7)
        
        dp=[1,1,1,1,1]
        chars={
            0:[1,2,4],
            1:[0,2],
            2:[1,3],
            3:[2],
            4:[2,3]
        }
        
        for i in range(2,n+1):
            new = [
                (dp[1]+dp[2]+dp[4])%MOD,
                (dp[0]+dp[2])%MOD,
                (dp[1]+dp[3])%MOD,
                dp[2],
                (dp[2]+dp[3])%MOD
            ]
            dp=new
        
        return sum(dp)%MOD