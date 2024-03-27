class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l, res, totprod = -1, 0, 1
        for idx, val in enumerate(nums):
            totprod *= val
            while totprod >= k and l < idx: 
                l += 1
                totprod //= nums[l]
            res += idx-l
        return res