class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        resset = set(nums1).intersection(set(nums2))
        if len(resset): return min(resset)
        return -1