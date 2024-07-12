class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        
        @cache
        def rec(l, r):
            n = r-l+1
            if n <= 1: return 0

            maxleft = list(arr[l:r+1])
            maxright = list(maxleft)
            for i in range(1, len(maxleft)):
                maxleft[i] = max(maxleft[i], maxleft[i-1])
            for i in range(len(maxright)-2, -1, -1):
                maxright[i] = max(maxright[i], maxright[i+1])
            
            res = inf

            for i in range(1, n):
                res = min(res, maxleft[i-1] * maxright[i] + rec(l, l+i-1)+ rec(l+i, r))

            return res

        return rec(0, len(arr)-1)