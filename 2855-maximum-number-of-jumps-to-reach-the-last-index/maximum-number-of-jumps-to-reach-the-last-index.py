class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        memo = [-1]*len(nums)
        memo[0] = 0

        for curr in range(1,len(nums)):
            for last in range(curr-1,-1,-1):
                if abs(nums[curr]-nums[last]) <= target:
                    if memo[last] == -1: continue
                    memo[curr] = max(memo[curr], memo[last]+1)
        return memo[-1]