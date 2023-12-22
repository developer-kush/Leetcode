class Solution:
    def maxScore(self, s: str) -> int:
        res = tot = 0
        totones = s.count('1')
        for i in range(len(s)-1): 
            tot += (s[i]=='0')
            totones -= (s[i]=='1')
            res = max(res, tot+totones)

        return res