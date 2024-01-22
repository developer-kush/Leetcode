class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res=-1
        vals=set()
        for i in nums:
            if i in vals: res=i
            vals.add(i)
        for i in range(len(nums)):
            if i+1 not in vals:
                return [res,i+1]