class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
            
        res=[nums[0]]
        
        for i in range(1,len(nums)):
            if nums[i]>res[-1]: res.append(nums[i])
            else: res[bisect_left(res, nums[i])]=nums[i]
        
        return len(res)