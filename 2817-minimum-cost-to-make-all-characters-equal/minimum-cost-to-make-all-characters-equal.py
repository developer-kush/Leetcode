class Solution:
    def minimumCost(self, s: str) -> int:
        n = len(s)
        if n == 1: return 0
        
        pre, post = [0]*len(s), [0]*len(s)
        for i in range(1, len(s)):
            if s[i]!=s[i-1]: pre[i] = pre[i-1] + i
            else: pre[i] = pre[i-1]
        for i in range(len(s)-2, -1, -1):
            if s[i]!=s[i+1]: post[i] = post[i+1] + n-i-1
            else: post[i] = post[i+1]

        return min(
            pre[-1], post[0], 
            min(
                pre[i]+post[i+1]+
                (min(i+1, n-i) if s[i]!=s[i+1] else 0) 
                for i in range(len(s)-1)
            )
        )