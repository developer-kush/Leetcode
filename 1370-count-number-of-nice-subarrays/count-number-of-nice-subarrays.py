class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        cnt = res = 0
        ctr = Counter({0 : 1})

        for r in range(len(nums)):
            if nums[r]&1: cnt += 1
            ctr[cnt] += 1
            res += ctr[cnt-k]
        
        return res