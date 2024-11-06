class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def setCount(n):
            tot = 0
            while n: 
                tot += n&1
                n>>=1
            return tot
        
        groups = [[nums[0]]]
        for i in range(1, len(nums)):
            if setCount(nums[i-1])==setCount(nums[i]):
                groups[-1].append(nums[i])
            else:
                groups.append([nums[i]])
        
        groups = [sorted(arr) for arr in groups]
        finalarr = []
        for group in groups:
            for val in group: finalarr.append(val)
                
        return sorted(nums) == finalarr