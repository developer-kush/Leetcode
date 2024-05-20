class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        tot = 0
        for i in range(1<<len(nums)):
            curr = ptr = 0
            while i:
                if i&1: curr ^= nums[ptr]
                ptr += 1
                i >>= 1
            tot += curr
        return tot