class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        diffs = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]
        l = res = 0
        for r in range(len(s)):
            maxCost -= diffs[r]
            while maxCost < 0: 
                maxCost += diffs[l]
                l += 1
            
            res = max(res, r+1 - l)
        return res