def expand(s,i,j):
    res=[i,j]
    while 0<=i<=j<len(s) and s[i]==s[j]:
        res=[max(0,i),min(len(s)-1,j)]
        i-=1
        j+=1
    return res
    

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        res=[0,0]
        for i in range(n):
            s1=expand(s,i,i)
            if i<n-1 and s[i]==s[i+1]:
                s2=expand(s,i,i+1)
            else: s2=[0,0]
            res=max(res,s1,s2,key=lambda x: x[1]-x[0]+1)
        return s[res[0]:res[1]+1]