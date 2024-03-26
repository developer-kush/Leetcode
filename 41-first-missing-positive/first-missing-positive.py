class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums=set(nums)
        for i in range(1,5*(10**5)+1):
            if i not in nums: return i
        return 500001