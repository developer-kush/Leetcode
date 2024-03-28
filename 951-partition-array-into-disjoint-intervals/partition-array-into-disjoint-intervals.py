class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        maxel, minel = nums[0], list(nums)
        for i in range(len(nums)-2, -1, -1): minel[i] = min(minel[i], minel[i+1])
        for i in range(1, len(nums)):
            if maxel <= minel[i]: return i
            maxel = max(maxel, nums[i])
        return len(nums)