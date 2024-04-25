class Solution:
    def longestIdealString(self, s: str, k: int) -> int:

        def idx(char): return ord(char)-ord('a')

        dp = [[0]*26 for _ in range(len(s)+1)]

        for pos in range(1, len(s)+1):
            for last in range(26):
                if abs(last - idx(s[pos-1])) > k: dp[pos][last] = dp[pos-1][last]
                else: 
                    take = dp[pos-1][idx(s[pos-1])]+1
                    notake = dp[pos-1][last]
                    dp[pos][last] = max(take, notake)
    
        return max(dp[-1])