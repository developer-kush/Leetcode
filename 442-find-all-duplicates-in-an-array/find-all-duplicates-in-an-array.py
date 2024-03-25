class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        return [nums[i] for i in range(1,len(nums)) if nums[i] == nums[i-1]]