class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        zia = nums1.count(0)
        zib = nums2.count(0)
        sa, sb = sum(nums1), sum(nums2)
        if not zib and not zia and sa != sb: return -1
        if not zib and sa + zia > sb : return -1
        if not zia and sb + zib > sa : return -1
        return max(sa+zia, sb+zib)