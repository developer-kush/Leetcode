class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        s1, s2 = set(nums1), set(nums2)
        a, b, both = len(s1), len(s2), len(s1&s2)
        onlya, onlyb = a-both, b-both

        tot = min(n>>1, onlya)+min(n>>1, onlyb)+both

        return min(n, tot)