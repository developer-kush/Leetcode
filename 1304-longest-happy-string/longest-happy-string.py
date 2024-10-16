class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        d = {'a':a, 'b':b, 'c':c}
        res = max(d, key=lambda x: d[x])
        d[res]-=1

        cnt = 0
        while True:
            ch = max(d, key=lambda x:d[x])
            if len(res)>=2 and res[-1]==res[-2]==ch:
                ch = max((key for key in d if key!=ch), key=lambda x:d[x])
            
            if d[ch] <= 0: break
            
            res += ch
            d[ch]-=1

        return res