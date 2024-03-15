class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        currproduct=1
        for i in nums:
            res.append(currproduct)
            currproduct*=i
        currproduct=1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=currproduct
            currproduct*=nums[i]
        return res