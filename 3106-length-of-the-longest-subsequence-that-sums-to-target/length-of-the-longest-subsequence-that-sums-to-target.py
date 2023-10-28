class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        
        nums = sorted(nums)
        dp = [float('-inf')]*(target+1)
        dp[0] = 0
        
        for i in range(1, len(nums)+1):
            memo = [0]*(target+1)
            for j in range(1, target+1):
                if nums[i-1] <= j: memo[j] = max(dp[j], dp[j-nums[i-1]]+1)
                else: memo[j] = dp[j]
            dp = memo
        
        return dp[-1] if dp[-1]!=float('-inf') else -1