class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        tot = l = 0
        ctr = Counter()
        for r in range(len(s)):
            ctr[s[r]]+=1
            while ctr[s[r]]>=k:
                ctr[s[l]]-=1
                l+=1
            tot += l
        return tot