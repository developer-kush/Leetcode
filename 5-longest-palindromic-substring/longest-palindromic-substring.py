def expand(s,i,j):
    if s[i]!=s[j]: return ""
    while i>=0 and j<len(s) and s[i] == s[j]:
        i-=1 
        j+=1
    return s[i+1:j]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        res=''
        for i in range(n):
            res = max(res, expand(s,i,i), key=len)
            if i<n-1: res = max(res, expand(s,i,i+1), key=len)
        return res