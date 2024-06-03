class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if b in a: return 1
        if b in a + a: return 2
        if len(a) > len(b): return -1

        n = len(b)//len(a)

        if b == a*n: return n
        if len(b)%len(a)==0: n-=1

        a = a*n
        occs = [m.start() for m in re.finditer(a, b)]
        
        for occ in occs:
            res = n
            pref = b[:occ]
            suff = b[occ + len(a):]

            if not a.startswith(suff): continue
            if not a.endswith(pref): continue

            if pref: res += 1
            if suff: res += 1
            return res
            
        return -1