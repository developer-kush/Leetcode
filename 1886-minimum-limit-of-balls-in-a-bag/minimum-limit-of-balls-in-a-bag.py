class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        
        def possible(x):
            res = 0
            for balls in nums:
                if balls > x: res += (balls-1)//x
            return res <= maxOperations
        
        l, r = 1, max(nums)
        while l < r:
            m = (l+r)>>1
            if possible(m): r = m 
            else: l = m + 1 
        return l