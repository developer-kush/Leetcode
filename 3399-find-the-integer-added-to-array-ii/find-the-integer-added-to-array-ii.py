class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()

        res = float('inf')

        for i in range(len(nums1)):
            for j in range(i+1, len(nums1)):
                x = y = 0
                if i == 0 and j == 1: x = 2
                elif i == 0: x = 1
                else: x = 0
                diff = nums2[y] - nums1[x]

                while x < len(nums1):
                    if x == i or x == j: x += 1; continue
                    if nums2[y] - nums1[x] != diff: break
                    x, y = x+1, y+1
                else: res = min(res, diff)

        return res