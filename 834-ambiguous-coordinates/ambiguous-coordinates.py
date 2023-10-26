class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        s = s[1:-1]
        res = []
        for i in range(1, len(s)):
            for j in range(i,len(s)):
                for k in range(j+1, len(s)+1):
                    if (i > 1 and s[0] == '0') or (i != j and s[j-1] == '0'): continue
                    if (k - j > 1 and s[j] == '0') or (k < len(s) and s[-1] == '0'): continue
                    b = s[i:j]
                    d = s[k:]
                    res.append(f"({s[:i]}{'.'+b if b else ''}, {s[j:k]}{'.'+d if d else ''})")
        return res