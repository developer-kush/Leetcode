class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        res = 0
        nums.sort()

        curr = float('-inf')
        for num in nums:
            if curr <= num: 
                curr = num + 1
            else: 
                res += curr - num
                curr += 1
        
        return res