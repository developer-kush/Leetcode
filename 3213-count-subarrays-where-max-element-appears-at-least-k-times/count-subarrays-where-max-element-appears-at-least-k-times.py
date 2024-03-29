class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mxel = max(nums)
        tot = l = cnt = 0
        for r in range(len(nums)):
            if nums[r]==mxel: cnt+=1
            while cnt >= k:
                if nums[l] == mxel: cnt -= 1
                l += 1 
            tot += l
        return tot