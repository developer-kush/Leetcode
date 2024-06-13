class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        
        def cdiff(a, b): return min(abs(ord(a)-ord(b)), 26-abs(ord(a)-ord(b)))
        
        if k == 0: return s
        res = ""
        for char in s:
            adiff = cdiff(char, 'a')
            if adiff <= k: 
                k-=adiff
                res += 'a'
            elif k:
                res += chr(ord(char)-k)
                k = 0
            else: res += char
            
        return res