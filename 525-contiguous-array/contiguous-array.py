class Solution:
    
    def findMaxLength(self, nums: List[int]) -> int:

        diff = { 0: -1 }
        ones = zero = res = 0

        for idx,i in enumerate(nums):
            if i: ones += 1
            else: zero += 1
            if ones-zero not in diff: diff[ones-zero] = idx
            res = max(res, idx-diff[ones-zero])
        
        return res