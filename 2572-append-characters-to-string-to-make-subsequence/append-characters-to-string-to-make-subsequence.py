class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        tpos=0
        for i in s:
            if i==t[tpos]: tpos+=1
            if tpos==len(t): return 0
        return len(t)-tpos