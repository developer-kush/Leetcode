class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        freqs = Counter(s)

        ans = set()
        parsedletters = set()
        for i in s:
            freqs[i]-=1
            for j in parsedletters:
                if freqs[j]:
                    ans.add(i+j)
            parsedletters.add(i)

        return len(ans)