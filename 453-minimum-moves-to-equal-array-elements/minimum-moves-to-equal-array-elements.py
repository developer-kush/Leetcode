class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mn = min(nums)
        return sum(val-mn for val in nums)