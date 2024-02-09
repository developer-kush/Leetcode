class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()

        prev = {}

        dp = {}
        for val in nums:
            res = 0
            prev[val] = -1
            for i in range(1, int(sqrt(val))+1):
                if val%i==0: 
                    if dp.get(i, 0) > res: res, prev[val] = dp[i], i
                    i = val//i
                    if dp.get(i, 0) > res: res, prev[val] = dp[i], i
            dp[val] = res + 1

        maxval = max(dp.values())
        for key in dp:
            if dp[key] == maxval: break

        res = []
        while key != -1:
            res.append(key)
            key = prev[key]
        
        return res