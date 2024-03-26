class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        
        def findSubs(l, r):
            res = ((r-l)*(r-l+1))>>1
            cnt = 0
            for i in range(l, r):
                if nums[i] < left:
                    cnt += 1
                else:
                    if cnt: res -= (cnt * (cnt + 1)) >> 1
                    cnt = 0
            if cnt: res -= (cnt * (cnt + 1)) >> 1
            return res
        
        tot = last = 0
        for i in range(len(nums)):
            if nums[i] > right:
                tot += findSubs(last, i)
                last = i + 1
        
        if last < len(nums): tot += findSubs(last, len(nums))

        return tot