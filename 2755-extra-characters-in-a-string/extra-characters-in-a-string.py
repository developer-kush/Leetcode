class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        words = set(dictionary)
        
        @cache
        def rec(pos):
            if pos >= len(s): return 0
            mn = float('inf')
            for i in range(pos, len(s)):
                if s[pos:i+1] in words: curr = rec(i+1)
                else: curr = i+1-pos + rec(i+1)
                mn = min(mn, curr)
            return mn
        
        return rec(0)