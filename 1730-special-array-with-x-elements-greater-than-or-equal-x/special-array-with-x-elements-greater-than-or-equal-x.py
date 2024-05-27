class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        n = len(nums)
        if nums[-1] >= n: return n
        for i in range(1, n):
            if nums[i] < i and nums[i-1] >= i: return i
        return -1