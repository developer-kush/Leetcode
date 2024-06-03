class Solution:
    def minInsertions(self, s: str) -> int:
        
        @cache
        def rec(x, y):
            if y <= x: return 0
            if s[x] == s[y]: return rec(x+1, y-1)
            return min(rec(x+1, y), rec(x, y-1))+1
        
        return rec(0, len(s)-1)