class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        ctr = Counter(s1)
        c2 = Counter(s2[:n-1])
        for i in range(n-1, len(s2)):
            c2[s2[i]] += 1
            if ctr == c2: return True
            c2[s2[i-n+1]] -= 1
        return False