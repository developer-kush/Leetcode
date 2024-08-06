class Solution:
    def minimumPushes(self, word: str) -> int:
        arr = sorted(Counter(word).values(), reverse = True)
        tot = 0
        groups = [0]*8
        for val in arr:
            mn = min(groups)
            idx = groups.index(mn)
            tot += val*(mn+1)
            groups[idx] += 1
        return tot