class Solution:
    def grayCode(self, n: int) -> List[int]:
        def getIndex(l, r, x):
            mid = (l+r)//2
            if r-l <= 1: return x
            if x <= mid: return getIndex(l, mid, x)
            else: return getIndex(mid+1, r, r-x+mid+1)
        
        end_point = (1<<n) - 1
        return [getIndex(0, end_point, i) for i in range(end_point + 1)]