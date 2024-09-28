class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = -1
        ctr = Counter()
        res = 0
        for r in range(len(s)):
            ctr[s[r]] += 1
            while r-l-max(ctr.values()) > k:
                l += 1
                ctr[s[l]] -= 1
            res = max(res, r-l)
        
        return res