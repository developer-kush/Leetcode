class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces, res = set(spaces), ""
        for idx, ch in enumerate(s):
            if idx in spaces: res += ' '
            res += ch
        return res