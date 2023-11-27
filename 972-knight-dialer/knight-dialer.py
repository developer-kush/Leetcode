class Solution:
    def knightDialer(self, n: int) -> int:

        MOD = int(1e9 +7)

        mapping = {
            0: [4, 6], 1:[6, 8], 2:[7, 9], 3: [4, 8], 4:[0, 3, 9],
            6: [0, 1, 7], 7:[2, 6], 8:[1, 3], 9:[2, 4]
        }

        dp = [1]*10
        for i in range(n-1):
            curr = [0]*10
            for i in range(10): 
                if i == 5: continue
                curr[i] = sum(dp[val] for val in mapping[i])
            dp = curr

        return sum(dp)%MOD