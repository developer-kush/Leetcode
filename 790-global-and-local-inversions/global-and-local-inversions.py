class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        currmax = 0
        for i in range(1, len(nums)):
            if nums[i] < currmax: return False
            currmax = max(currmax, nums[i-1])
        return True