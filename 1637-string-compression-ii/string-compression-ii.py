class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        if k==len(s): return 0
        def ln(n): return 0 if n==1 else 1 if n<10 else 2 if n<100 else 3
        
        def rec(i,k,last,l,memo={}):
            if (i,k,last,l) in memo:
                return memo[(i,k,last,l)]
            if k<0:
                return float('inf')
            elif i<0:
                return 0
            if s[i]==last:
                ans=int(l in (1,9,99))+rec(i-1,k,last,l+1,memo)
            else:
                ans=min(1+rec(i-1,k,s[i],1,memo),rec(i-1,k-1,last,l,memo))
            memo[(i,k,last,l)]=ans
            return ans
        
        return rec(len(s)-1,k,'.',0)
            