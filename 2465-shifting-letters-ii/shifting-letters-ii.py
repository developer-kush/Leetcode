class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        new = [0]*(len(s)+1)
        for u, v, d in shifts:
            if not d:
                new[u] -=1 
                new[v+1] += 1
            else:
                new[u] += 1
                new[v+1] -= 1
        
        res = ""
        curr = 0
        for i in range(len(s)):
            curr += new[i]
            res += chr(((ord(s[i])-97) + curr)%26 + 97)
        return res