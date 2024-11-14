class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l, r = 1, max(quantities)

        def possible(x):
            nonlocal n, quantities
            cnt = 0
            for num in quantities: cnt += ceil(num/x)
            return cnt <= n
        
        while l < r: 
            m = (l+r)>>1
            if possible(m): r = m
            else: l = m + 1
        return l