class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        
        first = nums[0]
        second = max(nums[0], nums[1])
        third = second

        for i in range(2, len(nums)):
            third = max(second, nums[i]+first)
            first = second
            second = third
        
        return third
        