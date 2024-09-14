class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        bitwand = max(nums)
        res = off = 0
        while True:
            try: pos = nums.index(bitwand, off)
            except: break
            l, r = pos-1, pos+1
            while l >= 0 and bitwand & nums[l] == bitwand: l -= 1
            while r < len(nums) and bitwand & nums[r] == bitwand: r += 1
            res = max(res, r-l-1)
            off = r
        return res