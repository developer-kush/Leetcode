class Solution:
    def minSwaps(self, s: str) -> int:
        opens = 0
        for ch in s:
            if ch == '[': opens += 1
            elif opens: opens -= 1
            else: opens += 1
        return opens >> 1