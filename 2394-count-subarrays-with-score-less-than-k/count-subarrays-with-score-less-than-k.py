class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        tot = sm = cnt = l = 0
        for r in range(len(nums)):
            sm += nums[r]
            cnt += 1
            while sm*cnt >= k : 
                sm -= nums[l]
                cnt -= 1
                l += 1
            tot += r-l+1
        return tot