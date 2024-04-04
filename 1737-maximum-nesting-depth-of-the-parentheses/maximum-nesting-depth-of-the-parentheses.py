class Solution:
    def maxDepth(self, s: str) -> int:
        tot = res = 0
        for ch in s:
            if ch == '(': tot += 1
            if ch == ')': tot -= 1
            res = max(res, tot)
        return res