class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:

        def solve(l, r):
            if r-l <= 1: return True
            subarr = sorted(nums[l:r+1])
            k = subarr[1]-subarr[0]
            return not any(subarr[i]-subarr[i-1]!=k for i in range(2, len(subarr)))
        
        return [solve(x, y) for x, y in zip(l, r)]