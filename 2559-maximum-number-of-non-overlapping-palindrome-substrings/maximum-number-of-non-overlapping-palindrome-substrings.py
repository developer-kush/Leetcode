class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        pals = defaultdict(list)

        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 >= k: pals[r].append(l)
                l, r = l-1, r+1
            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 >= k: pals[r].append(l)
                l, r = l-1, r+1
        
        dp = [0]
        for i in range(n):
            dpi = dp[-1]
            if i in pals: dpi = max(dpi, 1+dp[pals[i][-1]])
            dp.append(dpi)
        
        return dp[-1]