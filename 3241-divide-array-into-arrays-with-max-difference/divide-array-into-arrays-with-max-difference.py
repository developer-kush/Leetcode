class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        if any((nums[i]-nums[i-2]) > k for i in range(2, len(nums), 3)): return []
        return [nums[i:i+3] for i in range(0, len(nums), 3)]