class Solution:
    def minChanges(self, s: str) -> int:
        cnt = 1
        last = tot = 0
        for i in range(1,len(s)):
            if s[i]==s[i-1]: cnt += 1
            else:
                if not last and cnt&1: last, tot = 1, tot+1
                elif last and not cnt&1: last, tot = 1, tot+1
                else: last = 0
                cnt = 1
        return tot