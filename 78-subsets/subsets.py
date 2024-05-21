class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        curr=[]
        def rec(pos):
            if pos==len(nums): 
                res.append(list(curr))
                return
            rec(pos+1)
            curr.append(nums[pos])
            rec(pos+1)
            curr.pop()
        rec(0)
        return res