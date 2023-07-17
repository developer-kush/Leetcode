class Solution:
    def gcdOfStrings(self, a: str, b: str) -> str:
        
        s = a+b
        for i in range(min(len(a), len(b))-1,-1,-1):
            if len(s)%(i+1) == 0 :
                if s[:i+1]*(len(b)//(i+1)) == b and s[:i+1]*(len(a)//(i+1)) == a:
                    return s[:i+1]
        return ""

# 1 -> 2 -> 4