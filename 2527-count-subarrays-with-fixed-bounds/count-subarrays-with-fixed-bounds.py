class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        mn = mx = block = -1
        minfound = maxfound = False
        tot = 0
        for i, val in enumerate(nums):
            if val > maxK or val < minK: 
                mn = mx = block = i
                minfound = maxfound = False
                continue
            if val == minK: minfound = True; mn = i
            if val == maxK: maxfound = True; mx = i
            if minfound and maxfound:
                tot += min(mn, mx) - block
        return tot