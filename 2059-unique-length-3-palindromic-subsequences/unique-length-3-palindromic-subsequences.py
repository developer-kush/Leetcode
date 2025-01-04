class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        tc = Counter(s)
        c = Counter()

        res = set()

        for ch in s:
            tc[ch] -= 1
            for char in range(97, 123):
                char = chr(char)
                if tc[char] and c[char]: res.add(char+ch)
            c[ch] += 1
        
        return len(res)