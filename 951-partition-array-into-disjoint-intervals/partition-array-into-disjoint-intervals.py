class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        maxel = list(nums)
        for i in range(1, len(nums)): maxel[i] = max(maxel[i], maxel[i-1])
        minel = list(nums)
        for i in range(len(nums)-2, -1, -1): minel[i] = min(minel[i], minel[i+1])
        for i in range(1, len(nums)):
            if maxel[i-1] <= minel[i]: return i
        return len(nums)