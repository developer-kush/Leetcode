class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        cnt = res = 0
        ctr = [1]

        for r in range(len(nums)):
            if nums[r]&1: cnt += 1
            if cnt <= len(ctr): ctr.append(0)
            ctr[cnt] += 1
            if cnt-k >= 0: res += ctr[cnt-k]
        
        return res