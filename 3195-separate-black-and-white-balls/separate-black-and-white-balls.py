class Solution:
    def minimumSteps(self, s: str) -> int:
        s = s.lstrip('0')
        if s == '': return 0
        tot = ptr = 0
        for i in range(1, len(s)):
            if s[i] == '0': 
                tot += i-ptr
                ptr+=1
        
        return tot