class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        res = nums[1]-nums[0]
        for i in range(2, len(nums)):
            res = min(res, nums[i]-nums[i-1])
        return res