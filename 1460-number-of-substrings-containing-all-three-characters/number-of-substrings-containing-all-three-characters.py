class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ctr, l = Counter(), 0
        tot = 0
        for r in range(len(s)):
            ctr[s[r]] += 1
            while l < r and ctr[s[l]] > 1: 
                ctr[s[l]] -= 1
                l += 1
            if ctr['a'] and ctr['b'] and ctr['c']: tot += l+1
        return tot