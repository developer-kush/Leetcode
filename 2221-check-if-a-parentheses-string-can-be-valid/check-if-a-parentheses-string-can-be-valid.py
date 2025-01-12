class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n&1: return False
        
        ro, to, co = (n>>1)-sum(1 for i in range(n) if s[i]=='(' and locked[i]=='1'), 0, 0

        s = list(s)

        for i in range(n):
            if locked[i] == '1':
                if s[i] == '(': 
                    co += 1
                else: 
                    if not co: return False
                    co -= 1
            else:
                if ro:
                    co += 1
                    ro -= 1
                else:
                    if not co: return False
                    co -= 1
        if co: return False
        
        return True