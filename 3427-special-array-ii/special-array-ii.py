class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        tot = 0
        dp = []
        for i in range(len(nums)-1):
            if nums[i]&1 != nums[i+1]&1: tot += 1
            dp.append(tot)
            
        res = []
        for l, r in queries:
            if l == r: res.append(True)
            elif l == 0: res.append(dp[r-1]==r)
            else: res.append((dp[r-1]-dp[l-1])==r-l)
        
        return res