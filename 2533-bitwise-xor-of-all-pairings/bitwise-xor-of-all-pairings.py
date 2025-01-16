class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        if len(nums1)&1: res ^= reduce(lambda x, y: x^y, nums2)
        if len(nums2)&1: res ^= reduce(lambda x, y: x^y, nums1)
        return res