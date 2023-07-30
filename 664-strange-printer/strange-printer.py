class Solution:
    def strangePrinter(self, s: str) -> int:
        
        @cache
        def rec(x, y):
            if x == y: return 1
            if all(s[i]==s[i+1] for i in range(x,y)): return 1
            j = -1
            res = float('inf')
            for i in range(x,y):
                if s[i] != s[y] and j==-1: j = i
                if j!=-1: res = min(res, rec(j,i)+rec(i+1,y))
            return res

        return rec(0, len(s)-1)