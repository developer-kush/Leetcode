class Solution:
    def smallestNumber(self, pattern: str) -> str:
        num = list(map(str, range(1, len(pattern)+2)))
        pairs = []
        for i in range(len(pattern)):
            if pattern[i] == 'I': continue
            if not i or pattern[i-1] == 'I': pairs.append([i, i])
            pairs[-1][1] = i
        
        for u, v in pairs: num[u: v+2] = num[u: v+2][::-1]

        return ''.join(num)