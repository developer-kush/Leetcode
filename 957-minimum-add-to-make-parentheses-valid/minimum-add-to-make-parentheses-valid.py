class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opens = res = 0
        for ch in s:
            if ch == '(': opens += 1
            elif ch == ')':
                if opens: opens -= 1
                else: res += 1
        return res + opens