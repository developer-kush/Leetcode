class Solution:
    def maximumLength(self, s: str) -> int:

        ctr = Counter()

        cnt = 1
        for i in range(1, len(s)):
            if s[i-1]!=s[i]: ctr[s[i-cnt:i]] += 1; cnt = 1
            else: cnt += 1
        ctr[s[len(s)-cnt:]] += 1

        # print(ctr)
        
        resmax = -1

        for key, val in ctr.items():
            if len(key) >= 3: resmax = max(resmax, len(key)-2)
            if val >= 3: resmax = max(resmax, len(key))
            if val == 2 and len(key)>1: resmax = max(resmax, len(key)-1)
            tkey = key[1:]
            if tkey == '': continue
            if tkey in ctr: resmax = max(resmax, len(tkey))

        return resmax