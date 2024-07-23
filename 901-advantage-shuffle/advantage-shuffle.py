class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        order = sorted(range(n), key = lambda i: nums2[i])
        nums1 = sorted(nums1)

        res = [-1]*n

        ptr = 0
        for i in range(n):
            idx = order[i]
            while ptr < n and nums1[ptr] <= nums2[idx]: ptr += 1
            if ptr >= n: break
            res[idx] = nums1[ptr]
            nums1[ptr] = -1
            ptr += 1

        rem = [val for val in nums1 if val != -1]
        ln = len(rem)
        for i in range(-ln, 0):
            res[order[i]] = rem[i]
        
        return res