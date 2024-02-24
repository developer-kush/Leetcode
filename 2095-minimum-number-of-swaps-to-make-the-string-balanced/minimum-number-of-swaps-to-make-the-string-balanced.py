class Solution:
    def minSwaps(self, s: str) -> int:
        opens = res = 0
        for ch in s:
            if ch == '[': opens += 1
            elif opens: opens -= 1
            else: res, opens = res + 1, opens + 1
        return res