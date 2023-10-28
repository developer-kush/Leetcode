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
            new=[0,0,0,0,0]
            for j in range(5):
                for k in chars[j]:
                    new[j] = (new[j] + dp[k])%MOD
            dp=new
        
        return sum(dp)%MOD