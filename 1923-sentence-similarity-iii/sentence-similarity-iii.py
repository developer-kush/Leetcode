class Solution:
    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        if s1 == s2: return True

        s1, s2 = sorted([s1, s2], key=len)
        a = s1.split()
        b = s2.split()
        
        while a and a[-1] == b[-1]: a.pop(); b.pop()
        a, b = a[::-1], b[::-1]
        while a and a[-1] == b[-1]: a.pop(); b.pop()
        
        return not a