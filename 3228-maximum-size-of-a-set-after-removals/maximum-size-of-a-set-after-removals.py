class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        s1, s2 = set(nums1), set(nums2)
        a, b, both = len(s1), len(s2), len(s1&s2)
        
        return min(n, min(n>>1, a-both)+min(n>>1, b-both)+both)