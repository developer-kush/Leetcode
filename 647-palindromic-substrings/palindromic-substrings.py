class Solution:
    def countSubstrings(self, s: str) -> int:
        tot = 0
        n = len(s)
        for i in range(n):
            l = r = i
            while l >= 0 and r < n and s[l]==s[r]:
                tot += 1
                l -= 1
                r += 1
        for i in range(1, n):
            l, r = i-1, i
            while l >= 0 and r < n and s[l]==s[r]:
                tot += 1
                l -= 1
                r += 1
        return tot
            