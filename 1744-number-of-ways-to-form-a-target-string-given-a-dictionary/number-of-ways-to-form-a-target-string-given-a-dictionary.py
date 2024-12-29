class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        ctr = [Counter() for _ in range(len(words[0]))]
        for word in words:
            for idx, ch in enumerate(word):
                ctr[idx][ch] += 1
        
        @cache
        def rec(x, y):
            if y < 0: return 1
            if x < 0: return 0
            return rec(x-1, y) + rec(x - 1, y - 1)*ctr[x][target[y]]

        return rec(len(ctr)-1, len(target)-1)%(10**9+7)