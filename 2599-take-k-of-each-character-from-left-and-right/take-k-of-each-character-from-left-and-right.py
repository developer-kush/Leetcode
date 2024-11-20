class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n, freq  = len(s), Counter(s)
        if any(freq[val] < k for val in "abc"): return -1

        freq[s[-1]] -= 1

        l, res = 0, n
        s *= 2
        for r in range(n-1, len(s)):
            freq[s[r]] += 1
            while l < n and freq[s[l]] > k: 
                freq[s[l]] -= 1
                l += 1
            res = min(res, r-l+1)

        return res