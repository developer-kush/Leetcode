class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        if any(abs(val-idx) > 1 for idx,val in enumerate(nums)):
            return False
        return True