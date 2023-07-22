class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = {}
        
        def rec(pos):
            if pos in memo: return memo[pos]
            if pos == 0: return nums[0]
            if pos == 1: return max(nums[0], nums[1])
            memo[pos] = max(rec(pos-1), nums[pos]+rec(pos-2))
            return memo[pos]

        return rec(len(nums)-1)