class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        indices = {}
        for idx, ch in enumerate(s):
            if ch not in indices: indices[ch] = [idx, idx]
            else: indices[ch][-1] = idx
        res = ""
        return max(val[1]-val[0]-1 for val in indices.values())