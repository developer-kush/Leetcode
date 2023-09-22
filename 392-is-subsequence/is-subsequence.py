class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr = 0
        for letter in s:
            while ptr<len(t) and t[ptr]!=letter: ptr+=1
            if ptr == len(t): return False
            ptr += 1
        return True