class Solution:
    def minInsertions(self, s: str) -> int:
        rev = s[::-1]

        @lru_cache(6500)
        def lps(x, y):
            if x < 0 or y < 0: return 0
            if s[x] == rev[y]: return lps(x-1, y - 1) + 1
            else: return max(lps(x-1, y), lps(x, y-1))

        return len(s) - lps(len(s)-1, len(s)-1)