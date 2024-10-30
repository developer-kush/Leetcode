class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        lis_b = []
        lis = [0]*(n+1)
        lis_cpy = [0]*(n+1)
        lisb_last = [0]*(n+1)
        lcopy = 0
        
        for i in range(n-1, -1, -1):
            if not lis_b or nums[i] > lis_b[-1]: 
                lcopy = 0
                lis_b.append(nums[i])
            else: 
                pos = bisect_left(lis_b, nums[i]) 
                if pos == len(lis_b)-1 and lis_b[pos] != nums[i]: lcopy = 1
                lis_b[pos] = nums[i]
            lis_cpy[i] = lcopy
            lis[i] = len(lis_b)
            lisb_last[i] = lis_b[-1]
        
        res = inf
        lis_f = []
        lcopy = 0
        for i in range(n):
            if not lis_f or nums[i] > lis_f[-1]: 
                lcopy = 0
                lis_f.append(nums[i])
            else: 
                pos = bisect_left(lis_f, nums[i]) 
                if pos == len(lis_f)-1 and lis_f[pos] != nums[i]: lcopy = 1
                lis_f[pos] = nums[i]

            if len(lis_f)==1 or lis[i]==1: continue
            
            moun = len(lis_f) + lis[i]
            if lis_f[-1] == lisb_last[i] and not lcopy and not lis_cpy[i]: moun -= 1
            print(i, ":", moun)
            res = min(res, n-moun)
            
        return res