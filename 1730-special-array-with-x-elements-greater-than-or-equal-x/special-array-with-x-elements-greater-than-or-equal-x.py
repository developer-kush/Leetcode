class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)+1):
            pos = len(nums) - bisect_left(nums, i)
            if i == pos: return i
        return -1