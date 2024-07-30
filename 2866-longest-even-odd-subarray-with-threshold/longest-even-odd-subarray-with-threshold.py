class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        orig = list(nums)

        n = len(nums)
        for i in range(n): nums[i] &= 1

        if 0 not in nums: return 0

        res = 0
        
        ptr = 0
        while ptr < len(nums):
            if nums[ptr] or orig[ptr] > threshold: ptr += 1; continue
            cnt = 1
            ptr += 1
            while ptr < len(nums) and nums[ptr] != nums[ptr-1] and orig[ptr] <= threshold:
                cnt += 1
                ptr += 1
            res = max(res, cnt)

        return res