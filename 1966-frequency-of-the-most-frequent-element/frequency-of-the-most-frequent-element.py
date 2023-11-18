class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = l = 0

        for r in range(1, len(nums)):
            k -= (r-l)*(nums[r]-nums[r-1])
            while l < r and k < 0:
                k += nums[r]-nums[l]
                l += 1
            res = max(res, r-l)

        return res + 1