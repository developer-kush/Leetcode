class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        lis_b = []
        lis = [0]*(n+1)
        lcopy = 0
        
        for i in range(n-1, -1, -1):
            if not lis_b or nums[i] > lis_b[-1]: lis_b.append(nums[i])
            else: 
                pos = bisect_left(lis_b, nums[i])
                lis_b[pos] = nums[i]
            lis[i] = len(lis_b)
        
        res = inf
        lis_f = []
        for i in range(n):
            if not lis_f or nums[i] > lis_f[-1]: lis_f.append(nums[i])
            else: 
                pos = bisect_left(lis_f, nums[i])
                lis_f[pos] = nums[i]

            if len(lis_f)==1 or lis[i]==1: continue

            moun = len(lis_f) + lis[i] - 1
            res = min(res, n-moun)
            
        return res