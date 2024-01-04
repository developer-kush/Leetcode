class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ctr = Counter(nums)
        res = 0
        for key, val in ctr.items():
            if val  == 1: return -1
            res += ceil(val/3)
        return res